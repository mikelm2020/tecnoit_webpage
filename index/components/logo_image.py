import reflex as rx


def logo_image(image_alt_text, image_src):
    """Creates a logo image with specific dimensions and styling."""
    return rx.image(
        alt=image_alt_text,
        src=image_src,
        height="3rem",
        margin_right="1rem",
        width="3rem",
    )
