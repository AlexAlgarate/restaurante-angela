from enum import Enum


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.25em"
    MEDIUM_SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    MAIN_TEXTS = "1.15em"
    LARGE = "1.5em"
    BIG = "2em"
    BIG_TITLES = "2.5em"
    MEDIUM_BIGGER = "3em"
    VERY_BIG = "4em"


class Color(Enum): ...
