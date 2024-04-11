import reflex as rx

import index.constants as constants
import index.styles.styles as styles


def about() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    constants.ABOUT_TITLE,
                    size="lg",
                    color="white",
                    style=[
                        styles.h2_style,
                        styles.h2_section_title_text_style,
                    ],
                ),
                style=styles.section_title_style,
            ),
            rx.flex(
                rx.vstack(
                    rx.text(
                        constants.ABOUT_CONTENT_LEFT_COLUMN,
                        style=styles.parragraph_text_style,
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            constants.ABOUT_LIST_ITEM_1,
                            style=styles.list_item_unordered_style,
                        ),
                        rx.list_item(
                            constants.ABOUT_LIST_ITEM_2,
                            style=styles.list_item_unordered_style,
                        ),
                        rx.list_item(
                            constants.ABOUT_LIST_ITEM_3,
                            style=styles.list_item_unordered_style,
                        ),
                    ),
                    style=styles.col_style,
                ),
                rx.vstack(
                    rx.text(
                        constants.ABOUT_CONTENT_RIGHT_COLUMN,
                        style=styles.parragraph_text_style,
                    ),
                    style=styles.col_style,
                    padding_top="0 !important",
                ),
                style=styles.row_style,
            ),
            style=styles.container_style,
        ),
        style=styles.section_style,
    )
