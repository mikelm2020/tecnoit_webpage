import reflex as rx

# import index.styles.styles as styles
# from index.components.logo import logo
# from index.components.navbar import navbar
# from index.styles.colors import Color as Color
# from index.styles.colors import TextColor as TextColor
# from index.styles.styles import Size as Size


def header() -> rx.Component:
    """
    Returns a Reflex component that represents the header of the website.

    The header consists of a logo, a navigation bar, and an avatar with the user's information. The logo is a heading with the text "Tecnoit", and the navigation bar contains links to the user's social media profiles. The avatar includes the user's name, username, and links to their social media profiles. The user's information includes their experience in years, their occupation, and a short bio.

    Args:
        None

    Returns:
        A Reflex component that represents the header of the website.

    """
    return rx.vstack(
        rx.box(
            class_name="bg-slate-500",
        ),
        rx.box(),
        rx.box(),
    )
    # return rx.hstack(
    #     rx.flex(
    #         logo(
    #             "Logo de la empresa Tecnoit",
    #             "logo.png",
    #             "http://localhost:3000/",
    #         ),
    #         # rx.spacer(),
    #         navbar(),
    #         class_name=[
    #             "container",
    #             "d-flex",
    #             "align-items-center",
    #         ],
    #         # style=[
    #         #     styles.container_style,
    #         #     styles.d_flex_style,
    #         #     styles.align_items_center_style,
    #         # ],
    #     ),
    #     class_name="fixed-top",
    #     style=[
    #         styles.BASE_STYLE["#header"],
    #         styles.BASE_STYLE["#header.header-scrolled,#header.header-inner-pages"],
    #     ],
    #     # style=[
    #     #     styles.header_style,
    #     #     styles.fixed_top_style,
    #     # ],
    # )
