valid_orientations = [0, 90, 180, 270]
valid_header_types = ["dupont", "jst", "ffc"]
valid_header_polarity = ["pin", "socket"]

board_pin = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "width": {"type": "number"},
        "height": {"type": "number"},
        "orientation": {"type": "number", "enum": valid_orientations},
        "type": {"type": "string", "enum": valid_header_types},
        "polarity": {"type": "string", "enum": valid_header_polarity},
        "pitch": {"type": "number"},
        "pins": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "chip": {"type": "string"},
                    "signal": {"type": "string"},
                    "canonical_mode": {"type": "number"},
                },
                "required": ["chip", "signal"],
            },
            "unevaluatedItems": False,
        },
    },
    "required": ["name", "width", "height"],
    "additionalProperties": False,
}

board = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "headers": {"type": "array", "items": board_pin, "unevaluatedItems": False},
    },
}
