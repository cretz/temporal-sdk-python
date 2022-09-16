# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/enums/v1/workflow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n$temporal/api/enums/v1/workflow.proto\x12\x15temporal.api.enums.v1*\x8b\x02\n\x15WorkflowIdReusePolicy\x12(\n$WORKFLOW_ID_REUSE_POLICY_UNSPECIFIED\x10\x00\x12,\n(WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE\x10\x01\x12\x38\n4WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE_FAILED_ONLY\x10\x02\x12-\n)WORKFLOW_ID_REUSE_POLICY_REJECT_DUPLICATE\x10\x03\x12\x31\n-WORKFLOW_ID_REUSE_POLICY_TERMINATE_IF_RUNNING\x10\x04*\xa4\x01\n\x11ParentClosePolicy\x12#\n\x1fPARENT_CLOSE_POLICY_UNSPECIFIED\x10\x00\x12!\n\x1dPARENT_CLOSE_POLICY_TERMINATE\x10\x01\x12\x1f\n\x1bPARENT_CLOSE_POLICY_ABANDON\x10\x02\x12&\n\"PARENT_CLOSE_POLICY_REQUEST_CANCEL\x10\x03*\xbd\x01\n\x16\x43ontinueAsNewInitiator\x12)\n%CONTINUE_AS_NEW_INITIATOR_UNSPECIFIED\x10\x00\x12&\n\"CONTINUE_AS_NEW_INITIATOR_WORKFLOW\x10\x01\x12#\n\x1f\x43ONTINUE_AS_NEW_INITIATOR_RETRY\x10\x02\x12+\n'CONTINUE_AS_NEW_INITIATOR_CRON_SCHEDULE\x10\x03*\xe5\x02\n\x17WorkflowExecutionStatus\x12)\n%WORKFLOW_EXECUTION_STATUS_UNSPECIFIED\x10\x00\x12%\n!WORKFLOW_EXECUTION_STATUS_RUNNING\x10\x01\x12'\n#WORKFLOW_EXECUTION_STATUS_COMPLETED\x10\x02\x12$\n WORKFLOW_EXECUTION_STATUS_FAILED\x10\x03\x12&\n\"WORKFLOW_EXECUTION_STATUS_CANCELED\x10\x04\x12(\n$WORKFLOW_EXECUTION_STATUS_TERMINATED\x10\x05\x12.\n*WORKFLOW_EXECUTION_STATUS_CONTINUED_AS_NEW\x10\x06\x12'\n#WORKFLOW_EXECUTION_STATUS_TIMED_OUT\x10\x07*\xb5\x01\n\x14PendingActivityState\x12&\n\"PENDING_ACTIVITY_STATE_UNSPECIFIED\x10\x00\x12$\n PENDING_ACTIVITY_STATE_SCHEDULED\x10\x01\x12\"\n\x1ePENDING_ACTIVITY_STATE_STARTED\x10\x02\x12+\n'PENDING_ACTIVITY_STATE_CANCEL_REQUESTED\x10\x03*\x9b\x01\n\x18PendingWorkflowTaskState\x12+\n'PENDING_WORKFLOW_TASK_STATE_UNSPECIFIED\x10\x00\x12)\n%PENDING_WORKFLOW_TASK_STATE_SCHEDULED\x10\x01\x12'\n#PENDING_WORKFLOW_TASK_STATE_STARTED\x10\x02*\x97\x01\n\x16HistoryEventFilterType\x12)\n%HISTORY_EVENT_FILTER_TYPE_UNSPECIFIED\x10\x00\x12'\n#HISTORY_EVENT_FILTER_TYPE_ALL_EVENT\x10\x01\x12)\n%HISTORY_EVENT_FILTER_TYPE_CLOSE_EVENT\x10\x02*\x9f\x02\n\nRetryState\x12\x1b\n\x17RETRY_STATE_UNSPECIFIED\x10\x00\x12\x1b\n\x17RETRY_STATE_IN_PROGRESS\x10\x01\x12%\n!RETRY_STATE_NON_RETRYABLE_FAILURE\x10\x02\x12\x17\n\x13RETRY_STATE_TIMEOUT\x10\x03\x12(\n$RETRY_STATE_MAXIMUM_ATTEMPTS_REACHED\x10\x04\x12$\n RETRY_STATE_RETRY_POLICY_NOT_SET\x10\x05\x12%\n!RETRY_STATE_INTERNAL_SERVER_ERROR\x10\x06\x12 \n\x1cRETRY_STATE_CANCEL_REQUESTED\x10\x07*\xb0\x01\n\x0bTimeoutType\x12\x1c\n\x18TIMEOUT_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bTIMEOUT_TYPE_START_TO_CLOSE\x10\x01\x12\"\n\x1eTIMEOUT_TYPE_SCHEDULE_TO_START\x10\x02\x12\"\n\x1eTIMEOUT_TYPE_SCHEDULE_TO_CLOSE\x10\x03\x12\x1a\n\x16TIMEOUT_TYPE_HEARTBEAT\x10\x04\x42\x81\x01\n\x18io.temporal.api.enums.v1B\rWorkflowProtoP\x01Z!go.temporal.io/api/enums/v1;enums\xaa\x02\x15Temporal.Api.Enums.V1\xea\x02\x18Temporal::Api::Enums::V1b\x06proto3"
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "temporal.api.enums.v1.workflow_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\030io.temporal.api.enums.v1B\rWorkflowProtoP\001Z!go.temporal.io/api/enums/v1;enums\252\002\025Temporal.Api.Enums.V1\352\002\030Temporal::Api::Enums::V1"
    _WORKFLOWIDREUSEPOLICY._serialized_start = 64
    _WORKFLOWIDREUSEPOLICY._serialized_end = 331
    _PARENTCLOSEPOLICY._serialized_start = 334
    _PARENTCLOSEPOLICY._serialized_end = 498
    _CONTINUEASNEWINITIATOR._serialized_start = 501
    _CONTINUEASNEWINITIATOR._serialized_end = 690
    _WORKFLOWEXECUTIONSTATUS._serialized_start = 693
    _WORKFLOWEXECUTIONSTATUS._serialized_end = 1050
    _PENDINGACTIVITYSTATE._serialized_start = 1053
    _PENDINGACTIVITYSTATE._serialized_end = 1234
    _PENDINGWORKFLOWTASKSTATE._serialized_start = 1237
    _PENDINGWORKFLOWTASKSTATE._serialized_end = 1392
    _HISTORYEVENTFILTERTYPE._serialized_start = 1395
    _HISTORYEVENTFILTERTYPE._serialized_end = 1546
    _RETRYSTATE._serialized_start = 1549
    _RETRYSTATE._serialized_end = 1836
    _TIMEOUTTYPE._serialized_start = 1839
    _TIMEOUTTYPE._serialized_end = 2015
# @@protoc_insertion_point(module_scope)
