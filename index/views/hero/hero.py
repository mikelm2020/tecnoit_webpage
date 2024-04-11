import reflex as rx

import index.constants as constants
import index.styles.styles as styles
from index.components.hero_image import hero_image


def hero() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.flex(
                rx.flex(
                    rx.heading(
                        constants.HERO_TITLE,
                        as_="h1",
                        style=[
                            styles.BASE_STYLE["#hero h1"],
                            styles.BASE_STYLE["h1,h2,h3,h4,h5,h6"],
                        ],
                    ),
                    rx.heading(
                        constants.HERO_SUBTITLE,
                        as_="h2",
                        style=[
                            styles.BASE_STYLE["#hero h2"],
                            styles.BASE_STYLE["h1,h2,h3,h4,h5,h6"],
                        ],
                    ),
                    rx.flex(
                        rx.link(
                            "Iniciar",
                            href="#about",
                            class_name=["btn-get-started", "scrollto"],
                            style=styles.BASE_STYLE["#hero .btn-get-started"],
                        ),
                        class_name=[
                            "d-flex",
                            "justify-content-center",
                            "justify-content-lg-start",
                        ],
                    ),
                    class_name=[
                        "col-lg-6",
                        "d-flex",
                        "flex-column",
                        "justify-content-center",
                        "pt-4",
                        "pt-lg-0",
                        "order-2",
                        "order-lg-11",
                        "aos-init",
                        "aos-animate",
                        "data-aos=fadeup",
                        "data-aos-delay=200",
                    ],
                ),
                rx.vstack(
                    hero_image(
                        alt="imagen con computadoras que demuestran tecnología",
                        img="img/hero-img.png",
                    ),
                    class_name=[
                        "col-lg-6",
                        "order-1",
                        "order-lg-2",
                        "hero-img",
                        "aos-init",
                        "aos-animate",
                        "data-aos=zoomin",
                        "data-aos-delay=200",
                    ],
                ),
                class_name="row",
            ),
            class_name="container",
            style=[styles.BASE_STYLE["#hero .container"]],
        ),
        style=[
            styles.BASE_STYLE["#hero"],
            styles.BASE_STYLE["section"],
        ],
        class_name=[
            "d-flex",
            "align-items-center",
        ],
    )
