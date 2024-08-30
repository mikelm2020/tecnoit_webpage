import reflex as rx


def feature_heading(heading_text):
    """Creates a feature heading with specific styling."""
    return rx.heading(
        heading_text,
        class_name="dark:text-white",
        font_weight="600",
        margin_bottom="0.5rem",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )
