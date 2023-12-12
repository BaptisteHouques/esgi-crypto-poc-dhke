import sys
from parseColorInput import parse_color_input
from mixColor import mix_color
from mixTierColor import mix_tier_color

def main():
    args = sys.argv

    cmd = args[1]
    if cmd == "mixMyColors":
        # Split the input into two parts
        main_color_str, second_color_str = args[2].split(";")

        # Parse each part into a color
        main_color = parse_color_input(main_color_str)
        second_color = parse_color_input(second_color_str)

        mix_color(main_color, second_color)
    elif cmd == "decodeColors":
        # Split the input into two parts
        main_color_str, second_color_str = args[2].split(";")

        # Parse each part into a color
        main_color = parse_color_input(main_color_str)
        second_color = parse_color_input(second_color_str)

        mix_tier_color(main_color, second_color)

if __name__ == "__main__":
    main()