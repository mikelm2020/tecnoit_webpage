import reflex as rx

import index.constants as constants
import index.styles.styles as styles
from index.components.client_image import client_image


def customers() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading(
                constants.CUSTOMER_TITLE,
                size="lg",
                color="white",
                style=[
                    styles.h2_style,
                    styles.h2_section_title_text_style,
                ],
            ),
            style=styles.section_title_style,
        ),
        rx.vstack(
            rx.flex(
                rx.flex(
                    client_image(
                        alt=constants.ALT_CLIENT_1,
                        img=constants.IMAGE_CLIENT_1,
                    ),
                    style=[
                        styles.col_4_style,
                        styles.d_flex_style,
                        styles.align_items_center_style,
                        styles.justify_content_center_style,
                    ],
                ),
                rx.flex(
                    client_image(
                        alt=constants.ALT_CLIENT_2,
                        img=constants.IMAGE_CLIENT_2,
                    ),
                    style=[
                        styles.col_4_style,
                        styles.d_flex_style,
                        styles.align_items_center_style,
                        styles.justify_content_center_style,
                    ],
                ),
                rx.flex(
                    client_image(
                        alt=constants.ALT_CLIENT_3,
                        img=constants.IMAGE_CLIENT_3,
                    ),
                    style=[
                        styles.col_4_style,
                        styles.d_flex_style,
                        styles.align_items_center_style,
                        styles.justify_content_center_style,
                    ],
                ),
                rx.flex(
                    client_image(
                        alt=constants.ALT_CLIENT_4,
                        img=constants.IMAGE_CLIENT_4,
                    ),
                    style=[
                        styles.col_4_style,
                        styles.d_flex_style,
                        styles.align_items_center_style,
                        styles.justify_content_center_style,
                    ],
                ),
                rx.flex(
                    client_image(
                        alt=constants.ALT_CLIENT_5,
                        img=constants.IMAGE_CLIENT_5,
                    ),
                    style=[
                        styles.col_4_style,
                        styles.d_flex_style,
                        styles.align_items_center_style,
                        styles.justify_content_center_style,
                    ],
                ),
            ),
            rx.flex(
                rx.flex(
                    client_image(
                        alt=constants.ALT_CLIENT_6,
                        img=constants.IMAGE_CLIENT_6,
                    ),
                    style=[
                        styles.col_4_style,
                        styles.d_flex_style,
                        styles.align_items_center_style,
                        styles.justify_content_center_style,
                    ],
                ),
                rx.flex(
                    client_image(
                        alt=constants.ALT_CLIENT_7,
                        img=constants.IMAGE_CLIENT_7,
                    ),
                    style=[
                        styles.col_4_style,
                        styles.d_flex_style,
                        styles.align_items_center_style,
                        styles.justify_content_center_style,
                    ],
                ),
                rx.flex(
                    client_image(
                        alt=constants.ALT_CLIENT_8,
                        img=constants.IMAGE_CLIENT_8,
                    ),
                    style=[
                        styles.col_4_style,
                        styles.d_flex_style,
                        styles.align_items_center_style,
                        styles.justify_content_center_style,
                    ],
                ),
                rx.flex(
                    client_image(
                        alt=constants.ALT_CLIENT_9,
                        img=constants.IMAGE_CLIENT_9,
                    ),
                    style=[
                        styles.col_4_style,
                        styles.d_flex_style,
                        styles.align_items_center_style,
                        styles.justify_content_center_style,
                    ],
                ),
                rx.flex(
                    client_image(
                        alt=constants.ALT_CLIENT_10,
                        img=constants.IMAGE_CLIENT_10,
                    ),
                    style=[
                        styles.col_4_style,
                        styles.d_flex_style,
                        styles.align_items_center_style,
                        styles.justify_content_center_style,
                    ],
                ),
                style=styles.row_style,
            ),
            style=styles.container_style,
        ),
        style=[
            styles.section_style,
            styles.clients_style,
        ],
    )
