import reflex as rx
import index.styles.styles as styles
from index.styles.colors import DarkMode as DarkMode


def link_button(title: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            title,
            variant="soft",
            size="2",
            radius="large",
            class_name=["nav-link", "scrollto", "active"],

        ),
        href=url,
        is_external=False,
        width="100%",
        style=styles.BASE_STYLE[".navbar a,.navbar a:focus"]

    )
