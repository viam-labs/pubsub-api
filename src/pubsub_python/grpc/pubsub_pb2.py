# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pubsub.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpubsub.proto\x12\x1bviamlabs.services.pubsub.v1\x1a\x1cgoogle/api/annotations.proto\"f\n\x0ePublishRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05topic\x18\x02 \x01(\tR\x05topic\x12\x18\n\x07message\x18\x03 \x01(\tR\x07message\x12\x10\n\x03qos\x18\x04 \x01(\x05R\x03qos\"-\n\x0fPublishResponse\x12\x1a\n\x08response\x18\x01 \x01(\tR\x08response\"<\n\x10SubscribeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05topic\x18\x02 \x01(\tR\x05topic\"-\n\x11SubscribeResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\">\n\x12UnsubscribeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05topic\x18\x02 \x01(\tR\x05topic\"1\n\x13UnsubscribeResponse\x12\x1a\n\x08response\x18\x01 \x01(\tR\x08response2\xc5\x03\n\rPubsubService\x12\x98\x01\n\x07Publish\x12+.viamlabs.services.pubsub.v1.PublishRequest\x1a,.viamlabs.services.pubsub.v1.PublishResponse\"2\x82\xd3\xe4\x93\x02,\"*/acme/api/v1/service/pubsub/{name}/publish\x12n\n\tSubscribe\x12-.viamlabs.services.pubsub.v1.SubscribeRequest\x1a..viamlabs.services.pubsub.v1.SubscribeResponse\"\x00\x30\x01\x12\xa8\x01\n\x0bUnsubscribe\x12/.viamlabs.services.pubsub.v1.UnsubscribeRequest\x1a\x30.viamlabs.services.pubsub.v1.UnsubscribeResponse\"6\x82\xd3\xe4\x93\x02\x30\"./acme/api/v1/service/pubsub/{name}/unsubscribeB\x0eZ\x0c./pubsub-apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pubsub_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\014./pubsub-api'
  _globals['_PUBSUBSERVICE'].methods_by_name['Publish']._options = None
  _globals['_PUBSUBSERVICE'].methods_by_name['Publish']._serialized_options = b'\202\323\344\223\002,\"*/acme/api/v1/service/pubsub/{name}/publish'
  _globals['_PUBSUBSERVICE'].methods_by_name['Unsubscribe']._options = None
  _globals['_PUBSUBSERVICE'].methods_by_name['Unsubscribe']._serialized_options = b'\202\323\344\223\0020\"./acme/api/v1/service/pubsub/{name}/unsubscribe'
  _globals['_PUBLISHREQUEST']._serialized_start=75
  _globals['_PUBLISHREQUEST']._serialized_end=177
  _globals['_PUBLISHRESPONSE']._serialized_start=179
  _globals['_PUBLISHRESPONSE']._serialized_end=224
  _globals['_SUBSCRIBEREQUEST']._serialized_start=226
  _globals['_SUBSCRIBEREQUEST']._serialized_end=286
  _globals['_SUBSCRIBERESPONSE']._serialized_start=288
  _globals['_SUBSCRIBERESPONSE']._serialized_end=333
  _globals['_UNSUBSCRIBEREQUEST']._serialized_start=335
  _globals['_UNSUBSCRIBEREQUEST']._serialized_end=397
  _globals['_UNSUBSCRIBERESPONSE']._serialized_start=399
  _globals['_UNSUBSCRIBERESPONSE']._serialized_end=448
  _globals['_PUBSUBSERVICE']._serialized_start=451
  _globals['_PUBSUBSERVICE']._serialized_end=904
# @@protoc_insertion_point(module_scope)
