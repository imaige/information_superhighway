import grpc
from proto_models.internal_api_template_service_pb2 import (
    TemplateRequest, TemplateReply
)
from proto_models.internal_api_template_service_pb2_grpc import (
    InternalApiTemplateServiceStub
)
from ...libraries.logging_file_format import configure_logger

import asyncio
import logging


logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


async def template_request(req: TemplateRequest, port: str) -> None:
    # logging.basicConfig(level=logging.INFO)
    request_location = 'local'
    client_key = open(f'./tls_certs/{request_location}/client-key.pem', 'rb').read()
    client_cert = open(f'./tls_certs/{request_location}/client-cert.pem', 'rb').read()
    ca_cert = open(f'./tls_certs/{request_location}/ca-cert.pem', 'rb').read()

    channel_credentials = grpc.ssl_channel_credentials(
        root_certificates=ca_cert, private_key=client_key, certificate_chain=client_cert
    )

    # async with grpc.aio.secure_channel(port, channel_credentials) as channel:
    async with grpc.aio.insecure_channel(port) as channel:
        stub = InternalApiTemplateServiceStub(channel)

        
        logger.info(f"Client making InternalApiTemplateRequest with data: {req}")
        async for response in stub.InternalApiTemplateRequest(req):
            logger.info("Client received from async generator: " + response.message)
