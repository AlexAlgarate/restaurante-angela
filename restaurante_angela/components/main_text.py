import reflex as rx

from restaurante_angela.styles import Size


def _text(text: str) -> rx.Component:
    return rx.text(
        text,
        font_size=[
            Size.DEFAULT.value,
            Size.DEFAULT.value,
            Size.DEFAULT.value,
            Size.LARGE.value,
            Size.LARGE.value,
        ],
        color="#fff",
        text_align="center",
        justify_content="center",
        align_items="center",
        align_self="stretch",
    )


def main_text() -> rx.Component:
    return rx.vstack(
        _text("Página en construcción, disculpen las molestias."),
        _text(
            "Si quieren ponerse en contacto a través de Wahtsapp, haga click en el botón:"
        ),
    )
