import reflex as rx
from index.components.hero_image import hero_image
import index.styles.styles as styles
import index.constants as constants


def hero() -> rx.Component:
    return rx.chakra.flex(
        rx.chakra.hstack(
            rx.chakra.flex(
                rx.chakra.flex(
                    rx.chakra.heading(
                        constants.HERO_TITLE,
                        as_="h1",
                        style=[
                            styles.h1_style,
                            styles.h1_hero_style,
                        ],
                    ),
                    rx.chakra.heading(
                        constants.HERO_SUBTITLE,
                        style=[
                            styles.h2_style,
                            styles.h2_hero_style,
                        ],
                    ),
                    style=[
                        styles.col_style,
                        styles.d_flex_style,
                        styles.flex_column_style,
                        styles.justify_content_center_style,
                        styles.pt_4_style,
                        styles.pt_style,
                        styles.order_2_style,
                        styles.order_1_style,
                    ],
                ),
                rx.chakra.hstack(
                    hero_image(
                        alt="imagen con computadoras que demuestran tecnología",
                        img="img/hero-img.png",
                    ),
                    style=[
                        styles.col_style,
                        styles.order_1_style,
                        styles.order_2_style,
                        styles.aos_animate_style,
                        styles.data_aos_zoom_in_style,
                        styles.data_aos_delay_style,
                    ],
                ),
                style=styles.row_style,
            ),
            style=[
                styles.container_style,
                styles.hero_container_style,
            ],
        ),
        style=[
            styles.section_style,
            styles.hero_style,
            styles.d_flex_style,
            styles.align_items_center_style,
        ],
    )
