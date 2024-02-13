import reflex as rx
from restaurante_angela.styles import Routes


def image_oyster() -> rx.Component:
    return rx.image(
        src=Routes.OYSTER_DESKTOP.value,
        alt="Foto principal con varias ostras, un limón y los útiles para abrir las ostras",
        position="absolute",
        top="250px",
        left="351px",
        bottom="107px",
        width="550px",
    )
