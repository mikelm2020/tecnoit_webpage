import reflex as rx

import index.components.action_button as action_button
import index.components.description_text as description_text


def create_hero_content():
    """Creates the content for the hero section including heading, description, and call-to-action button."""
    return rx.box(
        rx.heading(
            "Expert Consulting Services",
            font_weight="700",
            margin_bottom="1rem",
            font_size=rx.breakpoints({"0px": "2.25rem", "768px": "3rem"}),
            line_height=rx.breakpoints({"0px": "2.5rem", "768px": "1"}),
            as_="h1",
        ),
        description_text.description_text(
            description_content="Empowering businesses with strategic solutions and innovative insights"
        ),
        action_button.action_button(button_text="Get Started"),
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
        position="relative",
        text_align="center",
        z_index="10",
    )
