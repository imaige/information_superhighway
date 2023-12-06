import sys
import subprocess


def generate_proto(proto_directory, files_out_location, proto_file):
    command = [
        "python3",
        "-m",
        "grpc_tools.protoc",
        f"-I{proto_directory}",
        f"--python_out={files_out_location}",
        f"--pyi_out={files_out_location}",
        f"--grpc_python_out={files_out_location}",
        proto_file
    ]

    subprocess.run(command)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_protos.py <proto_directory> <files_out_location> <proto_file>")
        sys.exit(1)

    proto_directory_arg = sys.argv[1]
    files_out_arg = sys.argv[2]
    proto_file_arg = sys.argv[3]

    generate_proto(proto_directory_arg, files_out_arg, proto_file_arg)
