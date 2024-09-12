import reflex as rx

import index.components.stylesheet_link as stylesheet_link
import index.content.main_content as main_content
import index.sections.footer.footer as footer
import index.sections.header.header as header
from index.styles.colors import Color


def page_layout():
    """Creates the overall page layout including styles, scripts, header, main content, and footer."""
    return rx.fragment(
        stylesheet_link.stylesheet_link(
            stylesheet_url="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
        ),
        stylesheet_link.stylesheet_link(
            stylesheet_url="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
        ),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
    """
        ),
        rx.script(
            """
        function toggleDarkMode() {
            document.documentElement.classList.toggle('dark');
        }
        function toggleAccordion(id) {
            const content = document.getElementById(id);
            content.classList.toggle('hidden');
        }
    """
        ),
        rx.box(
            header.header(),
            main_content.main_content(),
            footer.footer(),
            class_name="dark:bg-gray-900 font-['Poppins']",
            background_color=Color.BACKGROUND.value,
            transition_duration="300ms",
            transition_property="color, background-color, border-color, text-decoration-color, fill, stroke",
            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        ),
    )
