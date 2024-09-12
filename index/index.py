import reflex as rx

import index.layout.page_layout as page_layout


def index() -> rx.Component:
    return rx.box(
        page_layout.page_layout(),
    )


app = rx.App(
    # stylesheets=styles.STYLESHEETS,
    # style=styles.BASE_STYLE,
    # theme=rx.theme(
    #     appearance="dark",
    #     has_background=True,
    # ),
)
app.add_page(
    index,
    title="Tecnoit | Tecnología para las MicroPyMes",
    description="Tecnoit es una empresa con 11 años de experiencia para ofrecer tecnología a las Micro, pequeñas y medianas empresas de la Ciudad de México ",
)
# app.compile()
