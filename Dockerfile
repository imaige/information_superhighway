FROM python:3.9.10

WORKDIR .

COPY . .

# the following two line are required to install grpc
# see https://github.com/grpc/grpc/issues/26971 and https://github.com/grpc/grpc/issues/24556
#RUN apk add g++
#RUN apk add build-base linux-headers

RUN apt-get update
RUN apt-get install -y g++ make
RUN apt-get install -y musl-dev
RUN apt-get install -y libffi-dev
RUN apt-get install -y build-essential

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 50051

CMD ["python", "main.py"]