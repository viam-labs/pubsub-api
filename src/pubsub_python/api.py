"""
This file outlines the general structure for the API around a custom, modularized service.

It defines the abstract class definition that all concrete implementations must follow,
the gRPC service that will handle calls to the service,
and the gRPC client that will be able to make calls to this service.

In this example, the ``Pubsub`` abstract class defines what functionality is required for all Pubsub services.
It extends ``ServiceBase``, as all service types must.
It also defines its specific ``SUBTYPE``, which is used internally to keep track of supported types.

The ``PubsubRPCService`` implements the gRPC service for the Pubsub service. This will allow other robots and clients to make
requests of the Pubsub service. It extends both from ``PubsubServiceBase`` and ``RPCServiceBase``.
The former is the gRPC service as defined by the proto, and the latter is the class that all gRPC services must inherit from.

Finally, the ``PubsubClient`` is the gRPC client for a Pubsub service. It inherits from PubsubService since it implements
 all the same functions. The implementations are simply gRPC calls to some remote Pubsub service.

To see how this custom modular service is registered, see the __init__.py file.
To see the custom implementation of this service, see the mqtt-grpc.py file.
"""

import abc
from typing import Callable, Final, Sequence

from grpclib.client import Channel
from grpclib.server import Stream

from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.resource.types import RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_base import ServiceBase

from ..proto.pubsub_grpc import PubsubServiceBase, PubsubServiceStub

# update the below with actual methods for your API!
from ..proto.pubsub_pb2 import PublishRequest, PublishResponse, SubscribeRequest, SubscribeResponse, UnsubscribeRequest, UnsubscribeResponse


class Pubsub(ServiceBase):

    SUBTYPE: Final = Subtype("viam-labs", RESOURCE_TYPE_SERVICE, "pubsub")

    @abc.abstractmethod
    async def publish(self, topic: str, message: str, qos: int) -> str:
        ...
    
    @abc.abstractmethod
    async def subscribe(self, topic: str, callback: Callable[[str], None]): 
        ...

    @abc.abstractmethod
    async def unsubscribe(self, topic: str) -> str:
        ...

class PubsubRPCService(PubsubServiceBase, ResourceRPCServiceBase):

    RESOURCE_TYPE = Pubsub

    async def Publish(self, stream: Stream[PublishRequest, PublishResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        resp = await service.publish(request.topic, request.message, request.qos)
        await stream.send_message(PublishResponse(response=resp))

    async def Subscribe(self, stream: Stream[SubscribeRequest, SubscribeResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        while resp := await service.subscribe(request.topic, request.message, request.qos):
            await stream.send_message(SubscribeResponse(message=resp))

    async def Unsubscribe(self, stream: Stream[UnsubscribeRequest, UnsubscribeResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        service = self.get_resource(name)
        resp = await service.unsubscribe(request.topic)
        await stream.send_message(UnsubscribeResponse(response=resp))

class PubsubClient(Pubsub):

    def __init__(self, name: str, channel: Channel) -> None:
        self.channel = channel
        self.client = PubsubServiceStub(channel)
        super().__init__(name)

    async def publish(self, topic: str, message: str, qos: int) -> str:
        request = PublishRequest(name=self.name, topic=topic, message=message, qos=qos)
        response: PublishResponse = await self.client.Publish(request)
        return response.response

    async def subscribe(self, topic: str, callback: Callable[[str], None]):
        request = SubscribeRequest(name=self.name, topic=topic)
        for response in await self.client.Subscribe(request):
            callback(response.message)
     
    async def unsubscribe(self, topic: str) -> str:
        request = UnsubscribeRequest(name=self.name, topic=topic)
        response: UnsubscribeResponse = await self.client.Unsubscribe(request)
        return response.response