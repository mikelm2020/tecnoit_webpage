import reflex as rx

import index.components.line_break as line_break
import index.components.section_heading as section_heading


def footer_contact_info():
    """Creates the contact information section in the footer."""
    return rx.box(
        section_heading.section_heading(heading_text="Contact Us"),
        rx.text(
            "123 Business St, Suite 100",
            line_break.line_break(),
            "New York, NY 10001",
            line_break.line_break(),
            "Phone: (555) 123-4567",
            line_break.line_break(),
            "Email: info@proconsult.com",
            color="#9CA3AF",
        ),
        margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
        width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
    )
