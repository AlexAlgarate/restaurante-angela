import reflex as rx

from restaurante_angela.styles import Routes


def logo(width: str = "134.182px", height: str = "164px") -> rx.Component:
    return rx.image(
        src=Routes.LOGO.value,
        alt="Imagen del logo del restaurante",
        width=width,
        height=height,
    )
