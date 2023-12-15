import re


def get_protocol_buffer_file_name(input_string):
    # Define the pattern for capturing text after the last slash
    pattern = r'[^/]+/?$'

    # Use regular expressions to find the match
    match = re.search(pattern, input_string)

    if match:
        # Extract the matched text
        result = match.group(0)
        # remove '.proto' extension
        result = result[:-6]
        return result
    else:
        # If no match is found, return the original string
        return input_string


def replace_pb2_import_statement(file_path, file_name):
    # Read the content of the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Define the import statement to be replaced
    import_statement_to_replace = f'import {file_name} as {file_name.replace("_", "__")}'
    print(f'import_statement_to_replace is {import_statement_to_replace}')

    # Replace the import statement in the content
    modified_content = file_content.replace(import_statement_to_replace,
    f'from . import {file_name} as {file_name.replace("_", "__")}')

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

    # Example usage:
    # input_file_path = 'path/to/your/file.py'
    # replace_import_statements(input_file_path)
