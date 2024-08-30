import reflex as rx


def nav_link(link_text):
    """Creates a navigation link with hover effects."""
    return rx.el.a(
        link_text,
        class_name="dark:hover:text-blue-400 dark:text-gray-300",
        href="#",
        _hover={"color": "#3B82F6"},
        color="#4B5563",
    )
