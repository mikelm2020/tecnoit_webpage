import reflex as rx

import index.components.complex.navigation_bar as navigation_bar


def header():
    """Creates the header section with navigation bar."""
    return rx.box(
        rx.box(
            navigation_bar.navigation_bar(),
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
            padding_top="0.75rem",
            padding_bottom="0.75rem",
        ),
        class_name="dark:bg-gray-800",
        background_color="#ffffff",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
