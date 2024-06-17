import json


icons = {
    "+3v3": "fa-bolt",
    "+5v": "fa-triangle-exclamation",
    "i2c": "fa-microchip",
    "spi": "fa-magnifying-glass-arrow-right",
    "pwm": "fa-wave-square",
    "i2s": "fa-volume-off",
    "uart": "fa-bug",
    "gpclk": "fa-clock"
}

chip_cache = {}


def chip_path(chip):
    return f"chips/{chip}.json"


def get_chip(chip):
    if chip not in chip_cache:
        chip_cache[chip] = json.load(open(chip_path(chip)))

    return chip_cache[chip]


def get_chip_signal(chip, signal):
    return get_chip(chip)["signals"][signal]


data = json.load(open("boards/raspberry-pi-5.json", "r"))

header = data["headers"][0]

width = header["width"]
height = header["height"]
orientation = header["orientation"]
pins = header["pins"]

assert width * height == len(pins)

left_pins = pins[0::2]
right_pins = pins[1::2]

assert len(left_pins) == len(right_pins)

html = ""

banks = [
    {"pins": left_pins, "pin_offset": 1, "label": "J8 header, odd pins, left side", "class": "left"},
    {"pins": right_pins, "pin_offset": 2, "label": "J8 header, even pins, right side", "class": "right"}
]

for bank in banks:
    pins_html = ""
    for index, ref in enumerate(bank["pins"]):
        chip = ref["chip"]
        signal = ref["signal"]
        pin = get_chip_signal(chip, signal)
        name = pin["name"]
        pin_type = pin.get("type", "gpio")
        pin_subtype = pin.get("subtype")
        canonical_function = ""
        canonical_class = ""
        row_class = "gpio"
        cls = pin_type
        if pin_type == "power":
            cls = pin_subtype if pin_subtype == "ground" else "power"
            row_class = cls
        alt_html = ""

        try:
            canonical_function = ref["canonical_mode"]
            canonical_class = pin.get("alt_modes", [])[canonical_function]["type"]
            canonical_function = pin.get("alt_modes", [])[canonical_function]["name"]

            if canonical_class not in canonical_function:
                canonical_function = canonical_class + " " + canonical_function
            canonical_function = canonical_function.replace("_", " ")
            canonical_class = canonical_class.lower()
            row_class = canonical_class
        except KeyError:
            pass

        if pin_subtype in icons:
            icon = f'<i class="fa-solid {icons[pin_subtype]}"></i>'
        elif row_class in icons:
            icon = f'<i class="fa-solid {icons[row_class]}"></i>'
        else:
            icon = ""

        if row_class == "power":
            name = f"{icon}{name}"
        elif canonical_function:
            canonical_function = f"{icon}{canonical_function}"

        pin_index = index * 2 + bank["pin_offset"]
        pins_html += f"""            <tr aria-label="Physical pin {index + 1}" class="{row_class}">
<th>{pin_index}</th>
<td><a href="#">{name}</a></td>
<td><a href="#">{canonical_function}</a></td>
</tr>""".replace("\n", "")
        pins_html += "\n"

    html += f"""
        <table aria-label="{bank["label"]} pins" class="labels {bank["class"]}" aria-rowcount="20" aria-colcount="3" cellpadding="0" cellspacing="5">
            <thead>
                <th>Pin</th><th>Name</th><th>Function</th>
            </thead>
            <tbody>
{pins_html}
            </tbody>
        </table>
    """
    

template = open("template.html", "r").read()
template = template.format(pinout_table=html)
print(template)