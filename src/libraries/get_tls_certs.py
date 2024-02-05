from kubernetes import client, config
from typing import Dict, Optional
import logging
from logging_file_format import configure_logger


logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)


def get_secret_data(namespace: str, secret_name: str) -> Dict[str, str]:
    try:
        # Load Kubernetes configuration
        config.load_incluster_config()

        # Create a Kubernetes API client
        v1_api_client = client.CoreV1Api()

        # Retrieve the secret
        secret = v1_api_client.read_namespaced_secret(secret_name, namespace)

        # Access secret data
        secret_data = {
            "client-key": secret.data.get("client-key.pem", ""),
            "server-cert": secret.data.get("server-cert.pem", ""),
            "server-key": secret.data.get("server-key.pem", ""),
            "ca-cert": secret.data.get("ca-cert.pem", ""),
            "client-cert": secret.data.get("client-cert.pem", ""),
        }

        # Decode base64-encoded data
        decoded_data = {key: value.decode("utf-8") for key, value in secret_data.items()}

        return decoded_data

    except Exception as e:
        logger.info(f"Error while fetching secrets: {e}")
        raise Exception(f"Error while fetching secrets: {e}")

