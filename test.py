import pytest
import os


# to run tests, from the root (where this file is located), run python -m pytest
def run_tests():
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Use pytest to discover and run tests
    exit_code = pytest.main([current_directory])

    # Return the exit code to indicate success or failure
    return exit_code

if __name__ == "__main__":
    # Run the tests when the script is executed
    exit_code = run_tests()

    # Exit with the test result code
    exit(exit_code)
