import reflex as rx

from restaurante_angela.components.header import header
from restaurante_angela.components.main_text import main_text
from restaurante_angela.components.whastapp_button import button_whastapp


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.vstack(
            rx.flex(
                header("Restaurante Ángela"),
                main_text(),
                button_whastapp(),
                direction="column",
                align="center",
                justify="center",
                gap="20px",
                width="100%",
                max_width="800px",
            ),
            width="auto",
        ),
        background_color="#1b1d29" + "!important",
        width="100%",
        height="1000px",
        align_items="center",
    )


app = rx.App()
app.add_page(
    index,
    title="Restaurante Los Fogones de Ángela",
    description="Página web del restaurante Los Fogones de Ángela",
)
