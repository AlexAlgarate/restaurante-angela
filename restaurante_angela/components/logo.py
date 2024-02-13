import reflex as rx
from restaurante_angela.styles import Routes


def logo() -> rx.Component:
    return rx.image(
        src=Routes.LOGO.value,
        alt="Imagen del logo del restaurante",
        width="134.182px",
        height="164px",
    )
