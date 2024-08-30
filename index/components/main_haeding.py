import reflex as rx


def main_heading(heading_text):
    """Creates a main heading with centered text and specific styling."""
    return rx.heading(
        heading_text,
        class_name="dark:text-white",
        font_weight="600",
        margin_bottom="2rem",
        font_size="1.875rem",
        line_height="2.25rem",
        text_align="center",
        as_="h2",
    )
