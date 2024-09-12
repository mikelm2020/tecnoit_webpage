import reflex as rx

import index.components.carrusel_image as carrusel_image


def client_logo(logo_alt_text, logo_source):
    """Create a flexible container for a client logo with styling."""
    return rx.flex(
        carrusel_image.carrusel_image(alt_text=logo_alt_text, image_source=logo_source),
        class_name="dark:bg-gray-700 flex-shrink-0",
        background_color="#E5E7EB",
        display="flex",
        height="8rem",
        align_items="center",
        justify_content="center",
        border_radius="9999px",
        width="8rem",
    )
