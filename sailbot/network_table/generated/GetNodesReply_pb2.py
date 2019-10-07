# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetNodesReply.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Node_pb2 as Node__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='GetNodesReply.proto',
  package='NetworkTable',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13GetNodesReply.proto\x12\x0cNetworkTable\x1a\nNode.proto\"\x88\x01\n\rGetNodesReply\x12\x35\n\x05nodes\x18\x01 \x03(\x0b\x32&.NetworkTable.GetNodesReply.NodesEntry\x1a@\n\nNodesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.NetworkTable.Node:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[Node__pb2.DESCRIPTOR,])




_GETNODESREPLY_NODESENTRY = _descriptor.Descriptor(
  name='NodesEntry',
  full_name='NetworkTable.GetNodesReply.NodesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='NetworkTable.GetNodesReply.NodesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='NetworkTable.GetNodesReply.NodesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=186,
)

_GETNODESREPLY = _descriptor.Descriptor(
  name='GetNodesReply',
  full_name='NetworkTable.GetNodesReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='NetworkTable.GetNodesReply.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETNODESREPLY_NODESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=186,
)

_GETNODESREPLY_NODESENTRY.fields_by_name['value'].message_type = Node__pb2._NODE
_GETNODESREPLY_NODESENTRY.containing_type = _GETNODESREPLY
_GETNODESREPLY.fields_by_name['nodes'].message_type = _GETNODESREPLY_NODESENTRY
DESCRIPTOR.message_types_by_name['GetNodesReply'] = _GETNODESREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetNodesReply = _reflection.GeneratedProtocolMessageType('GetNodesReply', (_message.Message,), {

  'NodesEntry' : _reflection.GeneratedProtocolMessageType('NodesEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETNODESREPLY_NODESENTRY,
    '__module__' : 'GetNodesReply_pb2'
    # @@protoc_insertion_point(class_scope:NetworkTable.GetNodesReply.NodesEntry)
    })
  ,
  'DESCRIPTOR' : _GETNODESREPLY,
  '__module__' : 'GetNodesReply_pb2'
  # @@protoc_insertion_point(class_scope:NetworkTable.GetNodesReply)
  })
_sym_db.RegisterMessage(GetNodesReply)
_sym_db.RegisterMessage(GetNodesReply.NodesEntry)


_GETNODESREPLY_NODESENTRY._options = None
# @@protoc_insertion_point(module_scope)
