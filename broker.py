import grpc
from concurrent import futures
import pubsub_pb2
import pubsub_pb2_grpc

class PubSubService(pubsub_pb2_grpc.PubSubServiceServicer):
    def __init__(self):
        # Subscrições organizadas por tópico
        self.subscriptions = {}  # {topic: [messages]}
        # Conexões ativas para cada tópico
        self.active_subscribers = {}  # {topic: [contexts]}
    
    def Publish(self, request, context):
        topic = request.topic
        message = request.message

        # Adiciona o tópico se ele ainda não existir
        if topic not in self.subscriptions:
            self.subscriptions[topic] = []

        # Adiciona a mensagem ao tópico
        self.subscriptions[topic].append(message)
        print(f"Mensagem publicada no tópico '{topic}': {message}")
        return pubsub_pb2.PublishResponse(status="Mensagem enviada com sucesso!")
    
    def Subscribe(self, request, context):
        for topic in request.topics:
            if topic not in self.active_subscribers:
                self.active_subscribers[topic] = []

            # Registra o contexto do subscriber
            self.active_subscribers[topic].append(context)

        print(f"Cliente inscrito nos tópicos: {', '.join(request.topics)}")

        try:
            while context.is_active():  # Mantém a conexão ativa enquanto o cliente estiver conectado
                for topic in request.topics:
                    if topic in self.subscriptions and self.subscriptions[topic]:
                        # Envia a mensagem para o cliente
                        message = self.subscriptions[topic].pop(0)
                        yield pubsub_pb2.Message(topic=topic, message=message)
        except grpc.RpcError as e:
            print(f"Erro durante a assinatura: {e.details()}")

        # Remove o contexto do subscriber ao final da conexão
        for topic in request.topics:
            if topic in self.active_subscribers:
                self.active_subscribers[topic].remove(context)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pubsub_pb2_grpc.add_PubSubServiceServicer_to_server(PubSubService(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor inicializado na porta 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
