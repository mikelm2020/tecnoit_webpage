import reflex as rx
from index.views.customers.customers import customers
from index.views.about.about import about
from index.views.services.services import services
from index.views.faq.faq import faq
import index.styles.styles as styles


def main() -> rx.Component:
    return rx.vstack(
        customers(),
        about(),
        services(),
        faq(),
        style=styles.main_style,
    )
