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
from proto_models.face_analysis_layer_pb2 import (
    FaceRekognitionModelOutputRequest, FaceStatusReply
)
from proto_models.face_analysis_layer_pb2_grpc import (
    FaceAnalysisLayerStub
)
from .logging_file_format import configure_logger, get_log_level
from .get_tls_certs import get_secret_data
from .grpc_client_request_interceptor import LoggingClientInterceptor

import asyncio
import logging


logger = logging.getLogger(__name__)
log_level = get_log_level()
configure_logger(logger, level=log_level)


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

    # interceptors = [LoggingClientInterceptor()]
    interceptor = LoggingClientInterceptor()
    async with grpc.aio.secure_channel(port, channel_credentials, interceptors=[interceptor]) as channel:
    # async with grpc.aio.insecure_channel(port) as channel:
        stub = AnalysisLayerStub(channel)

        logger.info(f"Client making AiModelOutputRequest with data: {req}")
        try:
        #     async for response in stub.AiModelOutputRequestHandler(
        #             req
        #     ):
        #         logger.info(f"Superhighway received Analysis Layer's StatusReply with detail: {response}")
            logger.info(f"Initiating gRPC analysis layer call for {req.photo_id} in table {req.project_table_name}")
            logger.trace(f"Channel state before initiating call: {channel.get_state()}")
            call = stub.AiModelOutputRequestHandler(req, timeout=30)

            logger.trace(f"gRPC call initiated for {req.photo_id} in table {req.project_table_name}")

            async for response in call:
                logger.info(f"Received response: {response}")

                logger.trace(f"gRPC call completed successfully for {req.photo_id}")
                return response
        except grpc.aio.AioRpcError as e:
            logger.error(f"gRPC error for {req.photo_id}: {e.code()}, {e.details()}")
        except Exception as e:
            logger.error(f"Error occurred in gRPC request for {req.photo_id}: {e}")

        # response = stub.AiModelOutputRequestHandler(req)
        # # logger.info("Client received from async generator with detail: " + response.photo_id)
        # logger.info("Client received from async generator with detail: ")
        # logger.info(response)


def face_analysis_layer_request(req: FaceRekognitionModelOutputRequest, port: str, request_location: str = None) -> None:
    # flow for running locally
    # client_key = open(f'./tls_certs/{request_location}/client-key.pem', 'rb').read()
    # client_cert = open(f'./tls_certs/{request_location}/client-cert.pem', 'rb').read()
    # ca_cert = open(f'./tls_certs/{request_location}/ca-cert.pem', 'rb').read()

    # flow for running on k8s
    tls_certs = get_secret_data("default", "face-analysis-layer-tls-certs")
    client_key = tls_certs.get("client-key")
    client_cert = tls_certs.get("client-cert")
    ca_cert = tls_certs.get("ca-cert")

    channel_credentials = grpc.ssl_channel_credentials(
        root_certificates=ca_cert, private_key=client_key, certificate_chain=client_cert
    )

    # interceptors = [LoggingClientInterceptor()]
    # interceptor = LoggingClientInterceptor()
    # with grpc.secure_channel(port, channel_credentials) as channel:
    with grpc.insecure_channel(port) as channel:
        # channel = grpc.intercept_channel(channel)  #, interceptor)
        stub = FaceAnalysisLayerStub(channel)

        logger.trace(f"Client making FaceRekognitionModelOutputRequest with data: {req}")
        try:
            logger.info(f"Initiating gRPC face layer call for {req.photo_id} in table {req.project_table_name}")
            # logger.trace(f"Channel state before initiating call: {channel.get_state()}")
            call = stub.FaceRekognitionModelOutputRequestHandler(req, timeout=30)

            logger.trace(f"gRPC call initiated for {req.photo_id} in table {req.project_table_name}")

            for response in call:
                logger.info(f"Received response: {response.message}")

                logger.trace(f"gRPC call completed successfully for {req.photo_id}")
                return response
        except grpc.RpcError as e:
            logger.error(f"gRPC error for {req.photo_id}: {e.code()}, {e.details()}")
        except Exception as e:
            logger.error(f"Error occurred in gRPC request for {req.photo_id}: {e}")
