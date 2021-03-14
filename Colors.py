import random


def ibm_color_blind_palatte():
    CORNFLOWER_BLUE = (100, 143, 255)
    MEDIUM_SLATE_BLUE = (120, 94, 240)
    DEEP_CERISE = (220, 38, 127)
    SAFETY_BLAZER_ORANGE = (254, 97, 0)
    HONEY_YELLOW = (255, 176, 0)
    return [CORNFLOWER_BLUE, MEDIUM_SLATE_BLUE, DEEP_CERISE, SAFETY_BLAZER_ORANGE, HONEY_YELLOW]


def choose_random_color(colors):
    color = random.choice(colors)
    return [color[0] / 255, color[1] / 255, color[2] / 255]
