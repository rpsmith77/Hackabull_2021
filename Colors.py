""" RGB code colors """
import random


def ibm_color_blind_palette():
    """
    Color blind friendly color palette
    https://davidmathlogic.com/colorblind/#%23648FFF-%23785EF0-%23DC267F-%23FE6100-%23FFB000
    full palate can be found here: https://coolors.co/648fff-785ef0-dc267f-fe6100-ffb000
    :return: list of valid colors
    """
    CORNFLOWER_BLUE = (100, 143, 255)
    MEDIUM_SLATE_BLUE = (120, 94, 240)
    DEEP_CERISE = (220, 38, 127)
    SAFETY_BLAZER_ORANGE = (254, 97, 0)
    HONEY_YELLOW = (255, 176, 0)
    return [CORNFLOWER_BLUE, MEDIUM_SLATE_BLUE, DEEP_CERISE, SAFETY_BLAZER_ORANGE, HONEY_YELLOW]


def choose_random_color(colors):
    """
    choose random color out of list. Returns rgb color divided by 255 to work with PyCairo. PyCairo's rgb works from
    0.0 - 1.0 rather than 0 - 255
    :param colors: valid color choices
    :return: return the color with valid rgba values
    """
    color = random.choice(colors)
    return [color[0] / 255, color[1] / 255, color[2] / 255]
