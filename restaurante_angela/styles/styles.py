from enum import Enum
import reflex as rx
from . import Colors, Fonts

MAX_WIDTH = "1440px"


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.25em"
    MEDIUM_SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    MAIN_TEXTS = "1.25em"
    LARGE = "1.5em"
    BIG = "2em"
    BIG_TITLES = "3.5em"
    VERY_BIG = "4em"


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Aclonica&family=Poppins&display=swap",
]

BASE_STYLE = {
    "background": Colors.BACKGROUND.value,
    rx.Heading: {
        "color": Colors.TITLE.value,
        "font_family": Fonts.TITLE.value,
        "font_style": "normal",
        "font_weight": "400",
        "line_height": "normal",
    },
    rx.Text: {
        "color": Colors.TEXT.value,
        "font_family": Fonts.DEFAULT.value,
        # "font_size": Size.MAIN_TEXTS.value,
        "font_style": "normal",
        "font_weight": "400",
        "line_height": "normal",
    },
}
