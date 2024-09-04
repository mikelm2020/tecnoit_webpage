import reflex as rx

import index.components.complex.testimonials_accordion as testimonials_accordion
import index.components.main_heading as main_heading


def testimonials_section():
    """Creates the testimonials section with heading and accordion."""
    return rx.box(
        rx.box(
            main_heading.main_heading(heading_text="Client Testimonials"),
            testimonials_accordion.testimonials_accordion(),
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
        class_name="dark:bg-gray-800",
        background_color="#ffffff",
        padding_top="4rem",
        padding_bottom="4rem",
    )
