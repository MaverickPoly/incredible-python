import argparse


def rgb_to_hex(rgb_color: str):
    try:
        r_hex, g_hex, b_hex = map(lambda x: hex(int(x))[2:].upper(), rgb_color.split(" "))
        return f"#{r_hex}{g_hex}{b_hex}"
    except ValueError as e:
        print(f"Invalid rgb color: {e}")

def hex_to_rgb(hex_color: str):
    try:
        lst = hex_color[1:3], hex_color[3:5], hex_color[5:7]
        r, g, b = map(lambda x: int(x, 16), lst)
        return f"rgb({r}, {g}, {b})"
    except Exception as e:
        print(f"Invalid hex color: {e}")


def main():
    parser = argparse.ArgumentParser(description="Color Converter CLI")

    subparsers = parser.add_subparsers(dest="command")

    to_hex_parser = subparsers.add_parser("to_hex", help="RGB to Hex")
    to_hex_parser.add_argument("rgb", help="RGB in 'r g b' format")

    to_rgb_parser = subparsers.add_parser("to_rgb", help="Hex to RGB")
    to_rgb_parser.add_argument("hex", help="Hex in '#xxxxxx' format")

    args = parser.parse_args()

    match args.command:
        case "to_hex":
            hex_result = rgb_to_hex(args.rgb)
            print(hex_result)
        case "to_rgb":
            rgb_result = hex_to_rgb(args.hex)
            print(rgb_result)


if __name__ == '__main__':
    main()
