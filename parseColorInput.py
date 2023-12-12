def parse_color_input(color_string):
    # Remove brackets and split by comma
    color_values = color_string.strip("[]").split(",")
    # Convert each string in the list to an integer
    return [int(value.strip()) for value in color_values]