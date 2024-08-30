import reflex as rx


def bold_paragraph(paragraph_text):
    """Creates a bold paragraph with specific styling."""
    return rx.text(
        paragraph_text,
        class_name="dark:text-white",
        font_weight="600",
        margin_top="0.5rem",
    )
