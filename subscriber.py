import grpc
import pubsub_pb2
import pubsub_pb2_grpc
import sys

def run_subscriber(topics):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pubsub_pb2_grpc.PubSubServiceStub(channel)
        response_stream = stub.Subscribe(pubsub_pb2.SubscribeRequest(topics=topics))
        print(f"Inscrito nos tópicos: {', '.join(topics)}")
        for message in response_stream:
            print(f"Recebido no tópico '{message.topic}': {message.message}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    topics = sys.argv[1:]
    run_subscriber(topics)
