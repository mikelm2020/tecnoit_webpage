import reflex as rx


def bold_span(span_text):
    """Creates a bold span of text with specific styling."""
    return rx.text.span(
        span_text,
        class_name="dark:text-white",
        font_weight="600",
        font_size="1.125rem",
        line_height="1.75rem",
    )
