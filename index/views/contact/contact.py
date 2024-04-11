import reflex as rx

import index.constants as constants
import index.styles.styles as styles


def contact() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.vstack(
            rx.chakra.vstack(
                rx.chakra.heading(
                    constants.CONTACT_TITLE,
                    size="lg",
                    color="white",
                    style=[
                        styles.h2_style,
                        styles.h2_section_title_text_style,
                    ],
                ),
                rx.chakra.text(
                    constants.CONTACT_CONTENT,
                    style=styles.parragraph_text_style,
                ),
                rx.chakra.flex(
                    rx.chakra.flex(
                        rx.chakra.vstack(
                            rx.chakra.vstack(
                                rx.chakra.flex(
                                    rx.heading(
                                        "Localización:",
                                        as_="h4",
                                        style=[
                                            styles.h4_style,
                                            styles.h4_info_contact_style,
                                        ],
                                    ),
                                    rx.text(
                                        constants.CONTACT_LOCATION,
                                        as_="p",
                                    ),
                                    class_name=["bi", "bi-geo-alt"],
                                ),
                                class_name="address",
                            ),
                            class_name="info",
                        ),
                        class_name=[
                            "col-Ig-5",
                            "d-flex",
                            "align-items-strecht",
                        ],
                    ),
                    rx.chakra.flex(
                        class_name=[
                            "col-Ig-7",
                            "mt-5",
                            "mt-Ig-0",
                            "d-flex",
                            "align-items-stretch",
                        ],
                    ),
                    style=styles.row_style,
                    class_name="row",
                ),
                style=styles.section_title_style,
                class_name="section_title",
            ),
            style=[
                styles.container_style,
                styles.aos_animate_style,
                styles.data_aos_fade_up_style,
            ],
            class_name=["container", "aos_init", "aos_animate"],
        ),
        class_name="contact",
        style=styles.section_style,
    )
