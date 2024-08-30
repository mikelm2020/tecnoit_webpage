import reflex as rx

import index.components.bold_span as bold_span
import index.components.logo_image as logo_image


def logo_with_text(logo_alt_text, logo_src, company_name):
    """Creates a flex container with a logo and company name."""
    return rx.flex(
        logo_image.logo_image(image_alt_text=logo_alt_text, image_src=logo_src),
        bold_span.bold_span(span_text=company_name),
        display="flex",
        align_items="center",
    )
