import reflex as rx

import index.components.complex.footer_list_item as footer_list_item
import index.components.complex.social_media_link as social_media_link
import index.components.section_heading as section_heading
import index.sections.footer.footer_contact_info as footer_contact_info


def footer_content():
    """Creates the main content of the footer including company info, quick links, contact info, and social media links."""
    return rx.flex(
        rx.box(
            section_heading.section_heading(heading_text="ProConsult"),
            rx.text(
                "Empowering businesses through expert consulting services",
                color="#9CA3AF",
            ),
            margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        rx.box(
            section_heading.section_heading(heading_text="Quick Links"),
            rx.list(
                footer_list_item.footer_list_item(link_text="Home"),
                footer_list_item.footer_list_item(link_text="Services"),
                footer_list_item.footer_list_item(link_text="About Us"),
                footer_list_item.footer_list_item(link_text="Contact"),
                color="#9CA3AF",
            ),
            margin_bottom=rx.breakpoints({"0px": "1.5rem", "768px": "0"}),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        footer_contact_info.footer_contact_info(),
        rx.box(
            section_heading.section_heading(heading_text="Follow Us"),
            rx.flex(
                social_media_link.social_media_link(
                    icon_alt_text="LinkedIn",
                    icon_tag="linkedin",
                ),
                social_media_link.social_media_link(
                    icon_alt_text="Twitter",
                    icon_tag="twitter",
                ),
                social_media_link.social_media_link(
                    icon_alt_text="Facebook",
                    icon_tag="facebook",
                ),
                display="flex",
                column_gap="1rem",
            ),
            width=rx.breakpoints({"0px": "100%", "768px": "25%"}),
        ),
        display="flex",
        flex_wrap="wrap",
        justify_content="space-between",
    )
