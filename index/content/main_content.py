import reflex as rx

import index.components.hero_background as hero_background
import index.content.hero_content as hero_content
import index.sections.about.why_choose_us as why_choose_us_section
import index.sections.contact.contact_section as contact_section
import index.sections.services.services_section as services_section
import index.sections.trusted_clients.trusted_clients_section as trusted_clients_section
from index.styles.colors import Color, DarkMode


def main_content():
    """Creates the main content of the page including all sections."""
    return rx.box(
        rx.box(
            hero_background.hero_background(),
            hero_content.hero_content(),
            class_name="dark:bg-blue-800",
            # background_color="2563EB",
            background_color=DarkMode.SECOND.value,
            padding_top="5rem",
            padding_bottom="5rem",
            position="relative",
            color="#ffffff",
        ),
        services_section.services_section(),
        rx.box(
            why_choose_us_section.why_choose_us_section(),
            class_name="dark:bg-gray-900",
            # background_color="F3F4F6",
            background_color=Color.BACKGROUND.value,
            padding_top="4rem",
            padding_bottom="4rem",
        ),
        rx.box(
            trusted_clients_section.trusted_clients_section(),
            class_name="dark:bg-gray-800",
            # background_color="ffffff",
            background_color=Color.BACKGROUND.value,
            padding_top="4rem",
            padding_bottom="4rem",
        ),
        # testimonials_section.testimonials_section(),
        # rx.box(
        #     cta_section.cta_section(),
        #     class_name="dark:bg-blue-800",
        #     background_color="#2563EB",
        #     padding_top="4rem",
        #     padding_bottom="4rem",
        #     color="#ffffff",
        # ),
        rx.box(
            contact_section.contact_section(),
            class_name="dark:bg-gray-800",
            # background_color="ffffff",
            background_color=Color.BACKGROUND.value,
            padding_top="4rem",
            padding_bottom="4rem",
        ),
    )
