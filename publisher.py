import grpc
import pubsub_pb2
import pubsub_pb2_grpc
import sys # para argumentos de linha de comando

def run_publisher(topic,message):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pubsub_pb2_grpc.PubSubServiceStub(channel)
        response = stub.Publish(pubsub_pb2.PublishRequest(topic=topic, message=message))
        print(f"Publish status: {response.status}")

if __name__ == "__main__":
    #garantir que seja digitado python publisher.py <topico> <mensagem>
    if len(sys.argv) != 3:
        sys.exit(1)

    topic = sys.argv[1]
    message = sys.argv[2]
    run_publisher(topic,message)