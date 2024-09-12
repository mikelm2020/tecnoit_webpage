import reflex as rx

import index.components.main_heading as main_heading
import index.forms.contact.contact_form as contact_form


def contact_section():
    """Creates the contact section with heading and contact form."""
    return rx.box(
        main_heading.main_heading(heading_text="Contact Us"),
        rx.box(
            contact_form.contact_form(),
            max_width="32rem",
            margin_left="auto",
            margin_right="auto",
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
