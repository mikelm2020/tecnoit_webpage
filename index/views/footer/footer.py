import reflex as rx
import datetime
import index.constants as const
from index.styles.styles import Size as Size
from index.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            height=Size.VERY_BIG.value,
            weight=Size.VERY_BIG.value,
            alt='Logotipo de MoureDev. Una "eme" entre llaves.',
        ),
        rx.link(
            f"© 2014-{datetime.date.today().year} MoureDev by Brais Moure v3.",
            href=const.MOUREDEV_URL,
            is_external=True,
            font_size=Size.MEDIUM.value,
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value,
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value,
    )
