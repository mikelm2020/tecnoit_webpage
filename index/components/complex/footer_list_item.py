import reflex as rx

import index.components.footer_link as footer_link


def footer_list_item(link_text):
    """Creates a list item for the footer links."""
    return rx.el.li(footer_link.footer_link(link_text=link_text))
