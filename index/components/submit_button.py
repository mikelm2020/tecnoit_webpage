import reflex as rx


def submit_button():
    """Creates a submit button for the contact form."""
    return rx.el.button(
        " Send Message ",
        type="submit",
        background_color="#3B82F6",
        transition_duration="300ms",
        _focus={
            "outline-style": "none",
            "box-shadow": "0 0 0 3px rgba(59, 130, 246, 0.5)",
        },
        font_weight="700",
        _hover={"background-color": "#1D4ED8"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )
