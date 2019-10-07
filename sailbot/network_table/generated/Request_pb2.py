# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import SetValuesRequest_pb2 as SetValuesRequest__pb2
from . import GetNodesRequest_pb2 as GetNodesRequest__pb2
from . import SubscribeRequest_pb2 as SubscribeRequest__pb2
from . import UnsubscribeRequest_pb2 as UnsubscribeRequest__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Request.proto',
  package='NetworkTable',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rRequest.proto\x12\x0cNetworkTable\x1a\x16SetValuesRequest.proto\x1a\x15GetNodesRequest.proto\x1a\x16SubscribeRequest.proto\x1a\x18UnsubscribeRequest.proto\"\xe6\x02\n\x07Request\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.NetworkTable.Request.Type\x12\x39\n\x11setvalues_request\x18\x02 \x01(\x0b\x32\x1e.NetworkTable.SetValuesRequest\x12\x37\n\x10getnodes_request\x18\x03 \x01(\x0b\x32\x1d.NetworkTable.GetNodesRequest\x12\x39\n\x11subscribe_request\x18\x04 \x01(\x0b\x32\x1e.NetworkTable.SubscribeRequest\x12=\n\x13unsubscribe_request\x18\x05 \x01(\x0b\x32 .NetworkTable.UnsubscribeRequest\"C\n\x04Type\x12\r\n\tSETVALUES\x10\x00\x12\x0c\n\x08GETNODES\x10\x01\x12\r\n\tSUBSCRIBE\x10\x02\x12\x0f\n\x0bUNSUBSCRIBE\x10\x03\x62\x06proto3')
  ,
  dependencies=[SetValuesRequest__pb2.DESCRIPTOR,GetNodesRequest__pb2.DESCRIPTOR,SubscribeRequest__pb2.DESCRIPTOR,UnsubscribeRequest__pb2.DESCRIPTOR,])



_REQUEST_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='NetworkTable.Request.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SETVALUES', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GETNODES', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIBE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUBSCRIBE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=420,
  serialized_end=487,
)
_sym_db.RegisterEnumDescriptor(_REQUEST_TYPE)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='NetworkTable.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='NetworkTable.Request.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setvalues_request', full_name='NetworkTable.Request.setvalues_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='getnodes_request', full_name='NetworkTable.Request.getnodes_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribe_request', full_name='NetworkTable.Request.subscribe_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unsubscribe_request', full_name='NetworkTable.Request.unsubscribe_request', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUEST_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=487,
)

_REQUEST.fields_by_name['type'].enum_type = _REQUEST_TYPE
_REQUEST.fields_by_name['setvalues_request'].message_type = SetValuesRequest__pb2._SETVALUESREQUEST
_REQUEST.fields_by_name['getnodes_request'].message_type = GetNodesRequest__pb2._GETNODESREQUEST
_REQUEST.fields_by_name['subscribe_request'].message_type = SubscribeRequest__pb2._SUBSCRIBEREQUEST
_REQUEST.fields_by_name['unsubscribe_request'].message_type = UnsubscribeRequest__pb2._UNSUBSCRIBEREQUEST
_REQUEST_TYPE.containing_type = _REQUEST
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'Request_pb2'
  # @@protoc_insertion_point(class_scope:NetworkTable.Request)
  })
_sym_db.RegisterMessage(Request)


# @@protoc_insertion_point(module_scope)
