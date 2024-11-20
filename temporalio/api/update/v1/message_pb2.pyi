"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
The MIT License

Copyright (c) 2020 Temporal Technologies Inc.  All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import builtins
import sys

import google.protobuf.descriptor
import google.protobuf.message

import temporalio.api.common.v1.message_pb2
import temporalio.api.enums.v1.update_pb2
import temporalio.api.failure.v1.message_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class WaitPolicy(google.protobuf.message.Message):
    """Specifies client's intent to wait for Update results."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFECYCLE_STAGE_FIELD_NUMBER: builtins.int
    lifecycle_stage: temporalio.api.enums.v1.update_pb2.UpdateWorkflowExecutionLifecycleStage.ValueType
    """Indicates the Update lifecycle stage that the Update must reach before
    API call is returned.
    NOTE: This field works together with API call timeout which is limited by
    server timeout (maximum wait time). If server timeout is expired before
    user specified timeout, API call returns even if specified stage is not reached.
    """
    def __init__(
        self,
        *,
        lifecycle_stage: temporalio.api.enums.v1.update_pb2.UpdateWorkflowExecutionLifecycleStage.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["lifecycle_stage", b"lifecycle_stage"],
    ) -> None: ...

global___WaitPolicy = WaitPolicy

class UpdateRef(google.protobuf.message.Message):
    """The data needed by a client to refer to a previously invoked Workflow Update."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORKFLOW_EXECUTION_FIELD_NUMBER: builtins.int
    UPDATE_ID_FIELD_NUMBER: builtins.int
    @property
    def workflow_execution(
        self,
    ) -> temporalio.api.common.v1.message_pb2.WorkflowExecution: ...
    update_id: builtins.str
    def __init__(
        self,
        *,
        workflow_execution: temporalio.api.common.v1.message_pb2.WorkflowExecution
        | None = ...,
        update_id: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "workflow_execution", b"workflow_execution"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "update_id", b"update_id", "workflow_execution", b"workflow_execution"
        ],
    ) -> None: ...

global___UpdateRef = UpdateRef

class Outcome(google.protobuf.message.Message):
    """The outcome of a Workflow Update: success or failure."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    FAILURE_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> temporalio.api.common.v1.message_pb2.Payloads: ...
    @property
    def failure(self) -> temporalio.api.failure.v1.message_pb2.Failure: ...
    def __init__(
        self,
        *,
        success: temporalio.api.common.v1.message_pb2.Payloads | None = ...,
        failure: temporalio.api.failure.v1.message_pb2.Failure | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "failure", b"failure", "success", b"success", "value", b"value"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "failure", b"failure", "success", b"success", "value", b"value"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["value", b"value"]
    ) -> typing_extensions.Literal["success", "failure"] | None: ...

global___Outcome = Outcome

class Meta(google.protobuf.message.Message):
    """Metadata about a Workflow Update."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPDATE_ID_FIELD_NUMBER: builtins.int
    IDENTITY_FIELD_NUMBER: builtins.int
    update_id: builtins.str
    """An ID with workflow-scoped uniqueness for this Update."""
    identity: builtins.str
    """A string identifying the agent that requested this Update."""
    def __init__(
        self,
        *,
        update_id: builtins.str = ...,
        identity: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "identity", b"identity", "update_id", b"update_id"
        ],
    ) -> None: ...

global___Meta = Meta

class Input(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADER_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> temporalio.api.common.v1.message_pb2.Header:
        """Headers that are passed with the Update from the requesting entity.
        These can include things like auth or tracing tokens.
        """
    name: builtins.str
    """The name of the Update handler to invoke on the target Workflow."""
    @property
    def args(self) -> temporalio.api.common.v1.message_pb2.Payloads:
        """The arguments to pass to the named Update handler."""
    def __init__(
        self,
        *,
        header: temporalio.api.common.v1.message_pb2.Header | None = ...,
        name: builtins.str = ...,
        args: temporalio.api.common.v1.message_pb2.Payloads | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["args", b"args", "header", b"header"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "args", b"args", "header", b"header", "name", b"name"
        ],
    ) -> None: ...

global___Input = Input

class Request(google.protobuf.message.Message):
    """The client request that triggers a Workflow Update."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> global___Meta: ...
    @property
    def input(self) -> global___Input: ...
    def __init__(
        self,
        *,
        meta: global___Meta | None = ...,
        input: global___Input | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["input", b"input", "meta", b"meta"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["input", b"input", "meta", b"meta"]
    ) -> None: ...

global___Request = Request

class Rejection(google.protobuf.message.Message):
    """An Update protocol message indicating that a Workflow Update has been rejected."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REJECTED_REQUEST_MESSAGE_ID_FIELD_NUMBER: builtins.int
    REJECTED_REQUEST_SEQUENCING_EVENT_ID_FIELD_NUMBER: builtins.int
    REJECTED_REQUEST_FIELD_NUMBER: builtins.int
    FAILURE_FIELD_NUMBER: builtins.int
    rejected_request_message_id: builtins.str
    rejected_request_sequencing_event_id: builtins.int
    @property
    def rejected_request(self) -> global___Request: ...
    @property
    def failure(self) -> temporalio.api.failure.v1.message_pb2.Failure: ...
    def __init__(
        self,
        *,
        rejected_request_message_id: builtins.str = ...,
        rejected_request_sequencing_event_id: builtins.int = ...,
        rejected_request: global___Request | None = ...,
        failure: temporalio.api.failure.v1.message_pb2.Failure | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "failure", b"failure", "rejected_request", b"rejected_request"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "failure",
            b"failure",
            "rejected_request",
            b"rejected_request",
            "rejected_request_message_id",
            b"rejected_request_message_id",
            "rejected_request_sequencing_event_id",
            b"rejected_request_sequencing_event_id",
        ],
    ) -> None: ...

global___Rejection = Rejection

class Acceptance(google.protobuf.message.Message):
    """An Update protocol message indicating that a Workflow Update has
    been accepted (i.e. passed the worker-side validation phase).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCEPTED_REQUEST_MESSAGE_ID_FIELD_NUMBER: builtins.int
    ACCEPTED_REQUEST_SEQUENCING_EVENT_ID_FIELD_NUMBER: builtins.int
    ACCEPTED_REQUEST_FIELD_NUMBER: builtins.int
    accepted_request_message_id: builtins.str
    accepted_request_sequencing_event_id: builtins.int
    @property
    def accepted_request(self) -> global___Request: ...
    def __init__(
        self,
        *,
        accepted_request_message_id: builtins.str = ...,
        accepted_request_sequencing_event_id: builtins.int = ...,
        accepted_request: global___Request | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["accepted_request", b"accepted_request"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "accepted_request",
            b"accepted_request",
            "accepted_request_message_id",
            b"accepted_request_message_id",
            "accepted_request_sequencing_event_id",
            b"accepted_request_sequencing_event_id",
        ],
    ) -> None: ...

global___Acceptance = Acceptance

class Response(google.protobuf.message.Message):
    """An Update protocol message indicating that a Workflow Update has
    completed with the contained outcome.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    META_FIELD_NUMBER: builtins.int
    OUTCOME_FIELD_NUMBER: builtins.int
    @property
    def meta(self) -> global___Meta: ...
    @property
    def outcome(self) -> global___Outcome: ...
    def __init__(
        self,
        *,
        meta: global___Meta | None = ...,
        outcome: global___Outcome | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["meta", b"meta", "outcome", b"outcome"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["meta", b"meta", "outcome", b"outcome"],
    ) -> None: ...

global___Response = Response
