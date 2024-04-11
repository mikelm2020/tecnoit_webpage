import reflex as rx

import index.styles.styles as styles


def logo(alt: str, img: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=img,
            alt=alt,
            # style=[
            #     styles.img_style,
            #     styles.img_fluid_style,
            # ],
            max_height="100px",
            class_name="img-fluid",
        ),
        href=url,
        is_external=False,
        class_name=[
            "logo",
            "me-auto",
        ],
        style=styles.BASE_STYLE["#header .logo"],
        # style=[
        #     styles.logo_href_style,
        #     styles.me_auto_style,
        # ],
    )
