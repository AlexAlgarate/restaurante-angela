import reflex as rx
from restaurante_angela.styles import utils
from restaurante_angela.styles import Colors, Fonts


def apreciations() -> rx.Component:
    return rx.text(
        utils.appreciation,
        color=Colors.TITLE.value,
        font_family=Fonts.TITLE.value,
        line_height="30px",
    )
