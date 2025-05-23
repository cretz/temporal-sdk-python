# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/enums/v1/batch_operation.proto
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n+temporal/api/enums/v1/batch_operation.proto\x12\x15temporal.api.enums.v1*\x94\x02\n\x12\x42\x61tchOperationType\x12$\n BATCH_OPERATION_TYPE_UNSPECIFIED\x10\x00\x12"\n\x1e\x42\x41TCH_OPERATION_TYPE_TERMINATE\x10\x01\x12\x1f\n\x1b\x42\x41TCH_OPERATION_TYPE_CANCEL\x10\x02\x12\x1f\n\x1b\x42\x41TCH_OPERATION_TYPE_SIGNAL\x10\x03\x12\x1f\n\x1b\x42\x41TCH_OPERATION_TYPE_DELETE\x10\x04\x12\x1e\n\x1a\x42\x41TCH_OPERATION_TYPE_RESET\x10\x05\x12\x31\n-BATCH_OPERATION_TYPE_UPDATE_EXECUTION_OPTIONS\x10\x06*\xa6\x01\n\x13\x42\x61tchOperationState\x12%\n!BATCH_OPERATION_STATE_UNSPECIFIED\x10\x00\x12!\n\x1d\x42\x41TCH_OPERATION_STATE_RUNNING\x10\x01\x12#\n\x1f\x42\x41TCH_OPERATION_STATE_COMPLETED\x10\x02\x12 \n\x1c\x42\x41TCH_OPERATION_STATE_FAILED\x10\x03\x42\x8b\x01\n\x18io.temporal.api.enums.v1B\x13\x42\x61tchOperationProtoP\x01Z!go.temporal.io/api/enums/v1;enums\xaa\x02\x17Temporalio.Api.Enums.V1\xea\x02\x1aTemporalio::Api::Enums::V1b\x06proto3'
)

_BATCHOPERATIONTYPE = DESCRIPTOR.enum_types_by_name["BatchOperationType"]
BatchOperationType = enum_type_wrapper.EnumTypeWrapper(_BATCHOPERATIONTYPE)
_BATCHOPERATIONSTATE = DESCRIPTOR.enum_types_by_name["BatchOperationState"]
BatchOperationState = enum_type_wrapper.EnumTypeWrapper(_BATCHOPERATIONSTATE)
BATCH_OPERATION_TYPE_UNSPECIFIED = 0
BATCH_OPERATION_TYPE_TERMINATE = 1
BATCH_OPERATION_TYPE_CANCEL = 2
BATCH_OPERATION_TYPE_SIGNAL = 3
BATCH_OPERATION_TYPE_DELETE = 4
BATCH_OPERATION_TYPE_RESET = 5
BATCH_OPERATION_TYPE_UPDATE_EXECUTION_OPTIONS = 6
BATCH_OPERATION_STATE_UNSPECIFIED = 0
BATCH_OPERATION_STATE_RUNNING = 1
BATCH_OPERATION_STATE_COMPLETED = 2
BATCH_OPERATION_STATE_FAILED = 3


if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\030io.temporal.api.enums.v1B\023BatchOperationProtoP\001Z!go.temporal.io/api/enums/v1;enums\252\002\027Temporalio.Api.Enums.V1\352\002\032Temporalio::Api::Enums::V1"
    _BATCHOPERATIONTYPE._serialized_start = 71
    _BATCHOPERATIONTYPE._serialized_end = 347
    _BATCHOPERATIONSTATE._serialized_start = 350
    _BATCHOPERATIONSTATE._serialized_end = 516
# @@protoc_insertion_point(module_scope)
