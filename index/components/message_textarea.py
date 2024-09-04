import reflex as rx


def message_textarea():
    """Creates a textarea for the message in the contact form."""
    return rx.el.textarea(
        class_name="dark:bg-gray-600 dark:border-gray-500 dark:text-gray-300",
        id="message",
        placeholder="Your Message",
        required=True,
        rows="4",
        appearance="none",
        border_width="1px",
        _focus={
            "outline-style": "none",
            "box-shadow": "0 0 0 3px rgba(59, 130, 246, 0.5)",
        },
        line_height="1.25",
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.25rem",
        box_shadow="0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
        color="#374151",
        width="100%",
    )
