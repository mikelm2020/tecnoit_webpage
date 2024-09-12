import reflex as rx

import index.components.centered_icon as centered_icon
import index.components.feature_heading as feature_heading
import index.components.muted_text as muted_text


def feature_box(icon_alt_text, icon_tag, heading_text, description_text):
    """Creates a feature box with an icon, heading, and description."""
    return rx.box(
        centered_icon.centered_icon(icon_alt_text=icon_alt_text, icon_tag=icon_tag),
        feature_heading.feature_heading(heading_text=heading_text),
        muted_text.muted_text(text_content=description_text),
        text_align="center",
    )
