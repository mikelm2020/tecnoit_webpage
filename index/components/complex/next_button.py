import reflex as rx

import index.components.carrusel_icon as carrusel_icon


def next_button():
    """Create a styled 'Next' button with a right chevron icon."""
    return rx.el.button(
        carrusel_icon.carrusel_icon(icon_alt_text="Next", icon_tag="chevron-right"),
        class_name="dark:bg-gray-700 dark:hover:bg-gray-600 transform",
        transform="translateY(-50%)",
        position="absolute",
        background_color="#ffffff",
        transition_duration="300ms",
        _hover={"background-color": "#F3F4F6"},
        padding="0.5rem",
        right="0",
        border_radius="9999px",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        top="50%",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )
