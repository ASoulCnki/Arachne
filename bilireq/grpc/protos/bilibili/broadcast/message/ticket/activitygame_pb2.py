# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/broadcast/message/ticket/activitygame.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4bilibili/broadcast/message/ticket/activitygame.proto\x12!bilibili.broadcast.message.ticket\"e\n\tRoomEvent\x12\x42\n\x0broom_status\x18\x01 \x01(\x0e\x32-.bilibili.broadcast.message.ticket.RoomStatus\x12\x14\n\x0croom_message\x18\x02 \x01(\t**\n\nRoomStatus\x12\t\n\x05Pause\x10\x00\x12\x08\n\x04Play\x10\x01\x12\x07\n\x03\x45nd\x10\x02\x62\x06proto3')

_ROOMSTATUS = DESCRIPTOR.enum_types_by_name['RoomStatus']
RoomStatus = enum_type_wrapper.EnumTypeWrapper(_ROOMSTATUS)
Pause = 0
Play = 1
End = 2


_ROOMEVENT = DESCRIPTOR.message_types_by_name['RoomEvent']
RoomEvent = _reflection.GeneratedProtocolMessageType('RoomEvent', (_message.Message,), {
  'DESCRIPTOR' : _ROOMEVENT,
  '__module__' : 'bilibili.broadcast.message.ticket.activitygame_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.broadcast.message.ticket.RoomEvent)
  })
_sym_db.RegisterMessage(RoomEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROOMSTATUS._serialized_start=194
  _ROOMSTATUS._serialized_end=236
  _ROOMEVENT._serialized_start=91
  _ROOMEVENT._serialized_end=192
# @@protoc_insertion_point(module_scope)
