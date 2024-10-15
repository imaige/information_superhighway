# for this to work, the port must be forwarded to localhost:
# kubectl port-forward face-analysis-layer-service-deployment-565f6f7d6-vcs4s 50051:50051
# and the required proto outputs (3 files) must be moved to the libraries folder so they can be directly imported from

import grpc
# from proto_models.internal_api_template_service_pb2 import (
#     TemplateRequest, TemplateReply
# )
# from proto_models.internal_api_template_service_pb2_grpc import (
#     InternalApiTemplateServiceStub
# )
# from proto_models.analysis_layer_pb2 import (
#     AiModelOutputRequest,
# )
# from proto_models.analysis_layer_pb2_grpc import (
#     AnalysisLayerStub
# )
from .face_analysis_layer_pb2 import (
    FaceRekognitionModelOutputRequest
)
from .face_analysis_layer_pb2_grpc import (
    FaceAnalysisLayerStub
)
import asyncio
from os import getenv
import uuid
from .logging_file_format import configure_logger, get_log_level
# from get_tls_certs import get_secret_data

import logging


logger = logging.getLogger(__name__)
log_level = get_log_level()
configure_logger(logger, level=log_level)


async def face_analysis_layer_request() -> None:
    logger.trace("starting face_analysis_layer_request")
    port = f'face-analysis-layer-service-service:50051'
    face_details = {
        'BoundingBox': {'Width': 0.17027755081653595, 'Height': 0.11831283569335938, 'Left': 0.4174186587333679,
                        'Top': 0.2626023292541504}, 'AgeRange': {'Low': 19, 'High': 25},
        'Smile': {'Value': True, 'Confidence': 97.13677978515625},
        'Eyeglasses': {'Value': False, 'Confidence': 99.9803237915039},
        'Sunglasses': {'Value': False, 'Confidence': 99.99630737304688},
        'Gender': {'Value': 'Female', 'Confidence': 99.99918365478516},
        'Beard': {'Value': False, 'Confidence': 91.74179077148438},
        'Mustache': {'Value': False, 'Confidence': 99.6590347290039},
        'EyesOpen': {'Value': False, 'Confidence': 59.419803619384766},
        'MouthOpen': {'Value': False, 'Confidence': 88.30379486083984},
        'Emotions': [{'Type': 'HAPPY', 'Confidence': 99.0234375}, {'Type': 'CALM', 'Confidence': 0.23956298828125},
                     {'Type': 'SURPRISED', 'Confidence': 0.03412365913391113},
                     {'Type': 'DISGUSTED', 'Confidence': 0.00432133674621582},
                     {'Type': 'CONFUSED', 'Confidence': 0.0009834766387939453},
                     {'Type': 'SAD', 'Confidence': 8.940696716308594e-05},
                     {'Type': 'FEAR', 'Confidence': 7.152557373046875e-05},
                     {'Type': 'ANGRY', 'Confidence': 4.76837158203125e-05}],
        'Landmarks': [{'Type': 'eyeLeft', 'X': 0.4611765742301941, 'Y': 0.3104584515094757},
                      {'Type': 'eyeRight', 'X': 0.5366387963294983, 'Y': 0.30644065141677856},
                      {'Type': 'mouthLeft', 'X': 0.4775228500366211, 'Y': 0.3528870940208435},
                      {'Type': 'mouthRight', 'X': 0.540298342704773, 'Y': 0.34943410754203796},
                      {'Type': 'nose', 'X': 0.5087320804595947, 'Y': 0.3279687762260437},
                      {'Type': 'leftEyeBrowLeft', 'X': 0.4294799566268921, 'Y': 0.3030875325202942},
                      {'Type': 'leftEyeBrowRight', 'X': 0.4756956398487091, 'Y': 0.29572632908821106},
                      {'Type': 'leftEyeBrowUp', 'X': 0.452496737241745, 'Y': 0.2952297031879425},
                      {'Type': 'rightEyeBrowLeft', 'X': 0.5189370512962341, 'Y': 0.2934180796146393},
                      {'Type': 'rightEyeBrowRight', 'X': 0.5605810284614563, 'Y': 0.296085923910141},
                      {'Type': 'rightEyeBrowUp', 'X': 0.5395485758781433, 'Y': 0.29059046506881714},
                      {'Type': 'leftEyeLeft', 'X': 0.4471389353275299, 'Y': 0.3113935589790344},
                      {'Type': 'leftEyeRight', 'X': 0.47619351744651794, 'Y': 0.3100340962409973},
                      {'Type': 'leftEyeUp', 'X': 0.46069034934043884, 'Y': 0.30813881754875183},
                      {'Type': 'leftEyeDown', 'X': 0.4620046615600586, 'Y': 0.312297523021698},
                      {'Type': 'rightEyeLeft', 'X': 0.5217661261558533, 'Y': 0.3076187074184418},
                      {'Type': 'rightEyeRight', 'X': 0.5493234992027283, 'Y': 0.30591318011283875},
                      {'Type': 'rightEyeUp', 'X': 0.5364397168159485, 'Y': 0.30409345030784607},
                      {'Type': 'rightEyeDown', 'X': 0.5366811752319336, 'Y': 0.308287650346756},
                      {'Type': 'noseLeft', 'X': 0.4927545189857483, 'Y': 0.3353423774242401},
                      {'Type': 'noseRight', 'X': 0.5206311345100403, 'Y': 0.3338131308555603},
                      {'Type': 'mouthUp', 'X': 0.5094218254089355, 'Y': 0.3444114625453949},
                      {'Type': 'mouthDown', 'X': 0.5117443799972534, 'Y': 0.3577006161212921},
                      {'Type': 'leftPupil', 'X': 0.4611765742301941, 'Y': 0.3104584515094757},
                      {'Type': 'rightPupil', 'X': 0.5366387963294983, 'Y': 0.30644065141677856},
                      {'Type': 'upperJawlineLeft', 'X': 0.4099637269973755, 'Y': 0.31831100583076477},
                      {'Type': 'midJawlineLeft', 'X': 0.4366522431373596, 'Y': 0.3630276322364807},
                      {'Type': 'chinBottom', 'X': 0.5147101283073425, 'Y': 0.38116762042045593},
                      {'Type': 'midJawlineRight', 'X': 0.5701245069503784, 'Y': 0.3558181822299957},
                      {'Type': 'upperJawlineRight', 'X': 0.5745360851287842, 'Y': 0.3095261752605438}],
        'Pose': {'Roll': -9.068370819091797, 'Yaw': -0.013449691236019135, 'Pitch': 8.68962287902832},
        'Quality': {'Brightness': 91.12591552734375, 'Sharpness': 9.912903785705566}, 'Confidence': 99.99006652832031,
        'FaceOccluded': {'Value': True, 'Confidence': 99.95866394042969},
        'EyeDirection': {'Yaw': -8.403111457824707, 'Pitch': -35.83302307128906, 'Confidence': 99.62862396240234}}
    project_table_name = "1_a85eeccf-1de7-47fd-a668-7e78270d4457_photos"
    photo_id = "47aeae7e-89f8-48e0-9d33-5d8e02edd02a"
    logger.info("creating face_request")
    req = FaceRekognitionModelOutputRequest(
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
        # channel = grpc.intercept_channel(channel)  #, interceptor)
        stub = FaceAnalysisLayerStub(channel)

        logger.trace(f"Client making FaceRekognitionModelOutputRequest with data: {req}")
        try:
            logger.debug(f"Initiating gRPC face layer call for {req.photo_id} in table {req.project_table_name}")
            # logger.trace(f"Channel state before initiating call: {channel.get_state()}")
            async for response in stub.FaceRekognitionModelOutputRequestHandler(req, timeout=30):
                logger.info(f"received response: {response}")

            # logger.debug(f"gRPC face layer call initiated for {req.photo_id} in table {req.project_table_name} to port {port}")

            # logger.info(f"call output: {call}")

            # for response in call:
            #     logger.info(f"Received face layer response: {response.message}")
            #
            #     logger.debug(f"gRPC face layer call completed successfully for {req.photo_id}")
            #     return response
        except grpc.RpcError as e:
            logger.error(f"gRPC error for {req.photo_id}: {e.code()}, {e.details()}")
        except Exception as e:
            logger.error(f"Error occurred in gRPC request for {req.photo_id}: {e}")
