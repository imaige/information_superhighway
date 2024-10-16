import boto3
import base64
import json
from proto_models.face_analysis_layer_pb2 import (
    FaceRekognitionModelOutputRequest, FaceStatusReply
)
from os import getenv
from concurrent.futures import ThreadPoolExecutor
# import multiprocessing
# from multiprocessing.dummy import Pool

from src.libraries.grpc_analysis_layer_request import face_analysis_layer_request
from src.libraries.logging_file_format import configure_logger, get_log_level
import logging


logger = logging.getLogger(__name__)
log_level = get_log_level()
configure_logger(logger, level=log_level)

rekognition_client = boto3.client('rekognition', region_name="us-east-2")


# pool = Pool(10)
def send_request_in_background(project_table_name: str, photo_id: str, face_details):
    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(face_detail_process, project_table_name, photo_id, face_details)
    executor.shutdown(wait=False)  # Don’t block on shutdown.


def face_detail_process(project_table_name: str, photo_id: str, face_details):
    logger.trace(f"at start of process - face_details is: {face_details}")
    # futures = []
    face_request = FaceRekognitionModelOutputRequest(
        project_table_name=project_table_name,
        photo_id=photo_id,
        landmarks=face_details['Landmarks'],
        age_range_low=face_details['AgeRange']['Low'],
        age_range_high=face_details['AgeRange']['High'],
        smile_value=face_details['Smile']['Value'],
        smile_confidence=face_details['Smile']['Confidence'],
        eyeglasses_value=face_details['Eyeglasses']['Value'],
        eyeglasses_confidence=face_details['Eyeglasses']['Confidence'],
        sunglasses_value=face_details['Sunglasses']['Value'],
        sunglasses_confidence=face_details['Sunglasses']['Confidence'],
        gender_value=face_details['Gender']['Value'],
        gender_confidence=face_details['Gender']['Confidence'],
        beard_value=face_details['Beard']['Value'],
        beard_confidence=face_details['Beard']['Confidence'],
        mustache_value=face_details['Mustache']['Value'],
        mustache_confidence=face_details['Mustache']['Confidence'],
        eyes_open_value=face_details['EyesOpen']['Value'],
        eyes_open_confidence=face_details['EyesOpen']['Confidence'],
        mouth_open_value=face_details['MouthOpen']['Value'],
        mouth_open_confidence=face_details['MouthOpen']['Confidence'],
        emotion_happy_confidence=next(
            e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'HAPPY'
        ),
        emotion_angry_confidence=next(
            e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'ANGRY'
        ),
        emotion_disgusted_confidence=next(
            e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'DISGUSTED'
        ),
        emotion_fear_confidence=next(
            e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'FEAR'
        ),
        emotion_calm_confidence=next(
            e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'CALM'
        ),
        emotion_sad_confidence=next(
            e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'SAD'
        ),
        emotion_surprised_confidence=next(
            e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'SURPRISED'
        ),
        emotion_confused_confidence=next(
            e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'CONFUSED'
        ),
        pose_roll=face_details['Pose']['Roll'],
        pose_yaw=face_details['Pose']['Yaw'],
        pose_pitch=face_details['Pose']['Pitch'],
        quality_brightness=face_details['Quality']['Brightness'],
        quality_sharpness=face_details['Quality']['Sharpness'],
        confidence=face_details['Confidence'],
        face_occluded_value=face_details['FaceOccluded']['Value'],
        face_occluded_confidence=face_details['FaceOccluded']['Confidence'],
        eye_direction_yaw=face_details['EyeDirection']['Yaw'],
        eye_direction_pitch=face_details['EyeDirection']['Pitch'],
        eye_direction_confidence=face_details['EyeDirection']['Confidence']
    )

    # send non-IO-bound message with parsed_data
    # actually IO-bound for now - concurrent thread executor (send_request_in_background) handling IO bound issue
    try:
        face_analysis_layer_port = f'{getenv("FACE_ANALYSIS_LAYER_URL").strip()}.default.svc.cluster.local:50051'
        logger.trace(f"about to start face analysis layer request to port {face_analysis_layer_port}")
        # futures.append(pool.apply_async(face_analysis_layer_request, [face_request, face_analysis_layer_port]))
        face_analysis_layer_request(face_request, face_analysis_layer_port)
    except Exception as e:
        logger.error(f"Error occurred in gRPC face detail request: {e}")


def analyze_face(b64image: str, photo_id: str, project_table_name: str):
    logger.trace("starting analyze_face")
    # decode the base64 string to bytes for rekognition
    image_bytes = base64.b64decode(b64image)

    try:
        logger.trace("making request in analyze_face")
        response = rekognition_client.detect_faces(
            Image={'Bytes': image_bytes},
            Attributes=['ALL']
        )

        # logger.trace(f"received response from rekognition face detect request: {response}")   # commented this out to avoid polluting logs

        #  handle case where response['FaceDetails'] details is empty (no faces)
        number_of_faces = 0
        if not response['FaceDetails']:
            logger.trace("No faces found.")
            output = {
                "number_of_faces": number_of_faces,
                "bounding_boxes_from_faces_model": "[]"
            }
        else:
            # parsed_data_output = []
            bounding_boxes = []
            for face_details in response['FaceDetails']:
                logger.trace("Processing a bounding box.")
                bounding_box = {
                    'bounding_box_width': face_details['BoundingBox']['Width'],
                    'bounding_box_height': face_details['BoundingBox']['Height'],
                    'bounding_box_left': face_details['BoundingBox']['Left'],
                    'bounding_box_top': face_details['BoundingBox']['Top'],
                }
                bounding_boxes.append(bounding_box)
                number_of_faces += 1


                # start processing of additional face inputs
                # process = multiprocessing.Process(target=face_detail_process, args=(project_table_name, photo_id, face_details, ), daemon=True)
                # logger.trace(f"starting face analysis layer process for photo {photo_id}")
                # process.start()
                # do not call process.join() - run this process as a daemon without awaiting output

                # send face_request
                # face_detail_process(project_table_name, photo_id, face_details)
                send_request_in_background(project_table_name, photo_id, face_details)

                # face_request = FaceRekognitionModelOutputRequest(
                #     age_range_low=face_details['AgeRange']['Low'],
                #     age_range_high=face_details['AgeRange']['High'],
                #     smile_value=face_details['Smile']['Value'],
                #     smile_confidence=face_details['Smile']['Confidence'],
                #     eyeglasses_value=face_details['Eyeglasses']['Value'],
                #     eyeglasses_confidence=face_details['Eyeglasses']['Confidence'],
                #     sunglasses_value=face_details['Sunglasses']['Value'],
                #     sunglasses_confidence=face_details['Sunglasses']['Confidence'],
                #     gender_value=face_details['Gender']['Value'],
                #     gender_confidence=face_details['Gender']['Confidence'],
                #     beard_value=face_details['Beard']['Value'],
                #     beard_confidence=face_details['Beard']['Confidence'],
                #     mustache_value=face_details['Mustache']['Value'],
                #     mustache_confidence=face_details['Mustache']['Confidence'],
                #     eyes_open_value=face_details['EyesOpen']['Value'],
                #     eyes_open_confidence=face_details['EyesOpen']['Confidence'],
                #     mouth_open_value=face_details['MouthOpen']['Value'],
                #     mouth_open_confidence=face_details['MouthOpen']['Confidence'],
                #     emotion_happy_confidence=next(
                #         e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'HAPPY'
                #     ),
                #     emotion_angry_confidence=next(
                #         e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'ANGRY'
                #     ),
                #     emotion_disgusted_confidence=next(
                #         e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'DISGUSTED'
                #     ),
                #     emotion_fear_confidence=next(
                #         e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'FEAR'
                #     ),
                #     emotion_calm_confidence=next(
                #         e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'CALM'
                #     ),
                #     emotion_sad_confidence=next(
                #         e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'SAD'
                #     ),
                #     emotion_surprised_confidence=next(
                #         e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'SURPRISED'
                #     ),
                #     emotion_confused_confidence=next(
                #         e['Confidence'] for e in face_details['Emotions'] if e['Type'] == 'CONFUSED'
                #     ),
                #     pose_roll=face_details['Pose']['Roll'],
                #     pose_yaw=face_details['Pose']['Yaw'],
                #     pose_pitch=face_details['Pose']['Pitch'],
                #     quality_brightness=face_details['Quality']['Brightness'],
                #     quality_sharpness=face_details['Quality']['Sharpness'],
                #     confidence=face_details['Confidence'],
                #     face_occluded_value=face_details['FaceOccluded']['Value'],
                #     face_occluded_confidence=face_details['FaceOccluded']['Confidence'],
                #     eye_direction_yaw=face_details['EyeDirection']['Yaw'],
                #     eye_direction_pitch=face_details['EyeDirection']['Pitch'],
                #     eye_direction_confidence=face_details['EyeDirection']['Confidence']
                # )
                #
                # for landmark in face_details['Landmarks']:
                #     setattr(face_request, f'landmark_{landmark["Type"].lower()}_x', landmark['X'])
                #     setattr(face_request, f'landmark_{landmark["Type"].lower()}_y', landmark['Y'])
                #
                # # send non-IO-bound message with parsed_data
                # try:
                #     face_analysis_layer_port = f'{getenv("FACE_ANALYSIS_LAYER_URL")}:80'
                #     face_analysis_layer_request(face_request, face_analysis_layer_port)
                # except Exception as e:
                #     logger.error(f"Error occurred in gRPC face detail request: {e}")
                # end processing of additional face inputs

            output = {
                "number_of_faces": number_of_faces,
                "bounding_boxes_from_faces_model": json.dumps(bounding_boxes)
            }
        logger.debug(f"output is: {output}")
        return output
    except Exception as e:
        logger.error(f"Caught error processing face recognition using AWS Rekognition: {e}")

