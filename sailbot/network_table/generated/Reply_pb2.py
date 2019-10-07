# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Reply.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from . import GetNodesReply_pb2 as GetNodesReply__pb2
from . import SubscribeReply_pb2 as SubscribeReply__pb2
from . import ErrorReply_pb2 as ErrorReply__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Reply.proto',
  package='NetworkTable',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bReply.proto\x12\x0cNetworkTable\x1a\x13GetNodesReply.proto\x1a\x14SubscribeReply.proto\x1a\x10\x45rrorReply.proto\"\xfa\x01\n\x05Reply\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.NetworkTable.Reply.Type\x12\x33\n\x0egetnodes_reply\x18\x02 \x01(\x0b\x32\x1b.NetworkTable.GetNodesReply\x12\x35\n\x0fsubscribe_reply\x18\x03 \x01(\x0b\x32\x1c.NetworkTable.SubscribeReply\x12-\n\x0b\x65rror_reply\x18\x04 \x01(\x0b\x32\x18.NetworkTable.ErrorReply\".\n\x04Type\x12\x0c\n\x08GETNODES\x10\x00\x12\r\n\tSUBSCRIBE\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x62\x06proto3')
  ,
  dependencies=[GetNodesReply__pb2.DESCRIPTOR,SubscribeReply__pb2.DESCRIPTOR,ErrorReply__pb2.DESCRIPTOR,])



_REPLY_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='NetworkTable.Reply.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GETNODES', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIBE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=295,
  serialized_end=341,
)
_sym_db.RegisterEnumDescriptor(_REPLY_TYPE)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='NetworkTable.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='NetworkTable.Reply.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='getnodes_reply', full_name='NetworkTable.Reply.getnodes_reply', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribe_reply', full_name='NetworkTable.Reply.subscribe_reply', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_reply', full_name='NetworkTable.Reply.error_reply', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REPLY_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=341,
)

_REPLY.fields_by_name['type'].enum_type = _REPLY_TYPE
_REPLY.fields_by_name['getnodes_reply'].message_type = GetNodesReply__pb2._GETNODESREPLY
_REPLY.fields_by_name['subscribe_reply'].message_type = SubscribeReply__pb2._SUBSCRIBEREPLY
_REPLY.fields_by_name['error_reply'].message_type = ErrorReply__pb2._ERRORREPLY
_REPLY_TYPE.containing_type = _REPLY
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'Reply_pb2'
  # @@protoc_insertion_point(class_scope:NetworkTable.Reply)
  })
_sym_db.RegisterMessage(Reply)


# @@protoc_insertion_point(module_scope)
