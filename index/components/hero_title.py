import reflex as rx
import index.styles.styles as styles


def hero_title(text: str) -> rx.Component:
    return rx.chakra.text(
        text=text,
        style=styles.h1_hero_style,
    )
