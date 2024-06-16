valid_alt_mode_types = ["I2C", "SPI", "DPI", "DSI", "UART", "PIO", "I2S", "GPCLOCK"]
valid_orientations = [0, 90, 180, 270]
valid_directions = ["alternating", "around"]
valid_pin_types = ["gpio", "power", "nc"]
valid_pin_subtypes = ["+5v", "+3v3", "ground"]

valid_header_types = ["dupont", "jst"]
valid_header_polarity = ["pin", "socket"]

board = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "headers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "width": {"type": "number"},
                    "height": {"type": "number"},
                    "orientation": {"type": "number", "enum": valid_orientations},
                    "direction": {"type": "string", "enum": valid_directions},
                    "type": {"type": "string", "enum": valid_header_types},
                    "polarity": {"type": "string", "enum": valid_header_polarity},
                    "pitch": {"type": "number"},
                    "pins": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "type": {"type": "string", "enum": valid_pin_types},
                                "subtype": {"type": "string", "enum": valid_pin_subtypes},
                                "canonical_mode": {"type": "number"},
                                "alt_modes": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "name": {"type": "string"},
                                            "type": {"type": "string", "enum": valid_alt_mode_types},
                                            "used": {"type": "boolean"}
                                        },
                                        "required": [
                                            "name"
                                        ]
                                    }
                                }
                            },
                            "required": [
                                "name"
                            ]
                        },
                        "unevaluatedItems": False
                    }
                },
                "required": [
                    "name",
                    "width",
                    "height"
                ]
            },
            "unevaluatedItems": False
        }
    }
}