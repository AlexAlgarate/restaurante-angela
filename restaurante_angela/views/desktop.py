import reflex as rx

from restaurante_angela.components.apreciations import apreciations
from restaurante_angela.components.button_whastapp import button_whastapp
from restaurante_angela.components.contact_box import contact_box
from restaurante_angela.components.image_oyster import image_oyster
from restaurante_angela.components.logo import logo
from restaurante_angela.components.main_text import main_text
from restaurante_angela.styles import utils as utils


def desktop() -> rx.Component:
    return rx.desktop_only(
        rx.box(
            rx.flex(
                logo(),
                rx.heading(utils.title, size="2xl"),
                main_text(utils.text_below_title_one),
                main_text(utils.text_below_title_two),
                contact_box(),
                apreciations(),
                button_whastapp(),
                image_oyster(
                    position="absolute",
                    right="0px",
                    bottom="0px",
                ),
                direction="column",
                align="start",
                justify="center",
                width="100%",
            ),
            padding_right=" 480px",
            flex="1 0 0",
            gap="24px",
            align_self="stretch",
            height="100%",
            max_height="1095px",
            # width="100%",
        ),
        padding="90px 80px 86px 80px",
        max_width="1440px",
    )


# def desktop() -> rx.Component:
#     return rx.desktop_only(
#         rx.flex(
#             logo(),
#             rx.heading(utils.title, size="2xl"),
#             main_text(utils.text_below_title_one),
#             main_text(utils.text_below_title_two),
#             contact_box(),
#             apreciations(),
#             button_whastapp(),
#             image_oyster(
#                 position="absolute",
#                 right="0px",
#                 bottom="0px",
#             ),
#             direction="column",
#             align="start",
#             justify="center",
#             max_width="1280px",
#             padding_right=" 480px",
#             flex="1 0 0",
#             gap="24px",
#             align_self="stretch",
#         ),
#         padding="90px 80px 86px 80px",
#         width="1440px",
#         justify="center",
#         align="center",
#     )