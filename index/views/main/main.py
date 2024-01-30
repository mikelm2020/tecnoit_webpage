import reflex as rx
from index.views.customers.customers import customers
from index.views.about.about import about
from index.views.services.services import services
import index.styles.styles as styles


def main() -> rx.Component:
    return rx.vstack(
        customers(),
        about(),
        services(),
        style=styles.main_style,
    )
