# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pubsub.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'pubsub.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpubsub.proto\x12\x06pubsub\"0\n\x0ePublishRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"!\n\x0fPublishResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"!\n\x10SubscribeRequest\x12\r\n\x05topic\x18\x01 \x01(\t\")\n\x07Message\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2\x85\x01\n\rPubSubService\x12:\n\x07Publish\x12\x16.pubsub.PublishRequest\x1a\x17.pubsub.PublishResponse\x12\x38\n\tSubscribe\x12\x18.pubsub.SubscribeRequest\x1a\x0f.pubsub.Message0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pubsub_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PUBLISHREQUEST']._serialized_start=24
  _globals['_PUBLISHREQUEST']._serialized_end=72
  _globals['_PUBLISHRESPONSE']._serialized_start=74
  _globals['_PUBLISHRESPONSE']._serialized_end=107
  _globals['_SUBSCRIBEREQUEST']._serialized_start=109
  _globals['_SUBSCRIBEREQUEST']._serialized_end=142
  _globals['_MESSAGE']._serialized_start=144
  _globals['_MESSAGE']._serialized_end=185
  _globals['_PUBSUBSERVICE']._serialized_start=188
  _globals['_PUBSUBSERVICE']._serialized_end=321
# @@protoc_insertion_point(module_scope)
