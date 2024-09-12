import reflex as rx

import index.components.complex.client_logo as client_logo


def client_logos_container():
    """Create a container for multiple client logos with overflow handling."""
    return rx.box(
        rx.flex(
            client_logo.client_logo(
                logo_alt_text="Client 1 logo",
                logo_source="https://replicate.delivery/yhqm/SYL4WH7zBR7hCh5OtjzxQnR4Rmnde13dsqQLaO3NxEHZXzrJA/out-0.webp",
            ),
            client_logo.client_logo(
                logo_alt_text="Client 2 logo",
                logo_source="https://replicate.delivery/yhqm/ka9ieoGBXYzsUCjJ6uBbT6ZFtQghEOIjikUIlrvRQvFZXzrJA/out-0.webp",
            ),
            client_logo.client_logo(
                logo_alt_text="Client 3 logo",
                logo_source="https://replicate.delivery/yhqm/Q4xKV0sFerxoLa79JrzcgC74zpRwTyVQQCb8CtghyTBZXzrJA/out-0.webp",
            ),
            client_logo.client_logo(
                logo_alt_text="Client 4 logo",
                logo_source="https://replicate.delivery/yhqm/wOGiM8QW53amA5qOIdaqyyrgxCIKFRQfSCKtimdv5ZXZXzrJA/out-0.webp",
            ),
            client_logo.client_logo(
                logo_alt_text="Client 5 logo",
                logo_source="https://replicate.delivery/yhqm/ZVy3pSzLwHqeeUCUY3Om3Bxy1MIq2J7Jp6KDbBGj8CIyumXTA/out-0.webp",
            ),
            display="flex",
            align_items="center",
            justify_content="center",
            column_gap="2rem",
        ),
        overflow="hidden",
    )
