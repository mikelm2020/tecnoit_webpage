import reflex as rx


def form_label(label_text):
    """Creates a form label with specific styling."""
    return rx.el.label(
        label_text,
        class_name="dark:text-gray-300",
        display="block",
        font_weight="700",
        margin_bottom="0.5rem",
        color="#374151",
        font_size="0.875rem",
        line_height="1.25rem",
    )
