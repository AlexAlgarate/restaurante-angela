import reflex as rx

from restaurante_angela.components.apreciations import apreciations
from restaurante_angela.components.button_whastapp import button_whastapp
from restaurante_angela.components.contact_box import contact_box
from restaurante_angela.components.image_oyster import image_oyster
from restaurante_angela.components.logo import logo
from restaurante_angela.components.main_text import main_text
from restaurante_angela.styles import styles
from restaurante_angela.styles import utils as utils


def index() -> rx.Component:
    return rx.vstack(
        rx.script("document.documentElement.lang='es'"),
        rx.desktop_only(
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
                max_width="1280px",
                padding_right=" 480px",
                flex="1 0 0",
                gap="24px",
                align_self="stretch",
            ),
            padding="90px 80px 86px 80px",
            width="1440px",
            justify="center",
            align="center",
        ),
        rx.mobile_and_tablet(
            rx.box(
                rx.flex(
                    logo(width="80.36px", height="98px"),
                    rx.heading(utils.title, size="2xl"),
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
        ),
    )


app = rx.App(style=styles.BASE_STYLE, stylesheets=styles.STYLESHEETS)
app.add_page(
    index,
    title="Restaurante Ostras Nin",
    description="Página web del restaurante Ostras Nin",
)
