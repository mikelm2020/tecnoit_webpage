import reflex as rx
import index.styles.styles as styles
from index.styles.styles import Size as Size


def logo(alt: str, img: str, url: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            src=img,
            alt=alt,
            style=[
                styles.img_style,
                styles.img_fluid_style,
            ],
            max_height="100px",
        ),
        href=url,
        is_external=False,
        style=[
            styles.logo_href_style,
            styles.me_auto_style,
        ],
    )
