from enum import Enum

import reflex as rx


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.25em"
    MEDIUM_SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    MAIN_TEXTS = "1.15em"
    LARGE = "1.5em"
    BIG = "2em"
    BIG_TITLES = "2.5em"
    MEDIUM_BIGGER = "3em"
    VERY_BIG = "4em"


class Color(Enum): ...


def header() -> rx.Component:
    return rx.heading(
        "Restaurante Ángela", size="2xl", color="#3a58de", margin_top="20px"
    )


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


def button_whastapp() -> rx.Component:
    return rx.link(
        rx.button(
            "Chat de Whastapp",
            border_color="#16297d",
            text_align="center",
            font_variant_numeric="lining-nums proportional-nums",
            padding="8px 24px",
            justify_content="center",
            align_items="center",
            gap="8px",
            align_self="stretch",
            border_radius="5px",
            border="2px solid #4F1F7E",
            background="#F8F8FA",
            font_size=[
                Size.DEFAULT.value,
                Size.DEFAULT.value,
                Size.DEFAULT.value,
                Size.LARGE.value,
                Size.LARGE.value,
            ],
        ),
        href="https://wa.me/34626131261",
        is_external=True,
    )


def spinner() -> rx.Component:
    return rx.spinner(
        color="white",
        size="lg",
        speed="1s",
        thickness=3,
    )


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.vstack(
            rx.flex(
                header(),
                main_text(),
                button_whastapp(),
                spinner(),
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
app.add_page(index)
