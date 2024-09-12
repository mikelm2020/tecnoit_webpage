import reflex as rx


def footer_copyright():
    """Creates the copyright notice for the footer."""
    return rx.box(
        rx.text("© 2024 Tecnoit. All rights reserved."),
        border_color="#374151",
        border_top_width="1px",
        margin_top="2rem",
        padding_top="2rem",
        text_align="center",
        color="#9CA3AF",
        font_size="0.875rem",
        line_height="1.25rem",
    )
