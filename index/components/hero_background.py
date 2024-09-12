import reflex as rx


def hero_background():
    """Creates the background image for the hero section."""
    return rx.box(
        rx.image(
            alt="Professional consultants working together in a modern office, discussing strategies and analyzing data on digital screens",
            src="https://replicate.delivery/yhqm/c949NRFLbL69Dlfc2wdIAQorGB7SzzxYCvE08yEvbh4R1zrJA/out-0.webp",
            height="100%",
            object_fit="cover",
            opacity="0.3",
            width="100%",
        ),
        position="absolute",
        top="0",
        right="0",
        bottom="0",
        left="0",
        z_index="0",
    )
