import reflex as rx

import index.styles.styles as styles
from index.views.about.about import about
from index.views.contact.contact import contact
from index.views.customers.customers import customers
from index.views.faq.faq import faq
from index.views.services.services import services


def main() -> rx.Component:
    return rx.vstack(
        customers(),
        about(),
        services(),
        faq(),
        contact(),
        style=styles.main_style,
    )
