from enum import Enum

from .colors import BackGroundColor as BackGroundColor
from .colors import Color as Color
from .colors import DarkMode as DarkMode
from .colors import ElementColor as ElementColor
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontSize, FontStyle, FontWeight  # noqa: F401

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
    "https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700",
    # "/css/style.css",
    # "/vendor/bootstrap/css/bootstrap.css",
    # "/vendor/bootstrap/css/bootstrap-utilities.css",
    # "/vendor/aos/aos.css",
    # "/vendor/bootstrap/css/bootstrap.min.css",
    # "/vendor/bootstrap-icons/bootstrap-icons.css",
    # "/vendor/boxicons/css/boxicons.min.css",
    # "/vendor/glightbox/css/glightbox.min.css",
    # "/vendor/remixicon/remixicon.css",
    # "/vendor/swiper/swiper-bundle.min.css",
]

# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    # "font_weight": FontWeight.LIGHT.value,
    # "font_style": FontStyle.NORMAL.value,
    # "box_sizing": "border_box",
    # "background_color": Color.BACKGROUND.value,
    # Componentes default:
}

gradient = dict(
    background="linear-gradient(90deg, rgba(20,161,240,1) 0%, rgba(8,126,196,1) 100%)"
    # background = "linear-gradient90deg, #d53369 0%, #daae51 100%)"
)
