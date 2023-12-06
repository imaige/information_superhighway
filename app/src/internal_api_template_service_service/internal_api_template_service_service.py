import grpc
from proto_models import TemplateReply
from proto_models import InternalApiTemplateServiceServicer, add_InternalApiTemplateServiceServicer_to_server

import asyncio
import logging


# Service Class Definition #
class TemplateRequester(InternalApiTemplateServiceServicer):
    async def InternalApiTemplateRequest(self, request, context) -> TemplateReply:
        logging.info("Serving request %s", request)
        yield TemplateReply(message=f"Hello, {request.name}!")


async def serve() -> None:
    # server_key = open('../tls_certs/server-key.pem', 'rb').read()
    # server_cert = open('../tls_certs/server-cert.pem', 'rb').read()
    # ca_cert = open('../tls_certs/ca-cert.pem', 'rb').read()
    #
    # server_credentials = grpc.ssl_server_credentials(
    #     [(server_key, server_cert)], root_certificates=ca_cert,
    #     require_client_auth=True
    # )

    server = grpc.aio.server()
    add_InternalApiTemplateServiceServicer_to_server(TemplateRequester(), server)
    listen_addr = "localhost:50051"
    # server.add_secure_port(listen_addr, server_credentials)
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    print("Server started. Listening on port 50051...")
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
