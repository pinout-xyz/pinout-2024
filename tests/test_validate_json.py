import glob
import json

import pytest
from jsonschema import validate

from schema.board import board
from schema.chip import chip


@pytest.mark.parametrize("board_file", glob.glob("boards/*.json"))
def test_validate_board_json_schema(board_file):
    validate(instance=json.load(open(board_file, "r")), schema=board)


@pytest.mark.parametrize("chip_file", glob.glob("chips/*.json"))
def test_validate_chip_json_schema(chip_file):
    validate(instance=json.load(open(chip_file, "r")), schema=chip)
