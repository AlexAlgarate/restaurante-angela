import reflex as rx

from restaurante_angela.styles import styles
from restaurante_angela.views.desktop import desktop
from restaurante_angela.views.mobile import mobile


def index() -> rx.Component:
    return rx.hstack(
        rx.script("document.documentElement.lang='es'"),
        desktop(),
        mobile(),
        min_height="100%",
    )


app = rx.App(style=styles.BASE_STYLE, stylesheets=styles.STYLESHEETS)
app.add_page(
    index,
    title="Restaurante Ostras Nin",
    description="Página web del restaurante Ostras Nin",
    image="/images/imagen_web_ostras_nin.jpg",
)
