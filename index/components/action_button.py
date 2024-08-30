import reflex as rx


def action_button(button_text):
    """Creates an action button with hover effects and specific styling."""
    return rx.el.a(
        button_text,
        class_name="dark:bg-gray-200 dark:hover:bg-gray-300 dark:text-blue-800",
        href="#",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#F3F4F6"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        color="#2563EB",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )
