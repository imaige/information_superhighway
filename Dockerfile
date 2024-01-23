FROM python:3.11.7-alpine

WORKDIR .

COPY . .

# the following two line are required to install grpc
# see https://github.com/grpc/grpc/issues/26971 and https://github.com/grpc/grpc/issues/24556
RUN apk add g++
RUN apk add build-base linux-headers

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 50052

CMD ["python", "main.py"]
