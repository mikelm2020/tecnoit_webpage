from enum import Enum


class Font(Enum):
    DEFAULT = ["Source Sans Pro", "sans-serif"]
    TIPOGRAPHY = ["Jost", "sans-serif"]
    TITLE = "Poppins"
    LOGO = "Comfortaa"
    HERO = ["Jost", "sans-serif"]
    SECTION_TITLE = ["Jost", "sans-serif"]
    ICON = "boxIcons!Important"
    LINK = "Poppins"
    CONTENT = ["Poppins", "sans-serif"]
    FOOTER = ["Jost", "sans-serif"]


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
    MEDIUM_BIG = "40px"
    MEDIUM_REGULAR = "36px"
    MEDIUM = "32px"
    REGULAR_VERY_BIG = "28px"
    REGULAR_BIG = "26px"
    REGULAR = "24px"
    INTER = "22px"
    NORMAL = "20px"
    SMALL_MEDIUM = "18px"
    SMALL = "16px"
    VERY_SMALL = "14px"
    TINY = "12px"


class FontVariant(Enum):
    NORMAL = "normal"
