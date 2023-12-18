import grpc
import asyncio
import logging
from typing import List, Dict


def create_secure_server(
        port: str, service_classes: List[Dict], server_key_file: str, server_cert_file: str, ca_cert_file: str
) -> grpc.aio.server:
    # server_key = open(server_key_file, 'rb').read()
    # server_cert = open(server_cert_file, 'rb').read()
    # ca_cert = open(ca_cert_file, 'rb').read()
    #
    # server_credentials = grpc.ssl_server_credentials(
    #     [(server_key, server_cert)], root_certificates=ca_cert,
    #     require_client_auth=True
    # )

    server = grpc.aio.server()

    for function_class_pair in service_classes:
        add_func = function_class_pair["add_func"]
        add_class = function_class_pair["add_class"]
        add_func(add_class, server)

    # server.add_secure_port(port, server_credentials)
    server.add_insecure_port(port)

    return server
