# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analysis_layer.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61nalysis_layer.proto\x12\x18information_superhighway\"\xc3\x03\n\x14\x41iModelOutputRequest\x12\x10\n\x08photo_id\x18\x01 \x01(\t\x12\x1a\n\x12project_table_name\x18\x02 \x01(\t\x12\x1f\n\x17image_comparison_run_id\x18\x03 \x01(\t\x12\x1d\n\x15image_comparison_name\x18\x04 \x01(\t\x12!\n\x19image_comparison_datatype\x18\x05 \x01(\t\x12\x1e\n\x16image_comparison_shape\x18\x06 \x01(\x05\x12\x14\n\x0c\x61verage_hash\x18\x07 \x01(\x0c\x12\x17\n\x0fperceptual_hash\x18\x08 \x01(\x0c\x12\x17\n\x0f\x64ifference_hash\x18\t \x01(\x0c\x12\x19\n\x11wavelet_hash_haar\x18\n \x01(\x0c\x12\x12\n\ncolor_hash\x18\x0b \x01(\x0c\x12\x16\n\x0e\x63olor_averages\x18\x0c \x01(\t\x12\'\n\x1f\x62ounding_boxes_from_faces_model\x18\r \x01(\t\x12\x17\n\x0fnumber_of_faces\x18\x0e \x01(\x05\x12)\n!labels_from_classifications_model\x18\x0f \x03(\x0c\"3\n\x0bStatusReply\x12\x10\n\x08photo_id\x18\x01 \x01(\x03\x12\x12\n\nmodel_name\x18\x02 \x01(\t2\x87\x01\n\rAnalysisLayer\x12v\n\x1b\x41iModelOutputRequestHandler\x12..information_superhighway.AiModelOutputRequest\x1a%.information_superhighway.StatusReply0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analysis_layer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_AIMODELOUTPUTREQUEST']._serialized_start=51
  _globals['_AIMODELOUTPUTREQUEST']._serialized_end=502
  _globals['_STATUSREPLY']._serialized_start=504
  _globals['_STATUSREPLY']._serialized_end=555
  _globals['_ANALYSISLAYER']._serialized_start=558
  _globals['_ANALYSISLAYER']._serialized_end=693
# @@protoc_insertion_point(module_scope)
