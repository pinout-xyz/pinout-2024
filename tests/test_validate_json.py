import glob
import json

import pytest
from jsonschema import validate

from schema import board


@pytest.mark.parametrize('board_file', glob.glob("boards/*.json"))
def test_validate_board_json_schema(board_file):
    validate(instance=json.load(open(board_file, "r")), schema=board)
