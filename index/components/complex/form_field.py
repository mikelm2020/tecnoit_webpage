import reflex as rx

import index.components.form_input as form_input
import index.components.form_label as form_label


def form_field(label_text, input_id, input_placeholder, input_type):
    """Creates a form field with a label and input."""
    return rx.box(
        form_label.form_label(label_text=label_text),
        form_input.form_input(
            input_id=input_id,
            input_placeholder=input_placeholder,
            input_type=input_type,
        ),
        margin_bottom="1rem",
    )
