from grpc_interceptor import ClientInterceptor, ClientCallDetails
from grpc.aio import (
    UnaryUnaryClientInterceptor,
    UnaryStreamClientInterceptor,
    StreamUnaryClientInterceptor,
    StreamStreamClientInterceptor
)
import asyncio
import logging

from .logging_file_format import configure_logger, get_log_level

logger = logging.getLogger(__name__)
log_level = get_log_level()
configure_logger(logger, level=log_level)


class LoggingClientInterceptor(UnaryStreamClientInterceptor):
    async def intercept_unary_stream(self, continuation, client_call_details, request):
        # method = client_call_details.method
        # timeout = client_call_details.timeout
        # metadata = client_call_details.metadata
        # logger.info(f"Request Method: {method}")
        # logger.info(f"Request Timeout: {timeout}")
        # logger.info(f"Request Metadata: {metadata}")

        logger.info(f"Request: {request}")
        logger.info(f"Details: {client_call_details}")
        metadata = {metadatum.key: metadatum.value for metadatum in client_call_details.metadata}
        logger.info(f"Metadata: {metadata}")

        try:
            call = await continuation(client_call_details, request)
            logger.info(f"Call: {call.__dict__}")

            # logger.info("Response stream started")
            # async for response in call:
            #     logger.info(f"Response: {response}")
            # logger.info("Response stream ended")

            return call
        except Exception as e:
            logger.error(f"Exception from gRPC client interceptor for request with id: {request.photo_id} and model_name: {request.model_name}: {e}")

    # The next 3 methods should not get used (as we are using a unary_stream channel)
    # async def intercept_unary_unary(self, continuation, client_call_details, request):
    #     logger.info("interecept_unary_unary called")
    #     self.log_request(client_call_details, request)
    #     response = await continuation(client_call_details, request)
    #     self.log_response(response)
    #     return response
    #
    # async def intercept_stream_unary(self, continuation, client_call_details, request_iterator):
    #     logger.info("interecept_stream_unary called")
    #     self.log_request(client_call_details, request_iterator)
    #     response = await continuation(client_call_details, request_iterator)
    #     self.log_response(response)
    #     return response
    #
    # async def intercept_stream_stream(self, continuation, client_call_details, request_iterator):
    #     logger.info("interecept_stream_stream called")
    #     self.log_request(client_call_details, request_iterator)
    #     response = await continuation(client_call_details, request_iterator)
    #     async for resp in response:
    #         self.log_response(resp)
    #     return response
    #
    # def log_request(self, client_call_details, request):
    #     logger.info("log_request called")
    #     method = client_call_details.method
    #     timeout = client_call_details.timeout
    #     metadata = client_call_details.metadata
    #     logger.info(f"Request Method: {method}")
    #     logger.info(f"Request Timeout: {timeout}")
    #     logger.info(f"Request Metadata: {metadata}")
    #     logger.info(f"Request: {request}")
    #
    # def log_response(self, response):
    #     logger.info("log_response called")
    #     logger.info(f"Response: {response}")