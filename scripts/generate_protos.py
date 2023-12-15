import sys
import subprocess
import photo_letariat


def generate_proto_and_replace_import(proto_directory, files_out_location, proto_file):
    # enforcement that protocol buffer generation will happen successfully
    # proto_file must end with .proto
    assert (proto_file[-6:]) == '.proto', "The provided proto_file must be of file type .proto"

    # proto_file must be contained within proto_directory
    proto_dir_path = proto_directory.split('/')
    proto_file_path = proto_file.split('/')
    for i in range(0, len(proto_dir_path)):
        assert proto_dir_path[i] == proto_file_path[i], ("The file path for the proto_directory must match that of the "
                                                         "proto_file")

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

    proto_buffer_file_name = photo_letariat.get_protocol_buffer_file_name(proto_file)
    proto_buffer_file_path = f"{files_out_location}/{proto_buffer_file_name}_pb2_grpc.py"
    print(f"replacing text in {proto_buffer_file_path}")
    photo_letariat.replace_pb2_import_statement(proto_buffer_file_path, proto_buffer_file_name+"_pb2")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_protos.py <proto_directory> <files_out_location> <proto_file>")
        sys.exit(1)

    proto_directory_arg = sys.argv[1]
    files_out_arg = sys.argv[2]
    proto_file_arg = sys.argv[3]

    generate_proto_and_replace_import(proto_directory_arg, files_out_arg, proto_file_arg)
