import reflex as rx

from restaurante_angela.styles import Size


def button_whastapp() -> rx.Component:
    return rx.link(
        rx.button(
            "Chat de Whastapp",
            border_color="#16297d",
            text_align="center",
            font_variant_numeric="lining-nums proportional-nums",
            padding="8px 24px",
            justify_content="center",
            align_items="center",
            gap="8px",
            align_self="stretch",
            border_radius="5px",
            border="2px solid #4F1F7E",
            background="#F8F8FA",
            font_size=[
                Size.DEFAULT.value,
                Size.DEFAULT.value,
                Size.DEFAULT.value,
                Size.LARGE.value,
                Size.LARGE.value,
            ],
        ),
        href="https://wa.me/34626131261",
        is_external=True,
    )
