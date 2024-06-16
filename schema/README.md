# Pinout Board Schema

## Basic Requirements

Every board definition needs a `name` and one or more `headers`.

Headers entries are stored in an array and each describe a single, physical
header on a board. For example, the "J8" header (the main 40-pin header) on
a Raspberry Pi.

## Headers

Every header needs some basic info:

* `name` - The name of the header, eg: "J8"
* `width` - The physical width of the header (in pins), eg: 2
* `height` - The physical height of the header (in pins), eg: 20
* `direction` - The direction which pin numbers wrap around the header

Name is self explanatory, but should be the "unfriendly" name, eg: "J8" or
"J8" as written on the board silkscreen or otherwise.

Width and height are usually easy, we tend to describe pin headers as 2x20
or 1x5 and it's assumed you can picture what these are.

You can additionally specify some hints for rendering the header visually:

* `orientation` - The rotational orientation of the header
* `type` - The header type, normally "dupont"

Orientation is vague, but represents the orientation of the header (0, 90,
180 or 270 degrees) in relation to the up orientation of the board.

For example the Pi 5's 2x20 pin J8 header is considered to be orientated at
0 degrees. The original Pi 1's P2 header might be 90 or 270 degrees.

And further information about the specific type and size of the header:

* `type` - Eg: "dupont"
* `polarity` - Either "pin" or "socket"
* `pitch` - The connector pitch in inches