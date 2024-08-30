import reflex as rx


def centered_icon(icon_alt_text, icon_tag):
    """Creates a centered icon with specific dimensions and styling."""
    return rx.icon(
        alt=icon_alt_text,
        tag=icon_tag,
        height="3rem",
        margin_bottom="1rem",
        margin_left="auto",
        margin_right="auto",
        width="3rem",
    )
