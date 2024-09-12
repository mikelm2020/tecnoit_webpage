import reflex as rx


def carrusel_image(alt_text, image_source):
    """Create an image component with specified alt text and source."""
    return rx.image(
        src=image_source,
        alt=alt_text,
        height="6rem",
        object_fit="contain",
        width="6rem",
    )
