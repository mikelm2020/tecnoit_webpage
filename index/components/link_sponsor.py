import reflex as rx
import index.styles.styles as styles
from index.styles.styles import Size as Size


def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            src=imagen,
            height=Size.VERY_BIG.value,
            width="auto",
            alt=alt,
        ),
        href=url,
        is_external=True,
    )
