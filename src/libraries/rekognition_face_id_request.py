import boto3
import base64

rekognition_client = boto3.client('rekognition')


def analyze_face(b64image: str):
    # decode the base64 string to bytes for rekognition
    image_bytes = base64.b64decode(b64image)

    response = rekognition_client.detect_faces(
        Image={'Bytes': image_bytes},
        Attributes=['ALL']
    )

    for faceDetail in response['FaceDetails']:
        print(f"Confidence: {faceDetail['Confidence']:.2f}%")
        print("BoundingBox:")
        print(f"  Top: {faceDetail['BoundingBox']['Top']:.2f}")
        print(f"  Left: {faceDetail['BoundingBox']['Left']:.2f}")
        print(f"  Width: {faceDetail['BoundingBox']['Width']:.2f}")
        print(f"  Height: {faceDetail['BoundingBox']['Height']:.2f}")

        print("Emotions:")
        for emotion in faceDetail['Emotions']:
            print(f"  Type: {emotion['Type']}, Confidence: {emotion['Confidence']:.2f}%")

        print("Gender:")
        print(f"  Value: {faceDetail['Gender']['Value']}, Confidence: {faceDetail['Gender']['Confidence']:.2f}%")

        print("Age Range:")
        print(f"  Low: {faceDetail['AgeRange']['Low']}, High: {faceDetail['AgeRange']['High']}")

    return response
