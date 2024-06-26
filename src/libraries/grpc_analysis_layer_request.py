import grpc
from proto_models.internal_api_template_service_pb2 import (
    TemplateRequest, TemplateReply
)
from proto_models.internal_api_template_service_pb2_grpc import (
    InternalApiTemplateServiceStub
)
from proto_models.analysis_layer_pb2 import (
    AiModelOutputRequest,
)
from proto_models.analysis_layer_pb2_grpc import (
    AnalysisLayerStub
)
from .logging_file_format import configure_logger
from .get_tls_certs import get_secret_data

import asyncio
import logging


logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


async def analysis_layer_request(req: AiModelOutputRequest, port: str, request_location: str = None) -> None:
    # flow for running locally
    # client_key = open(f'./tls_certs/{request_location}/client-key.pem', 'rb').read()
    # client_cert = open(f'./tls_certs/{request_location}/client-cert.pem', 'rb').read()
    # ca_cert = open(f'./tls_certs/{request_location}/ca-cert.pem', 'rb').read()

    # flow for running on k8s
    tls_certs = get_secret_data("default", "analysis-layer-tls-certs")
    client_key = tls_certs.get("client-key")
    client_cert = tls_certs.get("client-cert")
    ca_cert = tls_certs.get("ca-cert")

    channel_credentials = grpc.ssl_channel_credentials(
        root_certificates=ca_cert, private_key=client_key, certificate_chain=client_cert
    )

    async with grpc.aio.secure_channel(port, channel_credentials) as channel:
    # async with grpc.aio.insecure_channel(port) as channel:
        stub = AnalysisLayerStub(channel)

        logger.info(f"Client making AiModelOutputRequest with data: {req}")
        try:
        #     async for response in stub.AiModelOutputRequestHandler(
        #             req
        #     ):
        #         logger.info(f"Superhighway received Analysis Layer's StatusReply with detail: {response}")
            logger.info(f"Initiating gRPC call for {req.photo_id}")
            logger.info(f"Channel state before initiating call: {channel.get_state()}")
            call = stub.AiModelOutputRequestHandler(req, timeout=30)
            logger.info(f"gRPC call initiated for {req.photo_id}")

            async for response in call:
                logger.info(f"Received response: {response}")

                logger.info(f"gRPC call completed successfully for {req.photo_id}")
                return response
        except grpc.aio.AioRpcError as e:
            logger.error(f"gRPC error: {e.code()}, {e.details()}")
        except Exception as e:
            logger.error(f"Error occurred in gRPC request: {e}")

        # response = stub.AiModelOutputRequestHandler(req)
        # # logger.info("Client received from async generator with detail: " + response.photo_id)
        # logger.info("Client received from async generator with detail: ")
        # logger.info(response)
