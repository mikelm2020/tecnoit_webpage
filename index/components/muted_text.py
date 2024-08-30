import reflex as rx


def muted_text(text_content):
    """Creates muted text with specific styling."""
    return rx.text(
        text_content,
        class_name="dark:text-gray-300",
        color="#4B5563",
    )
