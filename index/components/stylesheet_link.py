import reflex as rx


def stylesheet_link(stylesheet_url):
    """Creates a link element for a stylesheet."""
    return rx.el.link(href=stylesheet_url, rel="stylesheet")
