# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/operatorservice/v1/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporalio.api.operatorservice.v1 import (
    request_response_pb2 as temporal_dot_api_dot_operatorservice_dot_v1_dot_request__response__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n-temporal/api/operatorservice/v1/service.proto\x12\x1ftemporal.api.operatorservice.v1\x1a\x36temporal/api/operatorservice/v1/request_response.proto2\xd9\x0b\n\x0fOperatorService\x12\x92\x01\n\x13\x41\x64\x64SearchAttributes\x12;.temporal.api.operatorservice.v1.AddSearchAttributesRequest\x1a<.temporal.api.operatorservice.v1.AddSearchAttributesResponse"\x00\x12\x9b\x01\n\x16RemoveSearchAttributes\x12>.temporal.api.operatorservice.v1.RemoveSearchAttributesRequest\x1a?.temporal.api.operatorservice.v1.RemoveSearchAttributesResponse"\x00\x12\x95\x01\n\x14ListSearchAttributes\x12<.temporal.api.operatorservice.v1.ListSearchAttributesRequest\x1a=.temporal.api.operatorservice.v1.ListSearchAttributesResponse"\x00\x12\x86\x01\n\x0f\x44\x65leteNamespace\x12\x37.temporal.api.operatorservice.v1.DeleteNamespaceRequest\x1a\x38.temporal.api.operatorservice.v1.DeleteNamespaceResponse"\x00\x12\x9e\x01\n\x17\x44\x65leteWorkflowExecution\x12?.temporal.api.operatorservice.v1.DeleteWorkflowExecutionRequest\x1a@.temporal.api.operatorservice.v1.DeleteWorkflowExecutionResponse"\x00\x12\xa1\x01\n\x18\x41\x64\x64OrUpdateRemoteCluster\x12@.temporal.api.operatorservice.v1.AddOrUpdateRemoteClusterRequest\x1a\x41.temporal.api.operatorservice.v1.AddOrUpdateRemoteClusterResponse"\x00\x12\x92\x01\n\x13RemoveRemoteCluster\x12;.temporal.api.operatorservice.v1.RemoveRemoteClusterRequest\x1a<.temporal.api.operatorservice.v1.RemoveRemoteClusterResponse"\x00\x12\x86\x01\n\x0f\x44\x65scribeCluster\x12\x37.temporal.api.operatorservice.v1.DescribeClusterRequest\x1a\x38.temporal.api.operatorservice.v1.DescribeClusterResponse"\x00\x12}\n\x0cListClusters\x12\x34.temporal.api.operatorservice.v1.ListClustersRequest\x1a\x35.temporal.api.operatorservice.v1.ListClustersResponse"\x00\x12\x8f\x01\n\x12ListClusterMembers\x12:.temporal.api.operatorservice.v1.ListClusterMembersRequest\x1a;.temporal.api.operatorservice.v1.ListClusterMembersResponse"\x00\x42\xb2\x01\n"io.temporal.api.operatorservice.v1B\x0cServiceProtoP\x01Z5go.temporal.io/api/operatorservice/v1;operatorservice\xaa\x02\x1fTemporal.Api.OperatorService.V1\xea\x02"Temporal::Api::OperatorService::V1b\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "temporal.api.operatorservice.v1.service_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n"io.temporal.api.operatorservice.v1B\014ServiceProtoP\001Z5go.temporal.io/api/operatorservice/v1;operatorservice\252\002\037Temporal.Api.OperatorService.V1\352\002"Temporal::Api::OperatorService::V1'
    _OPERATORSERVICE._serialized_start = 139
    _OPERATORSERVICE._serialized_end = 1636
# @@protoc_insertion_point(module_scope)
