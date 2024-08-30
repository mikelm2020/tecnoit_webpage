import reflex as rx


def small_icon(icon_alt_text, icon_tag):
    """Creates a small icon with specific dimensions."""
    return rx.icon(
        alt=icon_alt_text,
        tag=icon_tag,
        height="1.5rem",
        width="1.5rem",
    )
