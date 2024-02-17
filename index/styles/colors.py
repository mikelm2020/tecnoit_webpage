from enum import Enum


class Color(Enum):
    PRIMARY = "#14A1F0"
    SECONDARY = "#087ec4"
    BACKGROUND = "black"
    # BACKGROUND = "#000"
    CONTENT = "#171F26"
    ICON = "#47b2e4"
    COLLAPSED = "#37517e"


class TextColor(Enum):
    HEADER = "#F1F2F4"
    BODY = "#C3C7CB"
    CARD = "#444444"
    FOOTER = "#A3ABB2"
    MENU_OPTION = "#FFF"
    TITLE = "#FFF"
    SUBTITLE = "rgba(255,255,255,0.6)"


class BackGroundColor(Enum):
    HERO = "#37517e"
    HEADER = "rgba(40, 58, 90, 0.9)"
    ROW = "black"
