import grpc
import asyncio
from typing import List, Dict
import logging
from .logging_file_format import configure_logger
from .get_tls_certs import get_secret_data

logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


def create_secure_server(
        port: str, service_classes: List[Dict], server_key_file: str, server_cert_file: str, ca_cert_file: str
) -> grpc.aio.server:
    # flow for local server creation
    # server_key = open(server_key_file, 'rb').read()
    # server_cert = open(server_cert_file, 'rb').read()
    # ca_cert = open(ca_cert_file, 'rb').read()

    # flow for k8s server creation
    tls_certs = get_secret_data("default", "tls-certs")
    server_key = tls_certs.get("server-key")
    server_cert = tls_certs.get("server-cert")
    ca_cert = tls_certs.get("ca-cert")

    server_credentials = grpc.ssl_server_credentials(
        [(server_key, server_cert)], root_certificates=ca_cert,
        require_client_auth=True
    )

    server = grpc.aio.server()

    for function_class_pair in service_classes:
        add_func = function_class_pair["add_func"]
        add_class = function_class_pair["add_class"]
        add_func(add_class, server)

    server.add_secure_port(port, server_credentials)
    # server.add_insecure_port(port)

    return server


def create_insecure_server(
        port: str, service_classes: List[Dict]
) -> grpc.aio.server:

    server = grpc.aio.server()

    for function_class_pair in service_classes:
        add_func = function_class_pair["add_func"]
        add_class = function_class_pair["add_class"]
        add_func(add_class, server)

    server.add_insecure_port(port)

    return server
