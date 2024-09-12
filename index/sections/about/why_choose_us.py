import reflex as rx

import index.components.complex.feature_box as feature_box
import index.components.main_heading as main_heading


def why_choose_us_section():
    """Creates the 'Why Choose Us' section with features grid."""
    return rx.box(
        main_heading.main_heading(heading_text="Why Choose Us"),
        rx.box(
            feature_box.feature_box(
                icon_alt_text="Experience",
                icon_tag="award",
                heading_text="20+ Years Experience",
                description_text="Decades of industry expertise",
            ),
            feature_box.feature_box(
                icon_alt_text="Clients",
                icon_tag="users",
                heading_text="500+ Satisfied Clients",
                description_text="Trusted by industry leaders",
            ),
            feature_box.feature_box(
                icon_alt_text="Success",
                icon_tag="circle_check_big",
                heading_text="98% Success Rate",
                description_text="Proven track record of success",
            ),
            feature_box.feature_box(
                icon_alt_text="Global",
                icon_tag="globe",
                heading_text="Global Reach",
                description_text="Serving clients worldwide",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                    "1024px": "repeat(4, minmax(0, 1fr))",
                }
            ),
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
    )
