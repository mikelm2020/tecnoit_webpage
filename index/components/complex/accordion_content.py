import reflex as rx

import index.components.bold_paragraph as bold_paragraph
import index.components.muted_text as muted_text


def accordion_content(content_id, testimonial_text, author_info):
    """Creates the content for an accordion item with a testimonial and author info."""
    return rx.box(
        muted_text.muted_text(text_content=testimonial_text),
        bold_paragraph.bold_paragraph(paragraph_text=author_info),
        class_name="dark:bg-gray-600",
        id=content_id,
        background_color="#ffffff",
        display="none",
        padding="1rem",
        border_bottom_right_radius="0.5rem",
        border_bottom_left_radius="0.5rem",
    )
