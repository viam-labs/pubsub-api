# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: pubsub.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
from . import pubsub_pb2


class PubsubServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Publish(self, stream: 'grpclib.server.Stream[pubsub_pb2.PublishRequest, pubsub_pb2.PublishResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Subscribe(self, stream: 'grpclib.server.Stream[pubsub_pb2.SubscribeRequest, pubsub_pb2.SubscribeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Unsubscribe(self, stream: 'grpclib.server.Stream[pubsub_pb2.UnsubscribeRequest, pubsub_pb2.UnsubscribeResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/viamlabs.services.pubsub.v1.PubsubService/Publish': grpclib.const.Handler(
                self.Publish,
                grpclib.const.Cardinality.UNARY_UNARY,
                pubsub_pb2.PublishRequest,
                pubsub_pb2.PublishResponse,
            ),
            '/viamlabs.services.pubsub.v1.PubsubService/Subscribe': grpclib.const.Handler(
                self.Subscribe,
                grpclib.const.Cardinality.UNARY_STREAM,
                pubsub_pb2.SubscribeRequest,
                pubsub_pb2.SubscribeResponse,
            ),
            '/viamlabs.services.pubsub.v1.PubsubService/Unsubscribe': grpclib.const.Handler(
                self.Unsubscribe,
                grpclib.const.Cardinality.UNARY_UNARY,
                pubsub_pb2.UnsubscribeRequest,
                pubsub_pb2.UnsubscribeResponse,
            ),
        }


class PubsubServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Publish = grpclib.client.UnaryUnaryMethod(
            channel,
            '/viamlabs.services.pubsub.v1.PubsubService/Publish',
            pubsub_pb2.PublishRequest,
            pubsub_pb2.PublishResponse,
        )
        self.Subscribe = grpclib.client.UnaryStreamMethod(
            channel,
            '/viamlabs.services.pubsub.v1.PubsubService/Subscribe',
            pubsub_pb2.SubscribeRequest,
            pubsub_pb2.SubscribeResponse,
        )
        self.Unsubscribe = grpclib.client.UnaryUnaryMethod(
            channel,
            '/viamlabs.services.pubsub.v1.PubsubService/Unsubscribe',
            pubsub_pb2.UnsubscribeRequest,
            pubsub_pb2.UnsubscribeResponse,
        )
