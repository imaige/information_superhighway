# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import image_comparison_outputs_pb2 as image__comparison__outputs__pb2


class ImageComparisonOutputServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ImageComparisonOutputRequest = channel.unary_unary(
                '/ImageComparisonOutputService/ImageComparisonOutputRequest',
                request_serializer=image__comparison__outputs__pb2.ImageComparisonOutput.SerializeToString,
                response_deserializer=image__comparison__outputs__pb2.StatusResponse.FromString,
                )


class ImageComparisonOutputServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ImageComparisonOutputRequest(self, request, context):
        """Basic request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageComparisonOutputServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ImageComparisonOutputRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.ImageComparisonOutputRequest,
                    request_deserializer=image__comparison__outputs__pb2.ImageComparisonOutput.FromString,
                    response_serializer=image__comparison__outputs__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImageComparisonOutputService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageComparisonOutputService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ImageComparisonOutputRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImageComparisonOutputService/ImageComparisonOutputRequest',
            image__comparison__outputs__pb2.ImageComparisonOutput.SerializeToString,
            image__comparison__outputs__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
