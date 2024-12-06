from os import getenv
from concurrent.futures import ThreadPoolExecutor
from proto_models.image_classification_analysis_layer_pb2 import (
    ImageClassificationModelOutputRequest
)
from src.libraries.grpc_analysis_layer_request import image_classification_analysis_layer_request
from src.libraries.logging_file_format import configure_logger, get_log_level
import logging


logger = logging.getLogger(__name__)
log_level = get_log_level()
configure_logger(logger, level=log_level)


def send_image_classification_analysis_request_in_background(project_table_name: str, photo_id: int, image_classification_output):
    logger.trace("starting send request in background in library file")
    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(image_classification_output_process, project_table_name, photo_id, image_classification_output)
    executor.shutdown(wait=False)  # Don’t block on shutdown.


def image_classification_output_process(project_table_name: str, photo_id: int, image_classification_raw_output):
    logger.trace("starting image_classification_output_process in library file")
    image_classification_request = ImageClassificationModelOutputRequest(
        project_table_name=project_table_name,
        photo_id=photo_id,
        labels_from_classifications_model={image_classification_raw_output}
    )
    try:
        image_classification_analysis_layer_port = f'{getenv("IMAGE_CLASSIFICATION_ANALYSIS_LAYER_URL").strip()}.default.svc.cluster.local:50051'
        logger.trace(f"about to start image classification analysis layer request to port {image_classification_analysis_layer_port}")
        image_classification_analysis_layer_request(
            image_classification_request, image_classification_analysis_layer_port
        )
    except Exception as e:
        logger.error(f"Error occurred in gRPC face detail request: {e}")
