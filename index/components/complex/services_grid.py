import reflex as rx

import index.components.feature_description as feature_description
import index.components.feature_heading as feature_heading
import index.components.feature_icon as feature_icon
import index.components.learn_more_link as learn_more_link


def services_grid():
    """Creates a grid of service offerings."""
    return rx.box(
        rx.box(
            feature_icon.feature_icon(
                icon_alt_text="Strategy",
                icon_tag="briefcase",
            ),
            feature_heading.feature_heading(heading_text="Strategic Planning"),
            feature_description.feature_description(
                description_text="Develop comprehensive strategies to drive your business forward"
            ),
            learn_more_link.learn_more_link(link_url="/services/strategic-planning"),
            class_name="dark:bg-gray-700",
            background_color="#F3F4F6",
            padding="1.5rem",
            border_radius="0.5rem",
        ),
        rx.box(
            feature_icon.feature_icon(
                icon_alt_text="Performance",
                icon_tag="trending-up",
            ),
            feature_heading.feature_heading(heading_text="Performance Optimization"),
            feature_description.feature_description(
                description_text="Improve operational efficiency and maximize your organization's potential"
            ),
            learn_more_link.learn_more_link(
                link_url="/services/performance-optimization"
            ),
            class_name="dark:bg-gray-700",
            background_color="#F3F4F6",
            padding="1.5rem",
            border_radius="0.5rem",
        ),
        rx.box(
            feature_icon.feature_icon(icon_alt_text="Leadership", icon_tag="users"),
            feature_heading.feature_heading(heading_text="Leadership Development"),
            feature_description.feature_description(
                description_text="Nurture and empower your leaders to drive sustainable growth"
            ),
            learn_more_link.learn_more_link(
                link_url="/services/leadership-development"
            ),
            class_name="dark:bg-gray-700",
            background_color="#F3F4F6",
            padding="1.5rem",
            border_radius="0.5rem",
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(3, minmax(0, 1fr))",
            }
        ),
    )
