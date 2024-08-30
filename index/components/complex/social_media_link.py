import reflex as rx

import index.components.small_icon as small_icon


def social_media_link(icon_alt_text, icon_tag):
    """Creates a social media link with an icon."""
    return rx.el.a(
        small_icon.small_icon(icon_alt_text=icon_alt_text, icon_tag=icon_tag),
        href="#",
        _hover={"color": "#ffffff"},
        color="#9CA3AF",
    )
