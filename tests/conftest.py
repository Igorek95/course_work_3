import json
import pytest


@pytest.fixture
def temp_operations_file(tmpdir):
    data = [
        {"state": "EXECUTED", "description": "Operation 1"},
        {"state": "PENDING", "description": "Operation 2"},
        {"state": "EXECUTED", "description": "Operation 3"},
    ]
    file_path = tmpdir.join("operations.json")
    with open(file_path, "w") as file:
        json.dump(data, file)
    return file_path
