import reflex as rx

import index.components.footer_copyright as footer_copyright
import index.content.footer_content as footer_content


def footer():
    """Creates the complete footer section."""
    return rx.box(
        rx.box(
            footer_content.footer_content(),
            footer_copyright.footer_copyright(),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
        ),
        class_name="dark:bg-gray-900",
        background_color="#1F2937",
        padding_top="2rem",
        padding_bottom="2rem",
        color="#ffffff",
    )
