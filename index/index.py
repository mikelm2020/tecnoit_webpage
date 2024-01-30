import reflex as rx
from index.components.navbar import navbar
from index.views.footer.footer import footer
from index.views.header.header import header
from index.views.hero.hero import hero
from index.views.main.main import main
import index.styles.styles as styles
from index.styles.styles import Size as Size
from index.styles.colors import Color

# class State(rx.State):
#     pass


def index() -> rx.Component:
    return rx.vstack(
        header(),
        hero(),
        main(),
        # rx.center(
        #     rx.vstack(
        #         header(),
        #         max_width=styles.MAX_WIDTH,
        #         width="100%",
        #         margin_y=Size.BIG.value,
        #         padding=Size.BIG.value,
        #     ),
        # ),
        # footer(),
        # background_color=Color.BACKGROUND.value,
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="Tecnoit | Tecnología para las MicroPyMes",
    description="Tecnoit es una empresa con 11 años de experiencia para ofrecer tecnología a las Micro, pequeñas y medianas empresas de la Ciudad de México ",
)
# app.compile()
