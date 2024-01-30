import reflex as rx
from index.styles.styles import Size as Size
from index.styles.colors import Color as Color
from index.styles.colors import TextColor as TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value,
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value,
    )
