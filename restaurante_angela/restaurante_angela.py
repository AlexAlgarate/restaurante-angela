import reflex as rx

from restaurante_angela.components.main_text import main_text
from restaurante_angela.components.button_whastapp import button_whastapp
from restaurante_angela.components.logo import logo
from restaurante_angela.components.contact_box import contact_box
from restaurante_angela.components.apreciations import apreciations
from restaurante_angela.components.image_oyster import image_oyster

from restaurante_angela.styles import styles
from restaurante_angela.styles import utils as utils


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.flex(
            logo(),
            rx.heading(utils.title, size="2xl"),
            main_text(utils.text_below_title_one),
            main_text(utils.text_below_title_two),
            contact_box(),
            apreciations(),
            button_whastapp(),
            image_oyster(),
            direction="column",
            align="start",
            justify="center",
            gap="24px",
            top="90px",
            left="80px",
            width="881px",
            position="relative",
            max_width=styles.MAX_WIDTH,
        ),
        width="100%",
        height="994px",
    )


app = rx.App(style=styles.BASE_STYLE, stylesheets=styles.STYLESHEETS)
app.add_page(
    index,
    title="Restaurante Ostras Nin",
    description="Página web del restaurante Ostras Nin",
)
