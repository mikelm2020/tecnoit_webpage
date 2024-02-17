import reflex as rx
from index.views.customers.customers import customers
from index.views.about.about import about
from index.views.services.services import services
from index.views.faq.faq import faq
from index.views.contact.contact import contact
import index.styles.styles as styles


def main() -> rx.Component:
    return rx.chakra.vstack(
        customers(),
        about(),
        services(),
        faq(),
        contact(),
        style=styles.main_style,
    )
