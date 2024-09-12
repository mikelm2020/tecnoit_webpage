import reflex as rx


def carrusel_icon(icon_alt_text, icon_tag):
    """Create an icon component with specified alt text and tag."""
    return rx.icon(
        alt=icon_alt_text,
        class_name="dark:text-gray-300",
        tag=icon_tag,
        height="1.5rem",
        color="#4B5563",
        width="1.5rem",
    )
