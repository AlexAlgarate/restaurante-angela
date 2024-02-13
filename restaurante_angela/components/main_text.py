import reflex as rx

from restaurante_angela.styles.styles import Size


def main_text(text: str) -> rx.Component:
    return rx.text(text, font_size="18px")
