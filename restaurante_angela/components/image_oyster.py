import reflex as rx

from restaurante_angela.styles import Routes


def image_oyster(
    width: str = "856x",
    height: str = "472px",
    position: str = None,
    right: str = None,
    bottom: str = None,
    **kwargs
) -> rx.Component:
    return rx.image(
        src=Routes.OYSTER_DESKTOP.value,
        alt="Foto principal con varias ostras, un limón y los útiles para abrir las ostras",
        position=position,
        right=right,
        bottom=bottom,
        width=width,
        height=height,
        **kwargs
    )
