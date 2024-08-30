import reflex as rx


def learn_more_link(link_url):
    """Creates a 'Learn More' link with hover effects."""
    return rx.el.a(
        "Learn More",
        class_name="dark:hover:text-blue-300 dark:text-blue-400",
        href=link_url,
        font_weight="600",
        _hover={"color": "#2563EB"},
        color="#3B82F6",
    )
