from enum import Enum


class Font(Enum):
    DEFAULT = ["Open Sans", "sans-serif"]
    TITLE = "Poppins"
    LOGO = "Comfortaa"
    HERO = ["Jost", "sans-serif"]
    SECTION_TITLE = ["Jost", "sans-serif"]


class FontWeight(Enum):
    LIGHT = "300"
    REGULAR = "400"
    MEDIUM = "500"
    SEMIBOLD = "600"
    BOLD = "700"


class FontStyle(Enum):
    NORMAL = "normal"
    ITALIC = "italic"


class FontSize(Enum):
    BIG = "48px"
    MEDIUM = "32px"
    REGULAR = "24px"
    NORMAL = "20px"
