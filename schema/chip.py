valid_alt_mode_types = [
    "I2C",
    "SPI",
    "DPI",
    "DSI",
    "UART",
    "PIO",
    "I2S",
    "GPCLK",
    "JTAG",
    "SDIO",
    "SMI",
    "PWM",
    "UNUSED",
]
valid_pin_types = ["gpio", "power", "nc"]
valid_pin_subtypes = ["+5v", "+3v3", "ground"]

chip_signal = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "type": {"type": "string", "enum": valid_pin_types},
        "subtype": {"type": "string", "enum": valid_pin_subtypes},
        "alt_modes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "type": {"type": "string", "enum": valid_alt_mode_types},
                },
                "required": ["name", "type"],
            },
        },
    },
}

chip = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "signals": {"type": "object", "additionalProperties": chip_signal},
    },
}
