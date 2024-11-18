import grpc
from concurrent import futures
import pubsub_pb2
import pubsub_pb2_grpc
from collections import defaultdict

class PubSubService(pubsub_pb2_grpc.PubSubServiceServicer):
    def __init__(self):
        # Subscrições organizadas por tópico
        self.subscriptions = defaultdict(list)  # {topic: [messages]}
        # Conexões ativas e filas independentes para cada subscriber
        self.subscriber_queues = defaultdict(lambda: defaultdict(list))  # {topic: {subscriber: [messages]}}

    def Publish(self, request, context):
        topic = request.topic
        message = request.message

        # Adiciona a mensagem na fila global do tópico
        self.subscriptions[topic].append(message)
        print(f"Mensagem publicada no tópico '{topic}': {message}")

        # Envia a mensagem para as filas de cada subscriber
        for subscriber_context in self.subscriber_queues[topic]:
            self.subscriber_queues[topic][subscriber_context].append(message)

        return pubsub_pb2.PublishResponse(status="Mensagem enviada com sucesso!")

    def Subscribe(self, request, context):
        for topic in request.topics:
            # Registra o contexto do subscriber se ainda não existir
            if context not in self.subscriber_queues[topic]:
                self.subscriber_queues[topic][context] = []

        print(f"Cliente inscrito nos tópicos: {', '.join(request.topics)}")

        try:
            while context.is_active():  # Mantém a conexão ativa enquanto o cliente estiver conectado
                for topic in request.topics:
                    # Verifica se há mensagens na fila do subscriber
                    if self.subscriber_queues[topic][context]:
                        message = self.subscriber_queues[topic][context].pop(0)
                        yield pubsub_pb2.Message(topic=topic, message=message)
        except grpc.RpcError as e:
            print(f"Erro durante a assinatura: {e.details()}")

        # Remove o contexto do subscriber ao final da conexão
        for topic in request.topics:
            if context in self.subscriber_queues[topic]:
                del self.subscriber_queues[topic][context]

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pubsub_pb2_grpc.add_PubSubServiceServicer_to_server(PubSubService(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor inicializado na porta 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
