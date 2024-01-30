import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import BackGroundColor as BackGroundColor
from .colors import TextColor as TextColor
from .fonts import Font as Font, FontWeight, FontStyle, FontSize

# Constants
MAX_WIDTH = "600px"


# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


STYLESHEETS = [
    "hhtps://fonts.googleapis.com/css2?family=Open+Sans:wght@300;300i;400;400i;600;600i;700;700i&display=swap",
    "hhtps://fonts.googleapis.com/css2?family=Jost:wght@300;300i;400;400i;500;500i;600;600i;700;700i&display=swap",
    "hhtps://fonts.googleapis.com/css2?family=Poppins:wght@300;300i;400;400i;500;500i;600;600i;700;700i&display=swap",
    # "css/style.css",
    "vendor/aos/aos.css",
    "vendor/bootstrap/css/bootstrap.min.css",
    "vendor/bootstrap-icons/bootstrap-icons.css",
    "vendor/boxicons/css/boxicons.min.css",
    "vendor/glightbox/css/glightbox.min.css",
    "vendor/remixicon/remixicon.css",
    "vendor/swiper/swiper-bundle.min.css",
]

# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "font_style": FontStyle.NORMAL.value,
    "box_sizing": "border-box",
    "background_color": Color.BACKGROUND.value,
    rx.MenuButton: {
        "_hover": {
            "background_color": Color.SECONDARY.value,
        },
        "active_color": Color.SECONDARY.value,
    },
    # rx.Heading: {
    #     "size": "lg",
    #     "color": TextColor.HEADER.value,
    #     "font_family": Font.TITLE.value,
    #     "font_weight": FontWeight.MEDIUM.value,
    # },
    # rx.Button: {
    #     "width": "100%",
    #     "height": "100%",
    #     "padding": Size.SMALL.value,
    #     "border_radius": Size.DEFAULT.value,
    #     "color": TextColor.HEADER.value,
    #     "background_color": Color.CONTENT.value,
    #     "white_space": "normal",
    #     "text_align": "start",
    #     "_hover": {
    #         "background_color": Color.SECONDARY.value,
    #     },
    # },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {},
    },
}

header_style = dict(
    display="block",
    transition="all 0.5s",
    z_index="997",
    padding_top="15px 0",
)

fixed_top_style = dict(
    position="fixed",
    top="0px",
    right="0px",
    left="0px",
)

align_items_center_style = dict(
    align_items_center="center!important",
)

d_flex_style = dict(
    display="flex!important",
)

container_style = dict(
    display="block",
    width="100%",
    padding_right="0.75rem",
    padding_left="0.75rem",
    margin_right="auto",
    margin_left="auto",
    max_width=[
        "540px",
        "720px",
        "960px",
        "1140px",
    ],
)

hero_container_style = dict(
    padding_top="72px",
)

logo_href_style = dict(
    font_size="30px",
    margin_top="0",
    margin_bottom="0px",
    margin_left="0px",
    padding="0px",
    line_height="1",
    font_weight=FontWeight.MEDIUM.value,
    letter_spacing="2px",
    text_transform="uppercase",
)

me_auto_style = dict(
    margin_right="auto!important",
)


img_style = dict(
    overflow_clip_margin="content-box",
    overflow="clip",
    vertical_align="middle",
)

img_fluid_style = dict(
    max_width="100%",
    height="auto",
)

navbar_style = dict(
    padding="0",
    position="relative",
    display="flex",
    flex_wrap="wrap",
    align_items="center",
    justify_content="space-between",
)

ul_style = dict(
    margin_block_start="1em",
    margin_block_end="1em",
    margin_inline_start="0px",
    margin_inline_end="0px",
    padding_inline_start="40px",
)

navbar_ul_style = dict(
    margin="0",
    padding="0",
    display="flex",
    list_style="none",
    align_items="center",
)

navbar_menu_button_style = dict(
    padding="8px 20px",
    margin_left="30px",
    border_radius="50px",
    color=TextColor.MENU_OPTION.value,
    font_size="14px",
    border="2px solid #47b2e4",
    font_weight=FontWeight.SEMIBOLD.value,
)

section_style = dict(
    padding="60px 0",
    overflow="hidden",
    display="block",
)

hero_style = dict(
    width="100%",
    height="80vh",
    background_color=BackGroundColor.HERO.value,
)

row_style = dict(
    display="flex",
    flex_wrap="wrap",
    margin_top="0px",
    margin_right="-0.75rem",
    margin_left="-0.75rem",
    max_width="100%",
    padding_right="0.75rem",
    padding_left="0.75rem",
)

col_style = dict(
    flex="0 0 auto",
    width=["50%", "50%", "50%", "50%", "50%"],
)

flex_column_style = dict(
    flex_direction="column!important",
)

justify_content_center_style = dict(
    justify_content="center!important",
)

order_2_style = dict(
    order=[
        "2!important",
        "2!important",
        "2!important",
        "2!important",
        "2!important",
    ]
)

pt_4_style = dict(
    padding_top="1.5rem!important",
)

order_1_style = dict(
    order=[
        "1!important",
        "1!important",
        "1!important",
        "1!important",
        "1!important",
    ]
)

pt_style = dict(
    padding_top=[
        "0!important",
        "0!important",
        "0!important",
        "0!important",
        "0!important",
    ]
)

h1_style = dict(
    font_weight="500",
    font_size="2.5rem",
    display="block",
    margin_block_start="0.83em",
    margin_block_end="0.83em",
    margin_inline_start="0px",
    margin_inline_end="0px",
)

h1_hero_style = dict(
    margin="0 0 10px 0",
    font_family=Font.HERO.value,
    font_size=FontSize.BIG.value,
    font_weight=FontWeight.BOLD.value,
    line_height="56px",
    color=TextColor.TITLE.value,
)

h2_style = dict(
    font_weight="500",
    font_size="2rem",
    display="block",
    margin_top="0",
    line_height="1.2",
    margin_block_start="0.83em",
    margin_block_end="0.83em",
    margin_inline_start="0px",
    margin_inline_end="0px",
)

h2_hero_style = dict(
    font_family=Font.HERO.value,
    color=TextColor.SUBTITLE.value,
    margin_bottom="50px",
    font_size=FontSize.REGULAR.value,
    font_weight=FontWeight.MEDIUM.value,
)

hero_img_style = dict(
    width="100%",
)

hero_container = dict(
    padding_top="72px",
)

animated_style = dict(
    animation="up-down 2s ease-in-out infinite alternate-reverse both",
)

aos_animate_style = dict(
    opacity="1",
    transform="translateZ(0) scale(1)",
    transition_delay=".2s",
    pointer_events="auto",
)

data_aos_fade_up_style = dict(
    transform="translate3d(0,100px,0)",
)

data_aos_delay_style = dict(
    transition_delay="0s",
)

data_aos_zoom_in_style = dict(
    transition_property="opacity,transform,-webkit-transform",
)

main_style = dict(
    display="block",
)

clients_style = dict(
    padding="12px 0",
    text_align="center",
)

section_bg = dict(
    background_color="black",
)


col_2_style = dict(
    flex="0 0 auto",
    width=[
        "30%",
        "30%",
        "30%",
        "30%",
        "30%",
    ],
)

col_4_style = dict(
    flex="0 0 auto",
    width=[
        "10%",
        "10%",
        "10%",
        "10%",
        "10%",
    ],
)

clients_img_style = dict(
    max_width="60%",
    transition="all 0.4s ease-in-out",
    display="inline-block",
    padding="15px 0",
)

section_title_style = dict(
    display="block",
    text_align="center",
    padding_bottom="30px",
)

h2_section_title_text_style = dict(
    font_family=Font.SECTION_TITLE.value,
    color=TextColor.TITLE.value,
    font_size=FontSize.MEDIUM.value,
    font_weight=FontWeight.BOLD.value,
    text_transform="uppercase",
    margin_bottom="20px",
    padding_bottom="20px",
    position="relative",
)

parragraph_text_style = dict(
    margin_top="0",
    margin_bottom="1rem",
    display="block",
    margin_block_start="1em",
    margin_block_end="1em",
    margin_inline_start="0px",
    margin_inline_end="0px",
    color=TextColor.BODY.value,
)

list_unordered_style = dict(
    list_style="none",
    padding="0",
    margin_top="0",
    margin_bottom="1rem",
    display="block",
    margin_block_start="1em",
    margin_block_start_end="1em",
    margin_inline_start="0px",
    margin_inline_end="0px",
    padding_inline_start="40px",
)

list_item_unordered_style = dict(
    padding_left="20px",
    position="relative",
    display="list-item",
    text_align="left",
    left="0",
    top="2px",
    color=TextColor.BODY.value,
    line_height="1",
    font_style=FontStyle.NORMAL.value,
)

services_col_style = dict(
    flex="0 0 auto",
    width=["50%", "50%", "50%", "25%", "25%"],
    # pointer_events="auto",
    # opacity="1",
    # transform="translateZ(0) scale(1)",
    # transition_delay=".1s",
    # transition_property="opacity,transform, -webkit-transform",
    # transition_timing_function="ease-in-out",
    # transition_duration="1s",
)

align_items_stretch_style = dict(
    align_items="stretch!important",
)

services_icon_box_style = dict(
    # box_shadow="0px 0 25px 0 rgba(0,0,0,0.1)",
    box_shadow="0px 0 25px 0 rgba(255,255,55,0.5)",
    padding="50px 30px",
    transition="all ease-in-out 0.4s",
    background="#000",
    display="block",
)

service_icon_container_style = dict(
    margin_bottom="10px",
    display="block",
)

sevice_icon_style = dict(
    color="#47b2e4",
    font_size="36px",
    transition="0.3s",
    font_family="boxicons!important",
    font_weight=FontWeight.REGULAR.value,
    font_style=FontStyle.NORMAL.value,
    font_variant="normal",
    line_height="1",
    text_rendering="auto",
    display="inline-block",
    text_transform="none",
    speak="none",
)

h4_style = dict(
    display="block",
    margin_block_start="1.33em",
    margin_block_end="1.33em",
    margin_inline_start="0px",
    margin_inline_end="0px",
    margin_top="0",
    line_height="1.2",
    color=TextColor.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    margin_bottom="15px",
    font_size=FontSize.REGULAR.value,
)

link_style = dict(
    color=Color.SECONDARY.value,
    transition="ease-in-out 0.3s",
    text_decoration="none",
    box_sizing="border-box",
    cursor="pointer",
)

service_parragraph_style = dict(
    line_height="24px",
    font_size="14px",
    margin_bottom="0",
    color=TextColor.CARD.value,
)

mt_4_style = dict(
    margin_top="1.5rem",
)

mt_md_0_style = dict(
    margin_top="0!important",
)

mt_xl_0_style = dict(
    margin_top="0!important",
)
