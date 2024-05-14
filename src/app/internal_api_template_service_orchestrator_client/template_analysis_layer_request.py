import grpc
from proto_models.internal_api_template_service_pb2 import (
    TemplateRequest, TemplateReply
)
from proto_models.internal_api_template_service_pb2_grpc import (
    InternalApiTemplateServiceStub
)
from proto_models.analysis_layer_pb2 import (
    AiModelOutputRequest, StatusReply
)
from proto_models.analysis_layer_pb2_grpc import (
    AnalysisLayerStub
)
from ...libraries.logging_file_format import configure_logger
from ...libraries.get_tls_certs import get_secret_data

import asyncio
import logging


logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


async def template_analysis_layer_request(req: AiModelOutputRequest, port: str, request_location: str) -> None:
    # flow for running locally
    print(f"file source: ./tls_certs/{request_location}/client-key.pem")
    client_key = open(f'./tls_certs/{request_location}/client-key.pem', 'rb').read()
    client_cert = open(f'./tls_certs/{request_location}/client-cert.pem', 'rb').read()
    ca_cert = open(f'./tls_certs/{request_location}/ca-cert.pem', 'rb').read()

    # flow for running on k8s
    # tls_certs = get_secret_data("default", "tls-certs")
    # client_key = tls_certs.get("client-key")
    # client_cert = tls_certs.get("client-cert")
    # ca_cert = tls_certs.get("ca-cert")

    channel_credentials = grpc.ssl_channel_credentials(
        root_certificates=ca_cert, private_key=client_key, certificate_chain=client_cert
    )

    async with grpc.aio.secure_channel(port, channel_credentials) as channel:
    # async with grpc.aio.insecure_channel(port) as channel:
        stub = AnalysisLayerStub(channel)

        logger.info(f"Client making AiModelOutputRequest with data: {req}")
        async for response in stub.AiModelOutputRequestHandler(req):
            # logger.info("Client received from async generator with detail: " + response.photo_id)
            logger.info("Client received from async generator with detail: ")
            logger.info(response)
