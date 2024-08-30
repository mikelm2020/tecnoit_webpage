import reflex as rx


def section_heading(heading_text):
    """Creates a section heading with specific styling."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom="0.5rem",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )
