# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/polymer/list/list.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n bilibili/polymer/list/list.proto\x12\x15\x62ilibili.polymer.list\"#\n\x11\x43heckAccountReply\x12\x0e\n\x06is_new\x18\x01 \x01(\x08\"/\n\x0f\x43heckAccountReq\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0f\n\x07periods\x18\x02 \x01(\t\":\n\x0f\x46\x61voriteTabItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"I\n\x10\x46\x61voriteTabReply\x12\x35\n\x05items\x18\x01 \x03(\x0b\x32&.bilibili.polymer.list.FavoriteTabItem\"\x10\n\x0e\x46\x61voriteTabReq2\xc7\x01\n\x04List\x12]\n\x0b\x46\x61voriteTab\x12%.bilibili.polymer.list.FavoriteTabReq\x1a\'.bilibili.polymer.list.FavoriteTabReply\x12`\n\x0c\x43heckAccount\x12&.bilibili.polymer.list.CheckAccountReq\x1a(.bilibili.polymer.list.CheckAccountReplyb\x06proto3')



_CHECKACCOUNTREPLY = DESCRIPTOR.message_types_by_name['CheckAccountReply']
_CHECKACCOUNTREQ = DESCRIPTOR.message_types_by_name['CheckAccountReq']
_FAVORITETABITEM = DESCRIPTOR.message_types_by_name['FavoriteTabItem']
_FAVORITETABREPLY = DESCRIPTOR.message_types_by_name['FavoriteTabReply']
_FAVORITETABREQ = DESCRIPTOR.message_types_by_name['FavoriteTabReq']
CheckAccountReply = _reflection.GeneratedProtocolMessageType('CheckAccountReply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKACCOUNTREPLY,
  '__module__' : 'bilibili.polymer.list.list_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.polymer.list.CheckAccountReply)
  })
_sym_db.RegisterMessage(CheckAccountReply)

CheckAccountReq = _reflection.GeneratedProtocolMessageType('CheckAccountReq', (_message.Message,), {
  'DESCRIPTOR' : _CHECKACCOUNTREQ,
  '__module__' : 'bilibili.polymer.list.list_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.polymer.list.CheckAccountReq)
  })
_sym_db.RegisterMessage(CheckAccountReq)

FavoriteTabItem = _reflection.GeneratedProtocolMessageType('FavoriteTabItem', (_message.Message,), {
  'DESCRIPTOR' : _FAVORITETABITEM,
  '__module__' : 'bilibili.polymer.list.list_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.polymer.list.FavoriteTabItem)
  })
_sym_db.RegisterMessage(FavoriteTabItem)

FavoriteTabReply = _reflection.GeneratedProtocolMessageType('FavoriteTabReply', (_message.Message,), {
  'DESCRIPTOR' : _FAVORITETABREPLY,
  '__module__' : 'bilibili.polymer.list.list_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.polymer.list.FavoriteTabReply)
  })
_sym_db.RegisterMessage(FavoriteTabReply)

FavoriteTabReq = _reflection.GeneratedProtocolMessageType('FavoriteTabReq', (_message.Message,), {
  'DESCRIPTOR' : _FAVORITETABREQ,
  '__module__' : 'bilibili.polymer.list.list_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.polymer.list.FavoriteTabReq)
  })
_sym_db.RegisterMessage(FavoriteTabReq)

_LIST = DESCRIPTOR.services_by_name['List']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHECKACCOUNTREPLY._serialized_start=59
  _CHECKACCOUNTREPLY._serialized_end=94
  _CHECKACCOUNTREQ._serialized_start=96
  _CHECKACCOUNTREQ._serialized_end=143
  _FAVORITETABITEM._serialized_start=145
  _FAVORITETABITEM._serialized_end=203
  _FAVORITETABREPLY._serialized_start=205
  _FAVORITETABREPLY._serialized_end=278
  _FAVORITETABREQ._serialized_start=280
  _FAVORITETABREQ._serialized_end=296
  _LIST._serialized_start=299
  _LIST._serialized_end=498
# @@protoc_insertion_point(module_scope)