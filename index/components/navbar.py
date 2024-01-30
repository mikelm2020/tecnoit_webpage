import reflex as rx
import index.styles.styles as styles
from index.styles.styles import Size as Size
from index.styles.colors import Color as Color


def navbar() -> rx.Component:
    return rx.flex(
        rx.menu(
            rx.menu_button(
                "Home",
                style=styles.navbar_menu_button_style,
            ),
            rx.menu_button(
                "Acerca de",
                style=styles.navbar_menu_button_style,
            ),
            rx.menu_button(
                "Servicios",
                style=styles.navbar_menu_button_style,
            ),
            rx.menu_button(
                "Contacto",
                style=styles.navbar_menu_button_style,
            ),
            style=[
                styles.ul_style,
                styles.navbar_ul_style,
            ],
        ),
        style=styles.navbar_style,
    )
