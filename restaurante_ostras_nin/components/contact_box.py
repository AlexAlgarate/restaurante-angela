import reflex as rx

from restaurante_ostras_nin.styles import Colors, utils


def contact_box() -> rx.Component:
    return rx.flex(
        _text(utils.number),
        _text(utils.email),
        direction="column",
    )


def _text(text: str) -> rx.Component:
    return rx.text(
        text,
        font_weight="600",
        line_height="30px",
        color=Colors.PHONE_NUMBER.value,
        font_size="18px",
    )
