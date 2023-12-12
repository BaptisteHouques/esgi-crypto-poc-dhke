def mix_tier_color(color1, color2):
    mix = [(2 * (color1[0]/3) + color2[0]/3) / 2, (2 * (color1[1]/3) + color2[1]/3) / 2, (2 * (color1[2]/3) + color2[2]/3) / 2]
    print(mix)