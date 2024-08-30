import reflex as rx


def description_text(description_content):
    """Creates a description text block with specific styling."""
    return rx.text(
        description_content,
        margin_bottom="2rem",
        font_size="1.25rem",
        line_height="1.75rem",
    )
