import reflex as rx
import index.styles.styles as styles
import index.constants as constants


def faq() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.vstack(
            rx.chakra.vstack(
                rx.chakra.heading(
                    constants.FAQ_TITLE,
                    size="lg",
                    color="white",
                    style=[
                        styles.h2_style,
                        styles.h2_section_title_text_style,
                    ],
                ),
                rx.chakra.text(
                    constants.FAQ_CONTENT,
                    style=styles.parragraph_text_style,
                ),
                style=styles.section_title_style,
            ),
            rx.chakra.vstack(
                rx.chakra.accordion(
                    rx.chakra.accordion_item(
                        rx.chakra.accordion_button(
                            rx.chakra.icon(
                                tag="question",
                                style=[
                                    styles.bx_style,
                                ],
                            ),
                            rx.chakra.heading(
                                constants.ASK_ITEM_1,
                                style=styles.link_faq_list_style,
                            ),
                            rx.chakra.accordion_icon(),
                        ),
                        rx.chakra.accordion_panel(
                            rx.chakra.text(
                                constants.ANSWER_ITEM_1,
                                style=styles.parragraph_text_style,
                            ),
                        ),
                    ),
                    rx.chakra.accordion_item(
                        rx.chakra.accordion_button(
                            rx.chakra.icon(
                                tag="question",
                                style=[
                                    styles.bx_style,
                                ],
                            ),
                            rx.chakra.heading(
                                constants.ASK_ITEM_2,
                                style=styles.link_faq_list_style,
                            ),
                            rx.chakra.accordion_icon(),
                        ),
                        rx.chakra.accordion_panel(
                            rx.chakra.text(
                                constants.ANSWER_ITEM_2,
                                style=styles.parragraph_text_style,
                            ),
                        ),
                    ),
                    rx.chakra.accordion_item(
                        rx.chakra.accordion_button(
                            rx.chakra.icon(
                                tag="question",
                                style=[
                                    styles.bx_style,
                                ],
                            ),
                            rx.chakra.heading(
                                constants.ASK_ITEM_3,
                                style=styles.link_faq_list_style,
                            ),
                            rx.chakra.accordion_icon(),
                        ),
                        rx.chakra.accordion_panel(
                            rx.chakra.text(
                                constants.ANSWER_ITEM_3,
                                style=styles.parragraph_text_style,
                            ),
                        ),
                    ),
                    rx.chakra.accordion_item(
                        rx.chakra.accordion_button(
                            rx.chakra.icon(
                                tag="question",
                                style=[
                                    styles.bx_style,
                                ],
                            ),
                            rx.chakra.heading(
                                constants.ASK_ITEM_4,
                                style=styles.link_faq_list_style,
                            ),
                            rx.chakra.accordion_icon(),
                        ),
                        rx.chakra.accordion_panel(
                            rx.chakra.text(
                                constants.ANSWER_ITEM_4,
                                style=styles.parragraph_text_style,
                            ),
                        ),
                    ),
                    rx.chakra.accordion_item(
                        rx.chakra.accordion_button(
                            rx.chakra.icon(
                                tag="question",
                                style=[
                                    styles.bx_style,
                                ],
                            ),
                            rx.chakra.heading(
                                constants.ASK_ITEM_5,
                                style=styles.link_faq_list_style,
                            ),
                            rx.chakra.accordion_icon(),
                        ),
                        rx.chakra.accordion_panel(
                            rx.chakra.text(
                                constants.ANSWER_ITEM_5,
                                style=styles.parragraph_text_style,
                            ),
                        ),
                    ),
                    rx.chakra.accordion_item(
                        rx.chakra.accordion_button(
                            rx.chakra.icon(
                                tag="question",
                                style=[
                                    styles.bx_style,
                                ],
                            ),
                            rx.chakra.heading(
                                constants.ASK_ITEM_6,
                                style=styles.link_faq_list_style,
                            ),
                            rx.chakra.accordion_icon(),
                        ),
                        rx.chakra.accordion_panel(
                            rx.chakra.text(
                                constants.ANSWER_ITEM_6,
                                style=styles.parragraph_text_style,
                            ),
                        ),
                    ),
                    rx.chakra.accordion_item(
                        rx.chakra.accordion_button(
                            rx.chakra.icon(
                                tag="question",
                                style=[
                                    styles.bx_style,
                                ],
                            ),
                            rx.chakra.heading(
                                constants.ASK_ITEM_7,
                                style=styles.link_faq_list_style,
                            ),
                            rx.chakra.accordion_icon(),
                        ),
                        rx.chakra.accordion_panel(
                            rx.chakra.text(
                                constants.ANSWER_ITEM_7,
                                style=styles.parragraph_text_style,
                            ),
                        ),
                    ),
                    rx.chakra.accordion_item(
                        rx.chakra.accordion_button(
                            rx.chakra.icon(
                                tag="question",
                                style=[
                                    styles.bx_style,
                                ],
                            ),
                            rx.chakra.heading(
                                constants.ASK_ITEM_8,
                                style=styles.link_faq_list_style,
                            ),
                            rx.chakra.accordion_icon(),
                        ),
                        rx.chakra.accordion_panel(
                            rx.chakra.text(
                                constants.ANSWER_ITEM_8,
                                style=styles.parragraph_text_style,
                            ),
                        ),
                    ),
                    rx.chakra.accordion_item(
                        rx.chakra.accordion_button(
                            rx.chakra.icon(
                                tag="question",
                                style=[
                                    styles.bx_style,
                                ],
                            ),
                            rx.chakra.heading(
                                constants.ASK_ITEM_9,
                                style=styles.link_faq_list_style,
                            ),
                            rx.chakra.accordion_icon(),
                        ),
                        rx.chakra.accordion_panel(
                            rx.chakra.text(
                                constants.ANSWER_ITEM_9,
                                style=styles.parragraph_text_style,
                            ),
                        ),
                    ),
                    rx.chakra.accordion_item(
                        rx.chakra.accordion_button(
                            rx.chakra.icon(
                                tag="question",
                                style=[
                                    styles.bx_style,
                                ],
                            ),
                            rx.chakra.heading(
                                constants.ASK_ITEM_10,
                                style=styles.link_faq_list_style,
                            ),
                            rx.chakra.accordion_icon(),
                        ),
                        rx.chakra.accordion_panel(
                            rx.chakra.text(
                                constants.ANSWER_ITEM_10,
                                style=styles.parragraph_text_style,
                            ),
                        ),
                    ),
                    allow_multiple=True,
                    bg="rgba(40, 58, 90, 0.9)",
                    color="white",
                    width="100%",
                ),
                styles=[
                    styles.faq_list_style,
                ],
            ),
            style=[
                styles.container_style,
            ],
        ),
        style=[
            styles.section_style,
        ],
    )
