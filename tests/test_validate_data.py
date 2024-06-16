import glob
import json

import pytest


def validate_alt_mode(data):
    # name = data["name"]
    mode_type = data.get("type", "")

    assert mode_type != ""
    assert not mode_type.endswith("?")


def validate_pin(data):
    alt_modes = data.get("alt_modes", [])

    for alt_mode in alt_modes:
        validate_alt_mode(alt_mode)


def validate_header(data):
    width = data["width"]
    height = data["height"]
    # orientation = data["orientation"]
    pins = data["pins"]

    assert width * height == len(pins)

    for pin in pins:
        validate_pin(pin)


@pytest.mark.parametrize('board_file', glob.glob("boards/*.json"))
def test_validate_board_json_files(board_file):
    data = json.load(open(board_file, "r"))

    for name, header in data["headers"].items():
        validate_header(header)
