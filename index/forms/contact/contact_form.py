import reflex as rx

import index.components.complex.form_field as form_field
import index.components.form_label as form_label
import index.components.message_textarea as message_textarea
import index.components.subject_input as subject_input
import index.components.submit_button as submit_button


def contact_form():
    """Creates the complete contact form with all fields and submit button."""
    return rx.form(
        form_field.form_field(
            label_text="Name",
            input_id="name",
            input_placeholder="Your Name",
            input_type="text",
        ),
        form_field.form_field(
            label_text="Email",
            input_id="email",
            input_placeholder="Your Email",
            input_type="email",
        ),
        rx.box(
            form_label.form_label(label_text="Subject"),
            subject_input.subject_input(),
            margin_bottom="1rem",
        ),
        rx.box(
            form_label.form_label(label_text="Message"),
            message_textarea.message_textarea(),
            margin_bottom="1.5rem",
        ),
        rx.flex(
            submit_button.submit_button(),
            display="flex",
            align_items="center",
            justify_content="space-between",
        ),
        class_name="dark:bg-gray-700",
        background_color="#F3F4F6",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
