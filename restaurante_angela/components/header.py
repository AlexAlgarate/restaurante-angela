import reflex as rx


def header(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="2xl",
        color="#3a58de",
        margin_top="20px",
    )
