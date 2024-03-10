import reflex as rx


def main_text(text: str) -> rx.Component:
    return rx.text(
        text,
        font_size=[
            "16px",
            "18px",
            "18px",
            "18px",
            "18px",
        ],
    )
