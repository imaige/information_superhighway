# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import internal_api_template_service_pb2 as internal__api__template__service__pb2


class InternalApiTemplateServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InternalApiTemplateRequest = channel.unary_stream(
                '/internal_api_template_service.InternalApiTemplateService/InternalApiTemplateRequest',
                request_serializer=internal__api__template__service__pb2.TemplateRequest.SerializeToString,
                response_deserializer=internal__api__template__service__pb2.TemplateReply.FromString,
                )


class InternalApiTemplateServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InternalApiTemplateRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InternalApiTemplateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InternalApiTemplateRequest': grpc.unary_stream_rpc_method_handler(
                    servicer.InternalApiTemplateRequest,
                    request_deserializer=internal__api__template__service__pb2.TemplateRequest.FromString,
                    response_serializer=internal__api__template__service__pb2.TemplateReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'internal_api_template_service.InternalApiTemplateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InternalApiTemplateService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InternalApiTemplateRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/internal_api_template_service.InternalApiTemplateService/InternalApiTemplateRequest',
            internal__api__template__service__pb2.TemplateRequest.SerializeToString,
            internal__api__template__service__pb2.TemplateReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
