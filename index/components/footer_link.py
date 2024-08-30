import reflex as rx


def footer_link(link_text):
    """Creates a footer link with hover effects."""
    return rx.el.a(link_text, href="#", _hover={"color": "#ffffff"})
