import reflex as rx

import index.components.complex.client_logos_container as client_logos_container
import index.components.complex.next_button as next_button
import index.components.complex.previous_button as previous_button


def trusted_clients_section():
    """Create a section displaying trusted clients with a heading and logo carousel."""
    return rx.box(
        rx.heading(
            "Our Trusted Clients",
            class_name="dark:text-white",
            font_weight="600",
            margin_bottom="2rem",
            font_size="1.875rem",
            line_height="2.25rem",
            text_align="center",
            as_="h2",
        ),
        rx.box(
            client_logos_container.client_logos_container(),
            previous_button.previous_button(),
            next_button.next_button(),
            position="relative",
        ),
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
    )
