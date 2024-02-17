import reflex as rx
import index.styles.styles as styles
from index.styles.styles import Size as Size


def hero_image(alt: str, img: str) -> rx.Component:
    return rx.chakra.image(
        src=img,
        alt=alt,
        style=[
            styles.img_style,
            styles.img_fluid_style,
            styles.animated_style,
        ],
    )
