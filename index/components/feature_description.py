import reflex as rx


def feature_description(description_text):
    """Creates a feature description with specific styling."""
    return rx.text(
        description_text,
        class_name="dark:text-gray-300",
        margin_bottom="1rem",
        color="#4B5563",
    )
