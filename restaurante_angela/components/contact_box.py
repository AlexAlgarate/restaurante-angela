import reflex as rx
from restaurante_angela.styles import utils
from restaurante_angela.styles import Colors


def contact_box() -> rx.Component:
    return rx.flex(
        rx.text(
            utils.number,
            font_weight="600",
            line_height="30px",
            color=Colors.PHONE_NUMBER.value,
        ),
        rx.text(
            utils.email,
            font_weight="600",
            line_height="30px",
            color=Colors.PHONE_NUMBER.value,
        ),
        direction="column",
    )
