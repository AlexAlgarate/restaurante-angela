import reflex as rx

from restaurante_ostras_nin.components.apreciations import apreciations
from restaurante_ostras_nin.components.button_whastapp import button_whastapp
from restaurante_ostras_nin.components.contact_box import contact_box
from restaurante_ostras_nin.components.image_oyster import image_oyster
from restaurante_ostras_nin.components.logo import logo
from restaurante_ostras_nin.components.main_text import main_text
from restaurante_ostras_nin.styles import utils as utils


def mobile() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.box(
            rx.flex(
                logo(width="80.36px", height="98px"),
                rx.heading(utils.title, size="8"),
                main_text(utils.text_below_title_one),
                main_text(utils.text_below_title_two),
                contact_box(),
                apreciations(),
                button_whastapp(),
                image_oyster(
                    width="478px",
                    height="276px",
                    margin_top="-100px",
                ),
                direction="column",
                align="start",
                justify="center",
                gap="16px",
                padding="40px 16px 0 16px",
            ),
        ),
        width="375px",
        height="800px",
        max_width="500px",
    )
