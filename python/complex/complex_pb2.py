# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: complex.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcomplex.proto\x12\x0f\x65xample.complex\"y\n\x0e\x43omplexMessage\x12\x30\n\tone_dummy\x18\x02 \x01(\x0b\x32\x1d.example.complex.DummyMessage\x12\x35\n\x0emultiple_dummy\x18\x03 \x03(\x0b\x32\x1d.example.complex.DummyMessage\"(\n\x0c\x44ummyMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3')



_COMPLEXMESSAGE = DESCRIPTOR.message_types_by_name['ComplexMessage']
_DUMMYMESSAGE = DESCRIPTOR.message_types_by_name['DummyMessage']
ComplexMessage = _reflection.GeneratedProtocolMessageType('ComplexMessage', (_message.Message,), {
  'DESCRIPTOR' : _COMPLEXMESSAGE,
  '__module__' : 'complex_pb2'
  # @@protoc_insertion_point(class_scope:example.complex.ComplexMessage)
  })
_sym_db.RegisterMessage(ComplexMessage)

DummyMessage = _reflection.GeneratedProtocolMessageType('DummyMessage', (_message.Message,), {
  'DESCRIPTOR' : _DUMMYMESSAGE,
  '__module__' : 'complex_pb2'
  # @@protoc_insertion_point(class_scope:example.complex.DummyMessage)
  })
_sym_db.RegisterMessage(DummyMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPLEXMESSAGE._serialized_start=34
  _COMPLEXMESSAGE._serialized_end=155
  _DUMMYMESSAGE._serialized_start=157
  _DUMMYMESSAGE._serialized_end=197
# @@protoc_insertion_point(module_scope)