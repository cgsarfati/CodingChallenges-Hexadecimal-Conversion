"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""

    # HOW TO CONVERT:
        # Get decimal equiv. of hex from table
        # Multiply qdigit w/ 16 power of digit's index
        # Sum all multipliers

    # have dict. to convert hex char to dec. value
    convert = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    # set counter
    result = 0

    # loop through char
    for i, hex_char in enumerate(hex_in):

        # convert hex char to digit
        hex_digit = convert[hex_char]

        # get reversed index position
        power = 16 ** (len(hex_in) - i - 1)

        # multiply digit to 16^index; get running total
        result = result + hex_digit * power

    return result


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n"
