import reflex as rx

import index.components.action_button as action_button
import index.components.description_text as description_text


def create_cta_section():
    """Creates a call-to-action section with heading, description, and button."""
    return rx.box(
        rx.heading(
            "Ready to Transform Your Business?",
            font_weight="600",
            margin_bottom="1rem",
            font_size="1.875rem",
            line_height="2.25rem",
            as_="h2",
        ),
        description_text.description_text(
            description_content="Let's collaborate to unlock your organization's full potential"
        ),
        action_button.action_button(button_text="Contact Us Today"),
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
        text_align="center",
    )
