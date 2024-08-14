import io

from kubernetes import client, config
from typing import Dict, Optional
import base64
import logging
from .logging_file_format import configure_logger, get_log_level


logger = logging.getLogger(__name__)
log_level = get_log_level()
configure_logger(logger, level=log_level)


def get_secret_data(namespace: str, secret_name: str) -> Dict[str, bytes]:
    logger.info("Getting secret data in get_tls_certs")
    try:
        # Load Kubernetes configuration
        config.load_incluster_config()

        # Create a Kubernetes API client
        v1_api_client = client.CoreV1Api()

        # Retrieve the secret
        secret = v1_api_client.read_namespaced_secret(secret_name, namespace)

        # Access secret data
        secret_data = {
            "server-cert": (base64.b64decode(secret.data.get("server-cert.pem", b""))),
            "server-key": (base64.b64decode(secret.data.get("server-key.pem", b""))),
            "ca-cert": (base64.b64decode(secret.data.get("ca-cert.pem", b""))),
            "client-cert": (base64.b64decode(secret.data.get("client-cert.pem", b""))),
            "client-key": (base64.b64decode(secret.data.get("client-key.pem", b""))),
        }

        return secret_data

    except Exception as e:
        logger.info(f"Error while fetching secrets: {e}")
        raise Exception(f"Error while fetching secrets: {e}")


def get_secret_files(namespace: str, secret_name: str) -> Dict[str, bytes]:
    logger.info("Getting secret data in get_tls_certs")
    try:
        # Load Kubernetes configuration
        config.load_incluster_config()

        # Create a Kubernetes API client
        v1_api_client = client.CoreV1Api()

        # Retrieve the secret
        secret = v1_api_client.read_namespaced_secret(secret_name, namespace)

        logger.info(f"secret is: {secret}")

        # Access secret data
        secret_data = {
            "server-cert": io.BytesIO(base64.b64decode(secret.data.get("server-cert.pem"))),
            "server-key": secret.data.get("server-key.pem"),
            "ca-cert": secret.data.get("ca-cert.pem"),
            "client-cert": secret.data.get("client-cert.pem"),
            "client-key": secret.data.get("client-key.pem"),
        }

        return secret_data

    except Exception as e:
        logger.info(f"Error while fetching secrets: {e}")
        raise Exception(f"Error while fetching secrets: {e}")
