"""
This file registers the model with the Python SDK.
"""

from viam.resource.registry import Registry, ResourceRegistration

from .api import PubsubClient, PubsubRPCService, Pubsub

Registry.register_subtype(ResourceRegistration(Pubsub, PubsubRPCService, lambda name, channel: PubsubClient(name, channel)))
