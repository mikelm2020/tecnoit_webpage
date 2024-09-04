import reflex as rx

import index.components.dark_mode_toggle as dark_mode_toggle
import index.components.nav_link as nav_link


def navigation_bar():
    """Creates the main navigation bar with logo, links, and dark mode toggle."""
    return rx.flex(
        rx.box(
            "ProConsult",
            class_name="dark:text-white",
            font_weight="600",
            color="#1F2937",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        rx.box(
            nav_link.nav_link(link_text="Home"),
            nav_link.nav_link(link_text="Services"),
            nav_link.nav_link(link_text="About Us"),
            nav_link.nav_link(link_text="Case Studies"),
            nav_link.nav_link(link_text="Contact"),
            dark_mode_toggle.dark_mode_toggle(),
            display=rx.breakpoints({"0px": "none", "768px": "flex"}),
            column_gap="1.5rem",
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
    )
