import reflex as rx

import index.styles.styles as styles
from index.components.link_button import link_button
from index.styles.colors import Color as Color
from index.styles.styles import Size as Size


def navbar() -> rx.Component:
    return rx.flex(
        rx.menu.root(
            rx.menu.trigger(
                link_button("Home", "#"),
                style=styles.BASE_STYLE[".navbar li"],

            ),
            rx.menu.trigger(
                link_button("Acerca de", "#"),
                style=styles.BASE_STYLE[".navbar li"],
                # class_name=["nav-link", "scrollto"],

                # style=styles.navbar_menu_button_style,
            ),
            rx.menu.trigger(
                link_button("Servicios", "#"),
                style=styles.BASE_STYLE[".navbar li"],
                # class_name=["nav-link", "scrollto"],

                # style=styles.navbar_menu_button_style,
            ),
            rx.menu.trigger(
                link_button("Contacto", "#"),
                style=styles.BASE_STYLE[".navbar li"],
                # class_name=["nav-link", "scrollto"],

                # style=styles.navbar_menu_button_style,
            ),
            style=styles.BASE_STYLE[".navbar ul"],
            # style=[
            #     styles.ul_style,
            #     styles.navbar_ul_style,
            # ],
        ),
        style=styles.BASE_STYLE[".navbar"],
        # class_name="navbar",
        # style=styles.navbar_style,
    )
