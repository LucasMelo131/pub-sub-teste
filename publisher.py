import grpc
import pubsub_pb2
import pubsub_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pubsub_pb2_grpc.PubSubServiceStub(channel)
    response = stub.Publish(pubsub_pb2.PublishRequest(topic="example", message="Hello, World!"))
    print("Publish status: " + response.status)

if __name__ == '__main__':
    run()
