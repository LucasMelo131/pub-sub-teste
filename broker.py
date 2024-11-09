import grpc
from concurrent import futures
import time
import queue

import pubsub_pb2
import pubsub_pb2_grpc

class PubSubService(pubsub_pb2_grpc.PubSubServiceServicer):
    def __init__(self):
        self.subscribers = {}

    def Publish(self, request, context):
        topic = request.topic
        message = request.message
        if topic in self.subscribers:
            for subscriber in self.subscribers[topic]:
                subscriber.put(pubsub_pb2.Message(topic=topic, message=message))
        return pubsub_pb2.PublishResponse(status="Message published")

    def Subscribe(self, request, context):
        topic = request.topic
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        subscriber_queue = queue.Queue()
        self.subscribers[topic].append(subscriber_queue)
        while True:
            message = subscriber_queue.get()
            yield message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pubsub_pb2_grpc.add_PubSubServiceServicer_to_server(PubSubService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
