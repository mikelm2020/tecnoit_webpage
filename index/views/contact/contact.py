import reflex as rx
import index.styles.styles as styles
import index.constants as constants


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
                style=styles.section_title_style,
            ),
            style=[
                styles.container_style,
                styles.aos_animate_style,
                styles.data_aos_fade_up_style,
            ],
        ),
        style=styles.section_style,
    )
