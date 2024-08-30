import reflex as rx

import index.components.complex.logo_with_text as logo_with_text
import index.components.small_icon as small_icon


def accordion_button(onclick_function, logo_alt_text, logo_src, company_name):
    """Creates an accordion button with a logo, company name, and expand icon."""
    return rx.el.button(
        logo_with_text.logo_with_text(
            logo_alt_text=logo_alt_text,
            logo_src=logo_src,
            company_name=company_name,
        ),
        small_icon.small_icon(icon_alt_text="Expand", icon_tag="chevron-down"),
        class_name="dark:bg-gray-700",
        onclick=onclick_function,
        background_color="#E5E7EB",
        display="flex",
        _focus={"outline-style": "none"},
        align_items="center",
        justify_content="space-between",
        padding="1rem",
        border_radius="0.5rem",
        width="100%",
    )
