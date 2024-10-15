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
import socket
from contextlib import closing
from kubernetes import client, config
from os import getenv

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
    # async with grpc.aio.secure_channel(port, channel_credentials, interceptors=[interceptor]) as channel:
    async with grpc.aio.insecure_channel(port) as channel:
        stub = AnalysisLayerStub(channel)

        logger.info(f"Client making AiModelOutputRequest with data: {req}")
        try:
        #     async for response in stub.AiModelOutputRequestHandler(
        #             req
        #     ):
        #         logger.info(f"Superhighway received Analysis Layer's StatusReply with detail: {response}")
            logger.debug(f"Initiating gRPC analysis layer call for {req.photo_id} in table {req.project_table_name} to port {port}")
            logger.trace(f"Channel state before initiating call: {channel.get_state()}")
            call = stub.AiModelOutputRequestHandler(req, timeout=30)

            logger.debug(f"gRPC analysis layer call initiated for {req.photo_id} in table {req.project_table_name}")

            async for response in call:
                logger.info(f"Received analysis layer response: {response}")

                logger.debug(f"gRPC analysis layer call completed successfully for {req.photo_id}")
                return response
        except grpc.aio.AioRpcError as e:
            logger.error(f"gRPC error for {req.photo_id}: {e.code()}, {e.details()}")
        except Exception as e:
            logger.error(f"Error occurred in gRPC request for {req.photo_id}: {e}")

        # response = stub.AiModelOutputRequestHandler(req)
        # # logger.info("Client received from async generator with detail: " + response.photo_id)
        # logger.info("Client received from async generator with detail: ")
        # logger.info(response)


async def face_analysis_layer_request(req: FaceRekognitionModelOutputRequest, port: str, request_location: str = None) -> None:
    async def debug_connection(channel):
        while True:
            state = channel.get_state(try_to_connect=True)
            logger.debug(f"Channel state: {state}")
            if state == grpc.ChannelConnectivity.READY:
                logger.info("channel state is ready")
                return
            elif state in [grpc.ChannelConnectivity.TRANSIENT_FAILURE, grpc.ChannelConnectivity.SHUTDOWN]:
                logger.error(f"Failed to connect. Channel state: {state}")
                return
            await asyncio.sleep(1)

    host, port = port.split(':')
    options = [
        ('grpc.keepalive_time_ms', 10000),
        ('grpc.keepalive_timeout_ms', 5000),
        ('grpc.keepalive_permit_without_calls', True),
        ('grpc.http2.max_pings_without_data', 0),
        ('grpc.http2.min_time_between_pings_ms', 10000),
        ('grpc.http2.min_ping_interval_without_data_ms', 5000),
    ]

    # flow for running locally
    # client_key = open(f'./tls_certs/{request_location}/client-key.pem', 'rb').read()
    # client_cert = open(f'./tls_certs/{request_location}/client-cert.pem', 'rb').read()
    # ca_cert = open(f'./tls_certs/{request_location}/ca-cert.pem', 'rb').read()

    # flow for running on k8s
    # tls_certs = get_secret_data("default", "face-analysis-layer-tls-certs")
    # client_key = tls_certs.get("client-key")
    # client_cert = tls_certs.get("client-cert")
    # ca_cert = tls_certs.get("ca-cert")

    # channel_credentials = grpc.ssl_channel_credentials(
    #     root_certificates=ca_cert, private_key=client_key, certificate_chain=client_cert
    # )

    # interceptors = [LoggingClientInterceptor()]
    # interceptor = LoggingClientInterceptor()
    # with grpc.secure_channel(port, channel_credentials) as channel:
    async with grpc.aio.insecure_channel(port) as channel:
        # connection_success = await enhanced_debug_connection(channel, host, port)
        #
        # if not connection_success:
        #     logger.error("Failed to establish connection. Aborting request.")
        #     return

        # channel = grpc.intercept_channel(channel)  #, interceptor)

        if not await debug_channel_state(channel):
            logger.error("Failed to establish a READY channel")
            return

        stub = FaceAnalysisLayerStub(channel)

        logger.trace(f"Client making FaceRekognitionModelOutputRequest with data: {req}")
        try:
            logger.debug(f"Initiating gRPC face layer call for {req.photo_id} in table {req.project_table_name} to port {port}")
            # logger.trace(f"Channel state before initiating call: {channel.get_state()}")
            async for response in stub.FaceRekognitionModelOutputRequestHandler(req, timeout=30):
                logger.info(f"received response: {response}")
        except grpc.RpcError as e:
            logger.error(f"gRPC error for {req.photo_id}: {e.code()}, {e.details()}")
        except asyncio.TimeoutError:
            logger.error(f"Timeout error for {req.photo_id}")
        except Exception as e:
            logger.error(f"Error occurred in gRPC request for {req.photo_id}: {e}")


# helpers
async def enhanced_debug_connection(channel, host, port, timeout=60):
    start_time = asyncio.get_event_loop().time()
    while True:
        state = channel.get_state(try_to_connect=True)
        logger.debug(f"Channel state: {state}")

        if state == grpc.ChannelConnectivity.READY:
            logger.info("Connection established successfully")
            return True
        elif state in [grpc.ChannelConnectivity.TRANSIENT_FAILURE, grpc.ChannelConnectivity.SHUTDOWN]:
            logger.error(f"Failed to connect. Channel state: {state}")
            return False

        # Check if we've exceeded the timeout
        if asyncio.get_event_loop().time() - start_time > timeout:
            logger.error(f"Connection attempt timed out after {timeout} seconds")
            return False

        # Perform additional network checks
        try:
            with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
                sock.settimeout(5)
                result = sock.connect_ex((host, int(port)))
                if result == 0:
                    logger.debug(f"Port {port} is open on host {host}")
                else:
                    logger.warning(f"Port {port} is not accessible on host {host}")
        except Exception as e:
            logger.error(f"Error during network check: {e}")

        await asyncio.sleep(5)


async def debug_channel_state(channel, timeout=60):
    start_time = asyncio.get_event_loop().time()
    while True:
        state = channel.get_state(try_to_connect=True)
        logger.debug(f"Channel state: {state}")
        if state == grpc.ChannelConnectivity.READY:
            logger.info("Channel is READY")
            return True
        elif state in [grpc.ChannelConnectivity.TRANSIENT_FAILURE, grpc.ChannelConnectivity.SHUTDOWN]:
            logger.error(f"Channel in failure state: {state}")
            return False
        if asyncio.get_event_loop().time() - start_time > timeout:
            logger.error(f"Channel state check timed out after {timeout} seconds")
            return False
        await asyncio.sleep(1)
