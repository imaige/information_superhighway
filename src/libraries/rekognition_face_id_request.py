import boto3
import base64

from src.libraries.logging_file_format import configure_logger
import logging


logger = logging.getLogger(__name__)
configure_logger(logger, level=logging.INFO)

rekognition_client = boto3.client('rekognition')


def analyze_face(b64image: str):
    logger.info("starting analyze_face")
    # decode the base64 string to bytes for rekognition
    image_bytes = base64.b64decode(b64image)

    logger.info("making request in analyze_face")
    response = rekognition_client.detect_faces(
        Image={'Bytes': image_bytes},
        Attributes=['ALL']
    )

    logger.info(f"response in analyze_face is: {response}")

    for faceDetail in response['FaceDetails']:
        logger.info(f"Confidence: {faceDetail['Confidence']:.2f}%")
        logger.info("BoundingBox:")
        logger.info(f"  Top: {faceDetail['BoundingBox']['Top']:.2f}")
        logger.info(f"  Left: {faceDetail['BoundingBox']['Left']:.2f}")
        logger.info(f"  Width: {faceDetail['BoundingBox']['Width']:.2f}")
        logger.info(f"  Height: {faceDetail['BoundingBox']['Height']:.2f}")

        logger.info("Emotions:")
        for emotion in faceDetail['Emotions']:
            logger.info(f"  Type: {emotion['Type']}, Confidence: {emotion['Confidence']:.2f}%")

        logger.info("Gender:")
        logger.info(f"  Value: {faceDetail['Gender']['Value']}, Confidence: {faceDetail['Gender']['Confidence']:.2f}%")

        logger.info("Age Range:")
        logger.info(f"  Low: {faceDetail['AgeRange']['Low']}, High: {faceDetail['AgeRange']['High']}")

    return response
