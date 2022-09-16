# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/sdk/core/bridge/bridge.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from temporal.sdk.core import (
    core_interface_pb2 as temporal_dot_sdk_dot_core_dot_core__interface__pb2,
)

from temporalio.bridge.proto.activity_task import (
    activity_task_pb2 as temporal_dot_sdk_dot_core_dot_activity__task_dot_activity__task__pb2,
)
from temporalio.bridge.proto.workflow_activation import (
    workflow_activation_pb2 as temporal_dot_sdk_dot_core_dot_workflow__activation_dot_workflow__activation__pb2,
)
from temporalio.bridge.proto.workflow_completion import (
    workflow_completion_pb2 as temporal_dot_sdk_dot_core_dot_workflow__completion_dot_workflow__completion__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n%temporal/sdk/core/bridge/bridge.proto\x12\x0e\x63oresdk.bridge\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a&temporal/sdk/core/core_interface.proto\x1a\x33temporal/sdk/core/activity_task/activity_task.proto\x1a?temporal/sdk/core/workflow_activation/workflow_activation.proto\x1a?temporal/sdk/core/workflow_completion/workflow_completion.proto"\x99\x06\n\x14InitTelemetryRequest\x12\x16\n\x0etracing_filter\x18\x01 \x01(\t\x12L\n\x07\x63onsole\x18\x02 \x01(\x0b\x32\x39.coresdk.bridge.InitTelemetryRequest.ConsoleLoggerOptionsH\x00\x12L\n\x07\x66orward\x18\x03 \x01(\x0b\x32\x39.coresdk.bridge.InitTelemetryRequest.ForwardLoggerOptionsH\x00\x12Q\n\x0cotel_tracing\x18\x04 \x01(\x0b\x32\x39.coresdk.bridge.InitTelemetryRequest.OtelCollectorOptionsH\x01\x12Q\n\x0cotel_metrics\x18\x05 \x01(\x0b\x32\x39.coresdk.bridge.InitTelemetryRequest.OtelCollectorOptionsH\x02\x12L\n\nprometheus\x18\x06 \x01(\x0b\x32\x36.coresdk.bridge.InitTelemetryRequest.PrometheusOptionsH\x02\x1a\x16\n\x14\x43onsoleLoggerOptions\x1a?\n\x14\x46orwardLoggerOptions\x12\'\n\x05level\x18\x01 \x01(\x0e\x32\x18.coresdk.bridge.LogLevel\x1a\xac\x01\n\x14OtelCollectorOptions\x12\x0b\n\x03url\x18\x01 \x01(\t\x12W\n\x07headers\x18\x02 \x03(\x0b\x32\x46.coresdk.bridge.InitTelemetryRequest.OtelCollectorOptions.HeadersEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x30\n\x11PrometheusOptions\x12\x1b\n\x13\x65xport_bind_address\x18\x01 \x01(\tB\t\n\x07loggingB\t\n\x07tracingB\t\n\x07metrics"\xbc\x05\n\x13\x43reateClientRequest\x12\x12\n\ntarget_url\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x13\n\x0b\x63lient_name\x18\x03 \x01(\t\x12\x16\n\x0e\x63lient_version\x18\x04 \x01(\t\x12\x10\n\x08identity\x18\x06 \x01(\t\x12\x41\n\ntls_config\x18\x08 \x01(\x0b\x32-.coresdk.bridge.CreateClientRequest.TlsConfig\x12\x45\n\x0cretry_config\x18\t \x01(\x0b\x32/.coresdk.bridge.CreateClientRequest.RetryConfig\x1ai\n\tTlsConfig\x12\x1b\n\x13server_root_ca_cert\x18\x01 \x01(\x0c\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x13\n\x0b\x63lient_cert\x18\x03 \x01(\x0c\x12\x1a\n\x12\x63lient_private_key\x18\x04 \x01(\x0c\x1a\xc9\x02\n\x0bRetryConfig\x12\x33\n\x10initial_interval\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12:\n\x14randomization_factor\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x30\n\nmultiplier\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\x0cmax_interval\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x33\n\x10max_elapsed_time\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x31\n\x0bmax_retries\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value"[\n\x0cInitResponse\x12\x31\n\x05\x65rror\x18\x01 \x01(\x0b\x32".coresdk.bridge.InitResponse.Error\x1a\x18\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t"\xee\x05\n\x13\x43reateWorkerRequest\x12\x12\n\ntask_queue\x18\x01 \x01(\t\x12:\n\x14max_cached_workflows\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x44\n\x1emax_outstanding_workflow_tasks\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12@\n\x1amax_outstanding_activities\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x46\n max_outstanding_local_activities\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12>\n\x18max_concurrent_wft_polls\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x43\n\x1enonsticky_to_sticky_poll_ratio\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12=\n\x17max_concurrent_at_polls\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x1c\n\x14no_remote_activities\x18\t \x01(\x08\x12I\n&sticky_queue_schedule_to_start_timeout\x18\n \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x42\n\x1fmax_heartbeat_throttle_interval\x18\x0b \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x46\n#default_heartbeat_throttle_interval\x18\x0c \x01(\x0b\x32\x19.google.protobuf.Duration"o\n\x16RegisterWorkerResponse\x12;\n\x05\x65rror\x18\x01 \x01(\x0b\x32,.coresdk.bridge.RegisterWorkerResponse.Error\x1a\x18\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t"\x1f\n\x1dPollWorkflowActivationRequest"\xe6\x01\n\x1ePollWorkflowActivationResponse\x12\x45\n\nactivation\x18\x01 \x01(\x0b\x32/.coresdk.workflow_activation.WorkflowActivationH\x00\x12\x45\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x34.coresdk.bridge.PollWorkflowActivationResponse.ErrorH\x00\x1a*\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08shutdown\x18\x02 \x01(\x08\x42\n\n\x08response"\x19\n\x17PollActivityTaskRequest"\xc8\x01\n\x18PollActivityTaskResponse\x12\x33\n\x04task\x18\x01 \x01(\x0b\x32#.coresdk.activity_task.ActivityTaskH\x00\x12?\n\x05\x65rror\x18\x02 \x01(\x0b\x32..coresdk.bridge.PollActivityTaskResponse.ErrorH\x00\x1a*\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08shutdown\x18\x02 \x01(\x08\x42\n\n\x08response"r\n!CompleteWorkflowActivationRequest\x12M\n\ncompletion\x18\x01 \x01(\x0b\x32\x39.coresdk.workflow_completion.WorkflowActivationCompletion"\x87\x01\n"CompleteWorkflowActivationResponse\x12G\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x38.coresdk.bridge.CompleteWorkflowActivationResponse.Error\x1a\x18\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t"R\n\x1b\x43ompleteActivityTaskRequest\x12\x33\n\ncompletion\x18\x01 \x01(\x0b\x32\x1f.coresdk.ActivityTaskCompletion"{\n\x1c\x43ompleteActivityTaskResponse\x12\x41\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x32.coresdk.bridge.CompleteActivityTaskResponse.Error\x1a\x18\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t"O\n\x1eRecordActivityHeartbeatRequest\x12-\n\theartbeat\x18\x01 \x01(\x0b\x32\x1a.coresdk.ActivityHeartbeat"\x81\x01\n\x1fRecordActivityHeartbeatResponse\x12\x44\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x35.coresdk.bridge.RecordActivityHeartbeatResponse.Error\x1a\x18\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t"0\n\x1eRequestWorkflowEvictionRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t"\x81\x01\n\x1fRequestWorkflowEvictionResponse\x12\x44\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x35.coresdk.bridge.RequestWorkflowEvictionResponse.Error\x1a\x18\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t"\x17\n\x15ShutdownWorkerRequest"o\n\x16ShutdownWorkerResponse\x12;\n\x05\x65rror\x18\x01 \x01(\x0b\x32,.coresdk.bridge.ShutdownWorkerResponse.Error\x1a\x18\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t"\x1a\n\x18\x46\x65tchBufferedLogsRequest"\xd5\x01\n\x19\x46\x65tchBufferedLogsResponse\x12\x43\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x32.coresdk.bridge.FetchBufferedLogsResponse.LogEntry\x1as\n\x08LogEntry\x12\x0f\n\x07message\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x05level\x18\x03 \x01(\x0e\x32\x18.coresdk.bridge.LogLevel*c\n\x08LogLevel\x12\x19\n\x15LOG_LEVEL_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x08\n\x04WARN\x10\x03\x12\x08\n\x04INFO\x10\x04\x12\t\n\x05\x44\x45\x42UG\x10\x05\x12\t\n\x05TRACE\x10\x06\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "temporal.sdk.core.bridge.bridge_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _INITTELEMETRYREQUEST_OTELCOLLECTOROPTIONS_HEADERSENTRY._options = None
    _INITTELEMETRYREQUEST_OTELCOLLECTOROPTIONS_HEADERSENTRY._serialized_options = (
        b"8\001"
    )
    _LOGLEVEL._serialized_start = 4571
    _LOGLEVEL._serialized_end = 4670
    _INITTELEMETRYREQUEST._serialized_start = 378
    _INITTELEMETRYREQUEST._serialized_end = 1171
    _INITTELEMETRYREQUEST_CONSOLELOGGEROPTIONS._serialized_start = 826
    _INITTELEMETRYREQUEST_CONSOLELOGGEROPTIONS._serialized_end = 848
    _INITTELEMETRYREQUEST_FORWARDLOGGEROPTIONS._serialized_start = 850
    _INITTELEMETRYREQUEST_FORWARDLOGGEROPTIONS._serialized_end = 913
    _INITTELEMETRYREQUEST_OTELCOLLECTOROPTIONS._serialized_start = 916
    _INITTELEMETRYREQUEST_OTELCOLLECTOROPTIONS._serialized_end = 1088
    _INITTELEMETRYREQUEST_OTELCOLLECTOROPTIONS_HEADERSENTRY._serialized_start = 1042
    _INITTELEMETRYREQUEST_OTELCOLLECTOROPTIONS_HEADERSENTRY._serialized_end = 1088
    _INITTELEMETRYREQUEST_PROMETHEUSOPTIONS._serialized_start = 1090
    _INITTELEMETRYREQUEST_PROMETHEUSOPTIONS._serialized_end = 1138
    _CREATECLIENTREQUEST._serialized_start = 1174
    _CREATECLIENTREQUEST._serialized_end = 1874
    _CREATECLIENTREQUEST_TLSCONFIG._serialized_start = 1437
    _CREATECLIENTREQUEST_TLSCONFIG._serialized_end = 1542
    _CREATECLIENTREQUEST_RETRYCONFIG._serialized_start = 1545
    _CREATECLIENTREQUEST_RETRYCONFIG._serialized_end = 1874
    _INITRESPONSE._serialized_start = 1876
    _INITRESPONSE._serialized_end = 1967
    _INITRESPONSE_ERROR._serialized_start = 1943
    _INITRESPONSE_ERROR._serialized_end = 1967
    _CREATEWORKERREQUEST._serialized_start = 1970
    _CREATEWORKERREQUEST._serialized_end = 2720
    _REGISTERWORKERRESPONSE._serialized_start = 2722
    _REGISTERWORKERRESPONSE._serialized_end = 2833
    _REGISTERWORKERRESPONSE_ERROR._serialized_start = 1943
    _REGISTERWORKERRESPONSE_ERROR._serialized_end = 1967
    _POLLWORKFLOWACTIVATIONREQUEST._serialized_start = 2835
    _POLLWORKFLOWACTIVATIONREQUEST._serialized_end = 2866
    _POLLWORKFLOWACTIVATIONRESPONSE._serialized_start = 2869
    _POLLWORKFLOWACTIVATIONRESPONSE._serialized_end = 3099
    _POLLWORKFLOWACTIVATIONRESPONSE_ERROR._serialized_start = 3045
    _POLLWORKFLOWACTIVATIONRESPONSE_ERROR._serialized_end = 3087
    _POLLACTIVITYTASKREQUEST._serialized_start = 3101
    _POLLACTIVITYTASKREQUEST._serialized_end = 3126
    _POLLACTIVITYTASKRESPONSE._serialized_start = 3129
    _POLLACTIVITYTASKRESPONSE._serialized_end = 3329
    _POLLACTIVITYTASKRESPONSE_ERROR._serialized_start = 3045
    _POLLACTIVITYTASKRESPONSE_ERROR._serialized_end = 3087
    _COMPLETEWORKFLOWACTIVATIONREQUEST._serialized_start = 3331
    _COMPLETEWORKFLOWACTIVATIONREQUEST._serialized_end = 3445
    _COMPLETEWORKFLOWACTIVATIONRESPONSE._serialized_start = 3448
    _COMPLETEWORKFLOWACTIVATIONRESPONSE._serialized_end = 3583
    _COMPLETEWORKFLOWACTIVATIONRESPONSE_ERROR._serialized_start = 1943
    _COMPLETEWORKFLOWACTIVATIONRESPONSE_ERROR._serialized_end = 1967
    _COMPLETEACTIVITYTASKREQUEST._serialized_start = 3585
    _COMPLETEACTIVITYTASKREQUEST._serialized_end = 3667
    _COMPLETEACTIVITYTASKRESPONSE._serialized_start = 3669
    _COMPLETEACTIVITYTASKRESPONSE._serialized_end = 3792
    _COMPLETEACTIVITYTASKRESPONSE_ERROR._serialized_start = 1943
    _COMPLETEACTIVITYTASKRESPONSE_ERROR._serialized_end = 1967
    _RECORDACTIVITYHEARTBEATREQUEST._serialized_start = 3794
    _RECORDACTIVITYHEARTBEATREQUEST._serialized_end = 3873
    _RECORDACTIVITYHEARTBEATRESPONSE._serialized_start = 3876
    _RECORDACTIVITYHEARTBEATRESPONSE._serialized_end = 4005
    _RECORDACTIVITYHEARTBEATRESPONSE_ERROR._serialized_start = 1943
    _RECORDACTIVITYHEARTBEATRESPONSE_ERROR._serialized_end = 1967
    _REQUESTWORKFLOWEVICTIONREQUEST._serialized_start = 4007
    _REQUESTWORKFLOWEVICTIONREQUEST._serialized_end = 4055
    _REQUESTWORKFLOWEVICTIONRESPONSE._serialized_start = 4058
    _REQUESTWORKFLOWEVICTIONRESPONSE._serialized_end = 4187
    _REQUESTWORKFLOWEVICTIONRESPONSE_ERROR._serialized_start = 1943
    _REQUESTWORKFLOWEVICTIONRESPONSE_ERROR._serialized_end = 1967
    _SHUTDOWNWORKERREQUEST._serialized_start = 4189
    _SHUTDOWNWORKERREQUEST._serialized_end = 4212
    _SHUTDOWNWORKERRESPONSE._serialized_start = 4214
    _SHUTDOWNWORKERRESPONSE._serialized_end = 4325
    _SHUTDOWNWORKERRESPONSE_ERROR._serialized_start = 1943
    _SHUTDOWNWORKERRESPONSE_ERROR._serialized_end = 1967
    _FETCHBUFFEREDLOGSREQUEST._serialized_start = 4327
    _FETCHBUFFEREDLOGSREQUEST._serialized_end = 4353
    _FETCHBUFFEREDLOGSRESPONSE._serialized_start = 4356
    _FETCHBUFFEREDLOGSRESPONSE._serialized_end = 4569
    _FETCHBUFFEREDLOGSRESPONSE_LOGENTRY._serialized_start = 4454
    _FETCHBUFFEREDLOGSRESPONSE_LOGENTRY._serialized_end = 4569
# @@protoc_insertion_point(module_scope)
