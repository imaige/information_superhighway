import sys
import subprocess
import replace_proto_imports


def generate_proto_and_replace_import(proto_directory, files_out_location, proto_file):
    command1 = [
        "python3",
        "-m",
        "grpc_tools.protoc",
        f"-I{proto_directory}",
        f"--python_out={files_out_location}",
        f"--pyi_out={files_out_location}",
        f"--grpc_python_out={files_out_location}",
        proto_file
    ]

    subprocess.run(command1)

    proto_buffer_file_name = replace_proto_imports.get_protocol_buffer_file_name(proto_file)
    proto_buffer_file_path = f"{files_out_location}/{proto_buffer_file_name}_pb2_grpc.py"
    print(f"replacing text in {proto_buffer_file_path}")
    replace_proto_imports.replace_pb2_import_statement(proto_buffer_file_path, proto_buffer_file_name+"_pb2")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_protos.py <proto_directory> <files_out_location> <proto_file>")
        sys.exit(1)

    proto_directory_arg = sys.argv[1]
    files_out_arg = sys.argv[2]
    proto_file_arg = sys.argv[3]

    generate_proto_and_replace_import(proto_directory_arg, files_out_arg, proto_file_arg)
