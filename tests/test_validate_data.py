import glob
import json

import pytest

chip_cache = {}


def chip_path(chip):
    return f"chips/{chip}.json"


def get_chip(chip):
    if chip not in chip_cache:
        chip_cache[chip] = json.load(open(chip_path(chip)))

    return chip_cache[chip]


def validate_pin(data):
    chip = get_chip(data["chip"])
    path = chip_path(data["chip"])
    signal = data["signal"]

    if signal not in chip["signals"]:
        raise AssertionError(f"Signal {signal} not found in {path}")


def validate_header(data):
    # name = data["name"]
    width = data["width"]
    height = data["height"]
    # orientation = data["orientation"]
    pins = data["pins"]

    assert width * height == len(pins)

    for pin in pins:
        validate_pin(pin)


@pytest.mark.parametrize("board_file", glob.glob("boards/*.json"))
def test_validate_board_json_files(board_file):
    data = json.load(open(board_file, "r"))

    for header in data["headers"]:
        validate_header(header)
