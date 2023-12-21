import grpc

from proto_models.internal_api_template_service_pb2 import (
    TemplateRequest, TemplateReply
)
from proto_models.internal_api_template_service_pb2_grpc import (
    InternalApiTemplateServiceServicer, add_InternalApiTemplateServiceServicer_to_server
)
from ...libraries.grpc_server_factory import create_secure_server
from ...libraries.logging_file_format import configure_logger

import grpc
import asyncio
import logging
from google.rpc import status_pb2, code_pb2, error_details_pb2
from google.protobuf import any_pb2


logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


# Service Class Definition #
class TemplateRequester(InternalApiTemplateServiceServicer):
    # Endpoint definition #
    # Matches name in InternalApiTemplateServiceServicer
    async def InternalApiTemplateRequest(
            self, request: TemplateRequest, context: grpc.ServicerContext
    ) -> TemplateReply | status_pb2.Status:
        logger.info(f"Serving request with detail: {request}")
        logger.info(f"request type is {type(request)}")
        # Example error handling
        # in this case, for using a protocol buffer that is not the designated one
        # IMO, Python does not enforce the 'same protocol buffer' requirement as stringently as it should
        # so it would be good practice to enforce this on our end using simple logic like the below
        if not isinstance(request, TemplateRequest):
            logger.info(f"Failure in method call")
            code = grpc.StatusCode.INVALID_ARGUMENT
            details = any_pb2.Any()
            # to access details for a particular error, use response[$index].details[0].value.decode('utf-8')
            # as details is passed as a list and the value parameter is passed as a protobuf-serialized string
            details.Pack(
                error_details_pb2.DebugInfo(
                    detail="Invalid argument: request must use TemplateRequest protocol buffer."
                )
            )
            message = "Invalid argument error."
            context.set_code(code)
            context.set_details(message)
            yield status_pb2.Status(
                code=code_pb2.INVALID_ARGUMENT,
                message=message,
                details=[details]
            )
        # send response (optional, but recommended)
        yield TemplateReply(message=f"Hello, {request.name}!")


# Server Creation #
async def serve() -> None:
    server_key = '../tls_certs/server-key.pem'
    server_cert = '../tls_certs/server-cert.pem'
    ca_cert = '../tls_certs/ca-cert.pem'
    port = "localhost:50051"
    service_classes = [
        {
            "add_func": add_InternalApiTemplateServiceServicer_to_server,
            "add_class": TemplateRequester()
        }
    ]

    server = create_secure_server(port, service_classes, server_key, server_cert, ca_cert)

    logger.info("Starting server on %s", port)
    await server.start()
    logger.info(f"Server started. Listening on port {port}...")
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
