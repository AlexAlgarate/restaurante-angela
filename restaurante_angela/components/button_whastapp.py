import reflex as rx

from restaurante_angela.styles import utils as utils
from restaurante_angela.styles.colors import Colors
from restaurante_angela.styles.fonts import Fonts


def button_whastapp() -> rx.Component:
    return rx.link(
        rx.button(
            utils.text_button,
            text_align="center",
            padding="18px",
            justify_content="center",
            align_items="center",
            gap="8px",
            background=Colors.BUTTON.value,
            border_radius="8px",
            color=Colors.BUTTON_TEXT.value,
            font_variant_numeric="lining_nums proportional_nums",
            font_family=Fonts.DEFAULT.value,
            font_size="18px",
            font_style="normal",
            font_weight="600",
            line_height="24px",
            letter_spacing="0.36px",
            width="fit-content",
        ),
        href="https://wa.me/34622498850",
        is_external=True,
        z_index="999",
    )
