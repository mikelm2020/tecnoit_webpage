import reflex as rx


def hero_title(text: str) -> rx.Component:
    return rx.chakra.text(
        text=text,
        # style=styles.h1_hero_style,
    )
