import reflex as rx


def feature_icon(icon_alt_text, icon_tag):
    """Creates a feature icon with specific dimensions and styling."""
    return rx.icon(
        alt=icon_alt_text,
        tag=icon_tag,
        height="3rem",
        margin_bottom="1rem",
        width="3rem",
    )
