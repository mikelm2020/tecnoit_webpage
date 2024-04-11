import reflex as rx

import index.styles.styles as styles
from index.styles.styles import Size as Size


def hero_image(alt: str, img: str) -> rx.Component:
    return rx.image(
        src=img,
        alt=alt,
        class_name=[
            "img-fluid",
            "animated",
        ],
        style=styles.BASE_STYLE["#hero .animated"],
    )
