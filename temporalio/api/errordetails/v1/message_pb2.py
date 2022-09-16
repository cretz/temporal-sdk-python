# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/errordetails/v1/message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporalio.api.common.v1 import (
    message_pb2 as temporal_dot_api_dot_common_dot_v1_dot_message__pb2,
)
from temporalio.api.enums.v1 import (
    failed_cause_pb2 as temporal_dot_api_dot_enums_dot_v1_dot_failed__cause__pb2,
)
from temporalio.api.enums.v1 import (
    namespace_pb2 as temporal_dot_api_dot_enums_dot_v1_dot_namespace__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n*temporal/api/errordetails/v1/message.proto\x12\x1ctemporal.api.errordetails.v1\x1a$temporal/api/common/v1/message.proto\x1a(temporal/api/enums/v1/failed_cause.proto\x1a%temporal/api/enums/v1/namespace.proto"B\n\x0fNotFoundFailure\x12\x17\n\x0f\x63urrent_cluster\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63tive_cluster\x18\x02 \x01(\t"R\n&WorkflowExecutionAlreadyStartedFailure\x12\x18\n\x10start_request_id\x18\x01 \x01(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\t"_\n\x19NamespaceNotActiveFailure\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x17\n\x0f\x63urrent_cluster\x18\x02 \x01(\t\x12\x16\n\x0e\x61\x63tive_cluster\x18\x03 \x01(\t"\xa6\x01\n\x1cNamespaceInvalidStateFailure\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x34\n\x05state\x18\x02 \x01(\x0e\x32%.temporal.api.enums.v1.NamespaceState\x12=\n\x0e\x61llowed_states\x18\x03 \x03(\x0e\x32%.temporal.api.enums.v1.NamespaceState"-\n\x18NamespaceNotFoundFailure\x12\x11\n\tnamespace\x18\x01 \x01(\t"\x1f\n\x1dNamespaceAlreadyExistsFailure"k\n ClientVersionNotSupportedFailure\x12\x16\n\x0e\x63lient_version\x18\x01 \x01(\t\x12\x13\n\x0b\x63lient_name\x18\x02 \x01(\t\x12\x1a\n\x12supported_versions\x18\x03 \x01(\t"d\n ServerVersionNotSupportedFailure\x12\x16\n\x0eserver_version\x18\x01 \x01(\t\x12(\n client_supported_server_versions\x18\x02 \x01(\t"%\n#CancellationAlreadyRequestedFailure"\x14\n\x12QueryFailedFailure")\n\x17PermissionDeniedFailure\x12\x0e\n\x06reason\x18\x01 \x01(\t"X\n\x18ResourceExhaustedFailure\x12<\n\x05\x63\x61use\x18\x01 \x01(\x0e\x32-.temporal.api.enums.v1.ResourceExhaustedCause"v\n\x15SystemWorkflowFailure\x12\x45\n\x12workflow_execution\x18\x01 \x01(\x0b\x32).temporal.api.common.v1.WorkflowExecution\x12\x16\n\x0eworkflow_error\x18\x02 \x01(\t"\x19\n\x17WorkflowNotReadyFailureB\xa3\x01\n\x1fio.temporal.api.errordetails.v1B\x0cMessageProtoP\x01Z/go.temporal.io/api/errordetails/v1;errordetails\xaa\x02\x1cTemporal.Api.ErrorDetails.V1\xea\x02\x1fTemporal::Api::ErrorDetails::V1b\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "temporal.api.errordetails.v1.message_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\037io.temporal.api.errordetails.v1B\014MessageProtoP\001Z/go.temporal.io/api/errordetails/v1;errordetails\252\002\034Temporal.Api.ErrorDetails.V1\352\002\037Temporal::Api::ErrorDetails::V1"
    _NOTFOUNDFAILURE._serialized_start = 195
    _NOTFOUNDFAILURE._serialized_end = 261
    _WORKFLOWEXECUTIONALREADYSTARTEDFAILURE._serialized_start = 263
    _WORKFLOWEXECUTIONALREADYSTARTEDFAILURE._serialized_end = 345
    _NAMESPACENOTACTIVEFAILURE._serialized_start = 347
    _NAMESPACENOTACTIVEFAILURE._serialized_end = 442
    _NAMESPACEINVALIDSTATEFAILURE._serialized_start = 445
    _NAMESPACEINVALIDSTATEFAILURE._serialized_end = 611
    _NAMESPACENOTFOUNDFAILURE._serialized_start = 613
    _NAMESPACENOTFOUNDFAILURE._serialized_end = 658
    _NAMESPACEALREADYEXISTSFAILURE._serialized_start = 660
    _NAMESPACEALREADYEXISTSFAILURE._serialized_end = 691
    _CLIENTVERSIONNOTSUPPORTEDFAILURE._serialized_start = 693
    _CLIENTVERSIONNOTSUPPORTEDFAILURE._serialized_end = 800
    _SERVERVERSIONNOTSUPPORTEDFAILURE._serialized_start = 802
    _SERVERVERSIONNOTSUPPORTEDFAILURE._serialized_end = 902
    _CANCELLATIONALREADYREQUESTEDFAILURE._serialized_start = 904
    _CANCELLATIONALREADYREQUESTEDFAILURE._serialized_end = 941
    _QUERYFAILEDFAILURE._serialized_start = 943
    _QUERYFAILEDFAILURE._serialized_end = 963
    _PERMISSIONDENIEDFAILURE._serialized_start = 965
    _PERMISSIONDENIEDFAILURE._serialized_end = 1006
    _RESOURCEEXHAUSTEDFAILURE._serialized_start = 1008
    _RESOURCEEXHAUSTEDFAILURE._serialized_end = 1096
    _SYSTEMWORKFLOWFAILURE._serialized_start = 1098
    _SYSTEMWORKFLOWFAILURE._serialized_end = 1216
    _WORKFLOWNOTREADYFAILURE._serialized_start = 1218
    _WORKFLOWNOTREADYFAILURE._serialized_end = 1243
# @@protoc_insertion_point(module_scope)
