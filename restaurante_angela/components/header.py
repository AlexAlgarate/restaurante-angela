import reflex as rx


def header(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="8",
        color="#3a58de",
        margin_top="20px",
    )


# def header(text: str) -> rx.Component:
#     return rx.chakra.heading(
#         text,
#         size="2xl",
#         color="#3a58de",
#         margin_top="20px",
#     )
