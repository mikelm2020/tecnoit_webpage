import reflex as rx

import index.components.complex.accordion_button as accordion_button
import index.content.accordion_content as accordion_content


def testimonials_accordion():
    """Creates an accordion of client testimonials."""
    return rx.box(
        rx.box(
            accordion_button.accordion_button(
                onclick_function="toggleAccordion('client1')",
                logo_alt_text="TechInnovate Logo",
                logo_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/Y8xVUVcEveQJMafK1G6Vee0UISBokgfKeGkcBwpiFlrYip51E/out-0.webp",
                company_name="TechInnovate",
            ),
            accordion_content.accordion_content(
                content_id="client1",
                testimonial_text="\"ProConsult's strategic insights have been invaluable to our company's growth. Their expertise and dedication are unmatched.\"",
                author_info="John Smith, CEO of TechInnovate",
            ),
            margin_bottom="1rem",
        ),
        rx.box(
            accordion_button.accordion_button(
                onclick_function="toggleAccordion('client2')",
                logo_alt_text="GlobalTrade Logo",
                logo_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/uRapbQuCj5azIljcGpKo1gcWWC7g03Q5K995IGh5R1Uip51E/out-0.webp",
                company_name="GlobalTrade",
            ),
            accordion_content.accordion_content(
                content_id="client2",
                testimonial_text='"Working with ProConsult has transformed our operations. Their tailored solutions have significantly improved our efficiency."',
                author_info="Sarah Johnson, COO of GlobalTrade",
            ),
            margin_bottom="1rem",
        ),
        rx.box(
            accordion_button.accordion_button(
                onclick_function="toggleAccordion('client3')",
                logo_alt_text="EcoSolutions Logo",
                logo_src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/JiS4h0fbkcWLXiwpoApccCp7HuESqmYOMnGYA1vwfiQJmmXTA/out-0.webp",
                company_name="EcoSolutions",
            ),
            accordion_content.accordion_content(
                content_id="client3",
                testimonial_text='"ProConsult\'s innovative approach to sustainability consulting has helped us achieve our green goals while improving our bottom line."',
                author_info="Michael Green, Founder of EcoSolutions",
            ),
            margin_bottom="1rem",
        ),
        max_width="48rem",
        margin_left="auto",
        margin_right="auto",
    )
