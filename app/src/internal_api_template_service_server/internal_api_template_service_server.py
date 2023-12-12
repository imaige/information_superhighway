from proto_models.internal_api_template_service_pb2 import (
    TemplateReply
)
from proto_models.internal_api_template_service_pb2_grpc import (
    InternalApiTemplateServiceServicer, add_InternalApiTemplateServiceServicer_to_server
)
from ...libraries.grpc_server_factory import create_secure_server
from ...libraries.logging_file_format import configure_logger

import asyncio
import logging


logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


# Service Class Definition #
class TemplateRequester(InternalApiTemplateServiceServicer):
    # Endpoint definition #
    # Matches name in InternalApiTemplateServiceServicer
    async def InternalApiTemplateRequest(self, request, context) -> TemplateReply:
        logger.info(f"Serving request with detail: {request}")
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
