from enum import Enum

import reflex as rx

from .colors import BackGroundColor as BackGroundColor
from .colors import Color as Color
from .colors import DarkMode as DarkMode
from .colors import ElementColor as ElementColor
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontSize, FontStyle, FontWeight

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
    "https://fonts.googleapis.com/css2?family=Open+Sans:wght@300,300i,400,400i,600,600i,700,700i&display=swap",
    "https://fonts.googleapis.com/css2?family=Jost:wght@300,300i,400,400i,500,500i,600,600i,700,700i&display=swap",
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300,300i,400,400i,500,500i,600,600i,700,700i&display=swap",
    "/css/style.css",
    "/vendor/bootstrap/css/bootstrap.css",
    "/vendor/bootstrap/css/bootstrap-utilities.css",
    "/vendor/aos/aos.css",
    "/vendor/bootstrap/css/bootstrap.min.css",
    "/vendor/bootstrap-icons/bootstrap-icons.css",
    "/vendor/boxicons/css/boxicons.min.css",
    "/vendor/glightbox/css/glightbox.min.css",
    "/vendor/remixicon/remixicon.css",
    "/vendor/swiper/swiper-bundle.min.css",
]

# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "font_style": FontStyle.NORMAL.value,
    "box_sizing": "border_box",
    "background_color": Color.BACKGROUND.value,
    # Componentes default:
    rx.menu.root: {
        "margin_block_start": "1em",
        "margin_block_end": "1em",
        "margin_inline_start": "0px",
        "margin_inline_end": "0px",
        "padding_inline_start": "40px",
    },
    rx.link: {
        "_hover": {
            "text_decoration": "none",
        },
        "color": ElementColor.A.value,
        "text_decoration": "none",
    },
    # General
    "body": {
        "font_family": Font.DEFAULT.value,
        "color": Color.PRIMARY.value,
    },
    rx.heading: {
        "font_family": Font.TIPOGRAPHY.value,
    },
    # encabezados
    "h1,h2,h3,h4,h5,h6": {
        "font_family": Font.TIPOGRAPHY.value,
    },
    # Preloader
    "#preloader": {
        "position": "fixed",
        "top": "0",
        "left": "0",
        "right": "0",
        "bottom": "0",
        "z_index": "9999",
        "overflow": "hidden",
        "background": ElementColor.PRELOADER.value,
    },
    "#preloader:before": {
        "content": None,
        "position": "fixed",
        "top": "calc(50% _ 30px)",
        "left": "calc(50% _ 30px)",
        "border": "6px solid  #37517e",
        "border_top_color": "#fff",
        "border_bottom_color": "#fff",
        "order_radius": "50%",
        "width": "60px",
        "height": "60px",
        # "animation": "animate_preloader 1s linear infinite",
    },
    # Header
    "#header": {
        "transition": "all 0.5s",
        "z_index": "997",
        "padding": "15px 0",
        "background": DarkMode.SECOND.value,
    },
    "#header.header-scrolled,#header.header-inner-pages": {
        "background": "rgba(40, 58, 90, 0.9)",
    },
    "#header .logo": {
        "font_size": "30px",
        "margin": "0",
        "padding": "0",
        "line_height": "1",
        "font_weight": "500",
        "letter_spacing": "2px",
        "text_transform": "uppercase",
    },
    "#header .logo a": {
        "color": "#fff",
    },
    "#header .logo img": {
        # "max_height": "40px"
        "max_height": "40px",
    },
    # Navbar
    # Navigation Menu
    # Desktop navigation
    ".navbar": {
        "padding": "0",
    },
    ".navbar ul": {
        "margin": "0",
        "padding": "0",
        "display": "flex",
        "list_style": "none",
        "align_items": "center",
    },
    ".navbar li": {
        "position": "relative",
    },
    ".navbar a,.navbar a:focus": {
        "display": "flex",
        "align_items": "center",
        "justify_content": "space-between",
        "padding": "10px 0 10px 30px",
        "font_size": "15px",
        "font_weight": FontWeight.MEDIUM.value,
        "color": "#fff",
        "white_space": "nowrap",
        "transition": "0.3s",
    },
    ".navbar a i,.navbar a:focus i": {
        "font_size": "12px",
        "line_height": "0",
        "margin_left": "5px",
    },
    ".navbar a:hover,.navbar .active,.navbar .active:focus,.navbar li:hover>a": {
        "color": "#47b2e4",
    },
    ".navbar .getstarted,.navbar .getstarted:focus": {
        "padding": "8px 20px",
        "margin_left": "30px",
        "border_radius": "50px",
        "color": "#fff",
        "font_size": FontSize.VERY_SMALL.value,
        "border": "2px solid #47b2e4",
        "font_weight": FontWeight.SEMIBOLD.value,
    },
    ".navbar .getstarted:hover,.navbar .getstarted:focus:hover": {
        "color": "#fff",
        "background": "#31a9e1",
    },
    ".navbar .dropdown ul": {
        "display": "block",
        "position": "absolute",
        "left": "14px",
        "top": "calc(100% + 30px)",
        "margin": "0",
        "padding": "10px 0",
        "z_index": "99",
        "opacity": "0",
        "visibility": "hidden",
        "background": Color.BACKGROUND.value,
        "box_shadow": "0px 0px 30px rgba(127, 137, 161, 0.25)",
        "transition": "0.3s",
        "border_radius": "4px",
    },
    ".navbar .dropdown ul li": {
        "min_width": "200px",
    },
    ".navbar .dropdown ul a": {
        "padding": "10px 20px",
        "font_size": FontSize.VERY_SMALL.value,
        "text_transform": "none",
        "font_weight": FontWeight.MEDIUM.value,
        "color": "#0c3c53",
    },
    ".navbar .dropdown ul a i": {
        "font_size": FontSize.TINY.value,
    },
    ".navbar .dropdown ul a:hover,.navbar .dropdown ul .active:hover,.navbar .dropdown ul li:hover>a": {
        "color": "#47b2e4",
    },
    ".navbar .dropdown:hover>ul": {
        "opacity": "1",
        "top": "100%",
        "visibility": "visible",
    },
    ".navbar .dropdown .dropdown ul": {
        "top": "0",
        "left": "calc(100% - 30px)",
        "visibility": "hidden",
    },
    ".navbar .dropdown .dropdown:hover>ul": {
        "opacity": "1",
        "top": "0",
        "left": "100%",
        "visibility": "visible",
    },
    # @media (max-width: 1366px) {
    # .navbar .dropdown .dropdown ul {
    #     left: -90%,
    # }
    # .navbar .dropdown .dropdown:hover>ul {
    #     left: -100%,
    # }
    # }
    # Hero Section
    "#hero": {
        "width": "100%",
        "height": "80vh",
        "background": "#37517e",
    },
    "#hero .container": {
        "padding_top": "72px",
    },
    "#hero h1": {
        "margin": "0 0 10px 0",
        "font_size": FontSize.BIG.value,
        "font_weight": FontWeight.BOLD.value,
        "line_height": "56px",
        "color": "#fff",
    },
    "#hero h2": {
        "color": "rgba(255, 255, 255, 0.6)",
        "margin_bottom": "50px",
        "font_size": FontSize.REGULAR.value,
    },
    "#hero .btn-get-started": {
        "font_family": Font.HERO.value,
        "font_weight": FontWeight.MEDIUM.value,
        "font_size": FontSize.SMALL.value,
        "letter_spacing": "1px",
        "display": "inline_block",
        "padding": "10px 28px 11px 28px",
        "border_radius": "50px",
        "transition": " 0.5s",
        "margin": "10px 0 0 0",
        "color": "#fff",
        "background": DarkMode.FIFTH.value,
    },
    "#hero .btn-get-started:hover": {
        "background": Color.BACKGROUND.value,
    },
    "#hero .animated": {
        "animation": "up-down 5s ease-in-out infinite alternate-reverse both",
    },
    # Sesctions General
    "section": {
        "padding": "60px 0",
        "overflow": "hidden",
    },
    ".section-bg": {
        "background_color": Color.BACKGROUND.value,
    },
    ".section-title": {
        "text_align": "center",
        "padding_bottom": "30px",
    },
    ".section-title h2": {
        "font_size": FontSize.MEDIUM.value,
        "font_weight": FontWeight.BOLD.value,
        "text_transform": "uppercase",
        "margin_bottom": "20px",
        "padding_bottom": "20px",
        "position": "relative",
        "color": TextColor.SUBTITLE.value,
    },
    ".section-title h2::before": {
        "content": None,
        "position": "absolute",
        "display": "block",
        "width": "120px",
        "height": "1px",
        "background": Color.BACKGROUND.value,
        "bottom": "1px",
        "left": "calc(50% _ 60px)",
    },
    ".section-title h2::after": {
        "content": None,
        "position": "absolute",
        "display": "block",
        "width": "40px",
        "height": "3px",
        "background": Color.BACKGROUND.value,
        "bottom": "0",
        "left": "calc(50% _ 20px)",
    },
    ".section-title p": {
        "margin_bottom": "0",
    },
    # Clients
    ".clients": {
        "padding": "12px 0",
        "text_align": "center",
    },
    ".clients img": {
        "max_width": "45%",
        "transition": "all 0.4s ease_in_out",
        "display": "inline_block",
        "padding": "15px 0",
        "filter": "grayscale(100)",
    },
    ".clients img:hover": {
        "filter": "none",
        "transform": "scale(1.1)",
    },
    # About us
    ".about .content h3": {
        "font_weight": FontWeight.SEMIBOLD.value,
        "font_size": FontSize.REGULAR_BIG.value,
    },
    ".about .content ul": {
        "list_style": "none",
        "padding": "0",
    },
    ".about .content ul li": {
        "padding_left": "28px",
        "position": "relative",
    },
    ".about .content ul li+li": {
        "margin_top": "10px",
    },
    ".about .content ul i": {
        "position": "absolute",
        "left": "0",
        "top": "2px",
        "font_size": FontSize.NORMAL.value,
        "color": "#47b2e4",
        "line_height": "1",
    },
    ".about .content p:last-child": {
        "margin_bottom": "0",
    },
    ".about .content .btn-learn_more": {
        "font_family": Font.CONTENT.value,
        "font_weight": FontWeight.MEDIUM.value,
        "font_size": FontSize.VERY_SMALL.value,
        "letter_spacing": "1px",
        "display": "inline_block",
        "padding": "12px 32px",
        "border_radius": "4px",
        "transition": "0.3s",
        "line_height": "1",
        "color": "#47b2e4",
        "animation_delay": "0.8s",
        "margin_top": "6px",
        "border": "2px solid #47b2e4",
    },
    ".about .content .btn-learn-more:hover": {
        "background": "#47b2e4",
        "color": "#fff",
        "text_decoration": "none",
    },
    # Services
    ".services .icon-box": {
        "box_shadow": "0px 0 25px 0 rgba(0, 0, 0, 0.1)",
        "padding": "50px 30px",
        "transition": "all ease_in_out 0.4s",
        "background": Color.BACKGROUND.value,
    },
    ".services .icon-box .icon": {
        "margin_bottom": "10px",
    },
    ".services .icon-box .icon i": {
        "color": "#47b2e4",
        "font_size": FontSize.MEDIUM_REGULAR.value,
        "transition": "0.3s",
    },
    ".services .icon-box h4": {
        "font_weight": FontWeight.MEDIUM.value,
        "margin_bottom": "15px",
        "font_size": FontSize.REGULAR.value,
    },
    ".services .icon-box h4 a": {
        "color": "#37517e",
        "transition": "ease_in_out 0.3s",
    },
    ".services .icon-box p": {
        "line_height": "24px",
        "font_size": FontSize.VERY_SMALL.value,
        "margin_bottom": "0",
    },
    ".services .icon-box:hover": {
        "transform": "translateY(_10px)",
    },
    ".services .icon-box:hover h4 a": {
        "color": "#47b2e4",
    },
    # Frequently Asked Questions
    ".faq .faq-list": {
        "padding": "0 100px",
    },
    ".faq .faq-list ul": {
        "padding": "0",
        "list_style": "none",
    },
    ".faq .faq-list li+li": {
        "margin_top": "15px",
    },
    ".faq .faq-list li": {
        "padding": "20px",
        "background": Color.BACKGROUND.value,
        "border_radius": "4px",
        "position": "relative",
    },
    ".faq .faq-list a": {
        "display": "block",
        "position": "relative",
        "font_family": Font.CONTENT.value,
        "font_size": FontSize.SMALL.value,
        "line_height": "24px",
        "font_weight": FontWeight.MEDIUM.value,
        "padding": "0 30px",
        "outline": "none",
        "cursor": "pointer",
    },
    ".faq .faq-list .icon-help": {
        "font_size": "24px",
        "position": "absolute",
        "right": "0",
        "left": "20px",
        "color": "#47b2e4",
    },
    ".faq .faq-list .icon-show,.faq .faq-list .icon-close": {
        "font_size": "24px",
        "position": "absolute",
        "right": "0",
        "top": "0",
    },
    ".faq .faq-list p": {
        "margin_bottom": "0",
        "padding": "10px 0 0 0",
    },
    ".faq .faq-list .icon-show": {
        "display": "none",
    },
    ".faq .faq-list a.collapsed": {
        "color": "#37517e",
        "transition": "0.3s",
    },
    ".faq .faq-list a.collapsed:hover": {
        "color": "#47b2e4",
    },
    ".faq .faq-list a.collapsed .icon-show": {
        "display": "inline_block",
    },
    ".faq .faq-list a.collapsed .icon-close": {
        "display": "none",
    },
    # Contact
    ".contact .info": {
        "border_top": "3px solid #47b2e4",
        "border_bottom": "3px solid #47b2e4",
        "padding": "30px",
        "background": Color.BACKGROUND.value,
        "width": "100%",
        "box_shadow": "0 0 24px 0 rgba(0, 0, 0, 0.1)",
    },
    ".contact .info i": {
        "font_size": FontSize.NORMAL.value,
        "color": "#47b2e4",
        "float": "left",
        "width": "44px",
        "height": "44px",
        "background": Color.BACKGROUND.value,
        "display": "flex",
        "justify_content": "center",
        "align_items": "center",
        "border_radius": "50px",
        "transition": "all 0.3s ease_in_out",
    },
    ".contact .info h4": {
        "padding": "0 0 0 60px",
        "font_size": FontSize.INTER.value,
        "font_weight": FontWeight.SEMIBOLD.value,
        "margin_bottom": "5px",
        "color": "#37517e",
    },
    ".contact .info p": {
        "padding": "0 0 10px 60px",
        "margin_bottom": "20px",
        "font_size": FontSize.VERY_SMALL.value,
        "color": "#6182ba",
    },
    ".contact .info .email p": {
        "padding_top": "5px",
    },
    ".contact .info .social-links": {
        "padding_left": "60px",
    },
    ".contact .info .social-links a": {
        "font_size": FontSize.SMALL_MEDIUM.value,
        "display": "inline_block",
        "background": "#333",
        "color": "#fff",
        "line_height": "1",
        "padding": "8px 0",
        "border_radius": "50%",
        "text_align": "center",
        "width": "36px",
        "height": "36px",
        "transition": "0.3s",
        "margin_right": "10px",
    },
    ".contact .info .social-links a:hover": {
        "background": "#47b2e4",
        "color": "#fff",
    },
    ".contact .info .email:hover i,.contact .info .address:hover i,.contact .info .phone:hover i": {
        "background": "#47b2e4",
        "color": "#fff",
    },
    ".contact .php-email-form": {
        "width": "100%",
        "border_top": "3px solid #47b2e4",
        "border_bottom": "3px solid #47b2e4",
        "padding": "30px",
        "background": Color.BACKGROUND.value,
        "box_shadow": "0 0 24px 0 rgba(f, f, f, 0.12)",
    },
    ".contact .php-email-form .form-group": {
        "padding_bottom": "8px",
        "margin_bottom": "20px",
    },
    ".contact .php-email-form .validate": {
        "display": "none",
        "color": "red",
        "margin": "0 0 15px 0",
        "font_weight": FontWeight.REGULAR.value,
        "font_size": "13px",
    },
    ".contact .php-email-form .error-message": {
        "display": "none",
        "color": "#fff",
        "background": "#ed3c0d",
        "text_align": "left",
        "padding": "15px",
        "font_weight": FontWeight.SEMIBOLD.value,
    },
    ".contact .php-email-form .error-message br+br": {
        "margin_top": "25px",
    },
    ".contact .php-email-form .sent_message": {
        "display": "none",
        "color": "#fff",
        "background": "#18d26e",
        "text_align": "center",
        "padding": "15px",
        "font_weight": FontWeight.SEMIBOLD.value,
    },
    ".contact .php-email-form .loading": {
        "display": "none",
        "background": "#fff",
        "text_align": "center",
        "padding": "15px",
    },
    ".contact .php-email-form .loading:before": {
        "content": None,
        "display": "inline_block",
        "border_radius": "50%",
        "width": "24px",
        "height": "24px",
        "margin": "0 10px _6px 0",
        "border": "3px solid #18d26e",
        "border_top_color": "#eee",
        # animation: animate_loading 1s linear infinite,
    },
    ".contact .php-email-form label": {
        "padding_bottom": "8px",
    },
    ".contact .php-email-form input,.contact .php-email-form textarea": {
        "box_shadow": "none",
        "font_size": FontSize.VERY_SMALL.value,
        "border_radius": "4px",
    },
    ".contact .php-email-form input:focus,.contact .php-email-form textarea:focus": {
        "border_color": "#47b2e4",
    },
    ".contact .php-email-form input": {
        "height": "44px",
    },
    ".contact .php-email-form textarea": {
        "padding": "10px 12px",
    },
    ".contact .php-email-form button[type=submit]": {
        "background": "#47b2e4",
        "border": "0",
        "padding": "12px 34px",
        "color": "#fff",
        "transition": "0.4s",
        "border_radius": "50px",
    },
    ".contact .php-email-form button[type=submit]:hover": {
        "background": "#209dd8",
    },
    # Footer
    "#footer": {
        "font_size": FontSize.VERY_SMALL.value,
        "background": "#37517e",
    },
    "#footer .footer-newsletter": {
        "padding": "50px 0",
        "background": "#f3f5fa",
        "text_align": "center",
        "font_size": "15px",
        "color": "#444444",
    },
    "#footer .footer-newsletter h4": {
        "font_size": FontSize.REGULAR.value,
        "margin": "0 0 20px 0",
        "padding": "0",
        "line_height": "1",
        "font_weight": FontWeight.SEMIBOLD.value,
        "color": "#37517e",
    },
    "#footer .footer-newsletter form": {
        "margin_top": "30px",
        "background": Color.BACKGROUND.value,
        "padding": "6px 10px",
        "position": "relative",
        "border_radius": "50px",
        "box_shadow": "0px 2px 15px rgba(0, 0, 0, 0.06)",
        "text_align": "left",
    },
    "#footer .footer-newsletter form input[type=email]": {
        "border": "0",
        "padding": "4px 8px",
        "width": "calc(100% _ 100px)",
    },
    "#footer .footer-newsletter form input[type=submit]": {
        "position": "absolute",
        "top": "0",
        "right": "0",
        "bottom": " 0",
        "border": "0",
        "font_size": "16px",
        "padding": "0 20px",
        "background": "#47b2e4",
        "color": "#fff",
        "transition": "0.3s",
        "border_radius": "50px",
        "box_shadow": "0px 2px 15px rgba(0, 0, 0, 0.1)",
    },
    "#footer .footer-newsletter form input[type=submit]:hover": {
        "background": "#209dd8",
    },
    "#footer .footer-top": {
        "padding": "60px 0 30px 0",
        "background": "#fff",
    },
    "#footer .footer-top .footer-contact": {
        "margin_bottom": "30px",
    },
    "#footer .footer-top .footer-contact h3": {
        "font_size": FontSize.REGULAR_VERY_BIG.value,
        "margin": "0 0 10px 0",
        "padding": "2px 0 2px 0",
        "line_height": "1",
        "text_transform": "uppercase",
        "font_weight": FontWeight.SEMIBOLD.value,
        "color": "#37517e",
    },
    "#footer .footer-top .footer-contact p": {
        "font_size": FontSize.VERY_SMALL.value,
        "line_height": "24px",
        "margin_bottom": "0",
        "font_family": Font.FOOTER.value,
        "color": "#5e5e5e",
    },
    "#footer .footer-top h4": {
        "font_size": FontSize.SMALL.value,
        "font_weight": FontWeight.BOLD.value,
        "color": "#37517e",
        "position": "relative",
        "padding_bottom": "12px",
    },
    "#footer .footer-top .footer-links": {
        "margin_bottom": "30px",
    },
    "#footer .footer-top .footer-links ul": {
        "list_style": "none",
        "padding": "0",
        "margin": "0",
    },
    "#footer .footer-top .footer-links ul i": {
        "padding_right": "2px",
        "color": "#47b2e4",
        "font_size": FontSize.SMALL_MEDIUM.value,
        "line_height": "1",
    },
    "#footer .footer-top .footer-links ul li": {
        "padding": "10px 0",
        "display": "flex",
        "align_items": "center",
    },
    "#footer .footer-top .footer-links ul li:first-child": {
        "padding_top": "0",
    },
    "#footer .footer-top .footer-links ul a": {
        "color": "#777777",
        "transition": "0.3s",
        "display": "inline_block",
        "line_height": "1",
    },
    "#footer .footer-top .footer-links ul a:hover": {
        "text_decoration": "none",
        "color": "#47b2e4",
    },
    "#footer .footer-top .social-links a": {
        "font_size": FontSize.SMALL_MEDIUM.value,
        "display": "inline_block",
        "background": "#47b2e4",
        "color": "#fff",
        "line_height": "1",
        "padding": "8px 0",
        "margin_right": "4px",
        "border_radius": "50%",
        "text_align": "center",
        "width": "36px",
        "height": "36px",
        "transition": " 0.3s",
    },
    "#footer .footer-top .social-links a:hover": {
        "background": "#209dd8",
        "color": "#fff",
        "text_decoration": "none",
    },
    "#footer .footer-bottom": {
        "padding_top": "30px",
        "padding_bottom": "30px",
        "color": "#fff",
    },
    "#footer .copyright": {
        "float": "left",
    },
    "#footer .credits": {
        "float": "right",
        "font_size": "13px",
        "padding_top": "4px",
    },
    "#footer .credits a": {
        "transition": "0.3s",
    },
    "#footer .copyright,#footer .credits": {
        "text_align": "center",
        "float": "none",
    },
    # rx.chakra.MenuButton: {
    #     "_hover": {
    #         "background_color": Color.SECONDARY.value,
    #     },
    #     "active_color": Color.PRIMARY.value,
    # },
    # rx.chakra.Heading: {
    #     "size": "lg",
    #     "color": TextColor.HEADER.value,
    #     "font_family": Font.TITLE.value,
    #     "font_weight": FontWeight.MEDIUM.value,
    # },
    # rx.chakra.Button: {
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
    # rx.chakra.Link: {
    #     "text_decoration": "none",
    #     "_hover": {},
    # },
}

# header_style = dict(
#     display="block",
#     transition="all 0.5s",
#     z_index="997",
#     padding_top="15px 0",
# )

fixed_top_style = dict(
    position="fixed",
    top="0px",
    right="0px",
    left="0px",
)

# align_items_center_style = dict(
#     align_items_center="center!important",
# )

# d_flex_style = dict(
#     display="flex!important",
# )

# container_style = dict(
#     display="block",
#     width="100%",
#     padding_right="0.75rem",
#     padding_left="0.75rem",
#     margin_right="auto",
#     margin_left="auto",
#     max_width=[
#         "540px",
#         "720px",
#         "960px",
#         "1140px",
#     ],
# )

# hero_container_style = dict(
#     padding_top="72px",
# )

# logo_href_style = dict(
#     font_size="30px",
#     margin_top="0",
#     margin_bottom="0px",
#     margin_left="0px",
#     padding="0px",
#     line_height="1",
#     font_weight=FontWeight.MEDIUM.value,
#     letter_spacing="2px",
#     text_transform="uppercase",
# )

# me_auto_style = dict(
#     margin_right="auto!important",
# )


# img_style = dict(
#     overflow_clip_margin="content_box",
#     overflow="clip",
#     vertical_align="middle",
# )

# img_fluid_style = dict(
#     max_width="100%",
#     height="auto",
# )

# navbar_style = dict(
#     padding="0",
#     position="relative",
#     display="flex",
#     flex_wrap="wrap",
#     align_items="center",
#     justify_content="space_between",
# )

# ul_style = dict(
#     margin_block_start="1em",
#     margin_block_end="1em",
#     margin_inline_start="0px",
#     margin_inline_end="0px",
#     padding_inline_start="40px",
# )

# navbar_ul_style = dict(
#     margin="0",
#     padding="0",
#     display="flex",
#     list_style="none",
#     align_items="center",
# )

# navbar_menu_button_style = dict(
#     padding="8px 20px",
#     margin_left="30px",
#     border_radius="50px",
#     color=TextColor.MENU_OPTION.value,
#     font_size="14px",
#     border="2px solid #47b2e4",
#     font_weight=FontWeight.SEMIBOLD.value,
# )

# section_style = dict(
#     padding="60px 0",
#     overflow="hidden",
#     display="block",
# )

# hero_style = dict(
#     width="100%",
#     height="80vh",
#     background_color=BackGroundColor.HERO.value,
# )

# row_style = dict(
#     display="flex",
#     flex_wrap="wrap",
#     margin_top="0px",
#     margin_right="_0.75rem",
#     margin_left="_0.75rem",
#     max_width="100%",
#     padding_right="0.75rem",
#     padding_left="0.75rem",
# )

# col_style = dict(
#     flex="0 0 auto",
#     width=["50%", "50%", "50%", "50%", "50%"],
# )

# flex_column_style = dict(
#     flex_direction="column!important",
# )

# justify_content_center_style = dict(
#     justify_content="center!important",
# )

# order_2_style = dict(
#     order=[
#         "2!important",
#         "2!important",
#         "2!important",
#         "2!important",
#         "2!important",
#     ]
# )

# pt_4_style = dict(
#     padding_top="1.5rem!important",
# )

# order_1_style = dict(
#     order=[
#         "1!important",
#         "1!important",
#         "1!important",
#         "1!important",
#         "1!important",
#     ]
# )

# pt_style = dict(
#     padding_top=[
#         "0!important",
#         "0!important",
#         "0!important",
#         "0!important",
#         "0!important",
#     ]
# )

# h1_style = dict(
#     font_weight="500",
#     font_size="2.5rem",
#     display="block",
#     margin_block_start="0.83em",
#     margin_block_end="0.83em",
#     margin_inline_start="0px",
#     margin_inline_end="0px",
# )

# h1_hero_style = dict(
#     margin="0 0 10px 0",
#     font_family=Font.HERO.value,
#     font_size=FontSize.BIG.value,
#     font_weight=FontWeight.BOLD.value,
#     line_height="56px",
#     color=TextColor.TITLE.value,
# )

# h2_style = dict(
#     font_weight="500",
#     font_size="2rem",
#     display="block",
#     margin_top="0",
#     line_height="1.2",
#     margin_block_start="0.83em",
#     margin_block_end="0.83em",
#     margin_inline_start="0px",
#     margin_inline_end="0px",
# )

# h2_hero_style = dict(
#     font_family=Font.HERO.value,
#     color=TextColor.SUBTITLE.value,
#     margin_bottom="50px",
#     font_size=FontSize.REGULAR.value,
#     font_weight=FontWeight.MEDIUM.value,
# )

# hero_img_style = dict(
#     width="100%",
# )

# hero_container = dict(
#     padding_top="72px",
# )

# animated_style = dict(
#     animation="up_down 2s ease_in_out infinite alternate_reverse both",
# )

# aos_animate_style = dict(
#     opacity="1",
#     transform="translateZ(0) scale(1)",
#     transition_delay=".2s",
#     pointer_events="auto",
# )

# data_aos_fade_up_style = dict(
#     transform="translate3d(0,100px,0)",
# )

# data_aos_delay_style = dict(
#     transition_delay="0s",
# )

# data_aos_zoom_in_style = dict(
#     transition_property="opacity,transform,_webkit_transform",
# )

# main_style = dict(
#     display="block",
# )

# clients_style = dict(
#     padding="12px 0",
#     text_align="center",
# )

# section_bg = dict(
#     background_color="black",
# )


# col_2_style = dict(
#     flex="0 0 auto",
#     width=[
#         "30%",
#         "30%",
#         "30%",
#         "30%",
#         "30%",
#     ],
# )

# col_4_style = dict(
#     flex="0 0 auto",
#     width=[
#         "20%",
#         "20%",
#         "20%",
#         "20%",
#         "20%",
#     ],
# )

# clients_img_style = dict(
#     max_width="60%",
#     transition="all 0.4s ease_in_out",
#     display="inline_block",
#     padding="15px 0",
# )

# section_title_style = dict(
#     display="block",
#     text_align="center",
#     padding_bottom="30px",
# )

# h2_section_title_text_style = dict(
#     font_family=Font.SECTION_TITLE.value,
#     color=TextColor.TITLE.value,
#     font_size=FontSize.MEDIUM.value,
#     font_weight=FontWeight.BOLD.value,
#     text_transform="uppercase",
#     margin_bottom="20px",
#     padding_bottom="20px",
#     position="relative",
# )

# parragraph_text_style = dict(
#     margin_top="0",
#     margin_bottom="1rem",
#     display="block",
#     margin_block_start="1em",
#     margin_block_end="1em",
#     margin_inline_start="0px",
#     margin_inline_end="0px",
#     color=TextColor.BODY.value,
# )

# list_unordered_style = dict(
#     list_style="none",
#     padding="0",
#     margin_top="0",
#     margin_bottom="1rem",
#     display="block",
#     margin_block_start="1em",
#     margin_block_start_end="1em",
#     margin_inline_start="0px",
#     margin_inline_end="0px",
#     padding_inline_start="40px",
# )

# list_item_unordered_style = dict(
#     padding_left="20px",
#     position="relative",
#     display="list_item",
#     text_align="left",
#     left="0",
#     top="2px",
#     color=TextColor.BODY.value,
#     line_height="1",
#     font_style=FontStyle.NORMAL.value,
# )

# services_col_style = dict(
#     flex="0 0 auto",
#     width=["50%", "50%", "50%", "25%", "25%"],
#     # pointer_events="auto",
#     # opacity="1",
#     # transform="translateZ(0) scale(1)",
#     # transition_delay=".1s",
#     # transition_property="opacity,transform, _webkit_transform",
#     # transition_timing_function="ease_in_out",
#     # transition_duration="1s",
# )

# align_items_stretch_style = dict(
#     align_items="stretch!important",
# )

# services_icon_box_style = dict(
#     # box_shadow="0px 0 25px 0 rgba(0,0,0,0.1)",
#     box_shadow="0px 0 25px 0 rgba(255,255,55,0.5)",
#     padding="50px 30px",
#     transition="all ease_in_out 0.4s",
#     background="#000",
#     display="block",
# )

# service_icon_container_style = dict(
#     margin_bottom="10px",
#     display="block",
# )

# sevice_icon_style = dict(
#     color="#47b2e4",
#     font_size="36px",
#     transition="0.3s",
#     font_family="boxicons!important",
#     font_weight=FontWeight.REGULAR.value,
#     font_style=FontStyle.NORMAL.value,
#     font_variant="normal",
#     line_height="1",
#     text_rendering="auto",
#     display="inline_block",
#     text_transform="none",
#     speak="none",
# )

# h4_style = dict(
#     display="block",
#     margin_block_start="1.33em",
#     margin_block_end="1.33em",
#     margin_inline_start="0px",
#     margin_inline_end="0px",
#     margin_top="0",
#     line_height="1.2",
#     color=TextColor.TITLE.value,
#     font_weight=FontWeight.MEDIUM.value,
#     margin_bottom="15px",
#     font_size=FontSize.REGULAR.value,
# )

# link_style = dict(
#     color=Color.SECONDARY.value,
#     transition="ease_in_out 0.3s",
#     text_decoration="none",
#     box_sizing="border_box",
#     cursor="pointer",
# )

# service_parragraph_style = dict(
#     line_height="24px",
#     font_size="14px",
#     margin_bottom="0",
#     color=TextColor.CARD.value,
# )

# mt_4_style = dict(
#     margin_top="1.5rem",
# )

# mt_md_0_style = dict(
#     margin_top="0!important",
# )

# mt_xl_0_style = dict(
#     margin_top="0!important",
# )

# faq_list_style = dict(
#     padding="0 100px",
# )

# faq_list_icon = dict(
#     font_size=FontSize.REGULAR.value,
#     position="absolute",
#     right="0",
#     left="0",
# )

# bx_style = dict(
#     font_family=Font.ICON.value,
#     font_size=FontSize.REGULAR.value,
#     font_weight=FontWeight.REGULAR.value,
#     font_style=FontStyle.NORMAL.value,
#     font_variant=FontVariant.NORMAL.value,
#     line_height="1",
#     text_rendering="auto",
#     display="inline_block",
#     text_transform="none",
#     speak="none",
#     color=Color.ICON.value,
# )

# link_faq_list_style = dict(
#     display="block",
#     position="relative",
#     font_family=Font.LINK.value,
#     font_size=FontSize.SMALL.value,
#     line_height="24px",
#     font_weight=FontWeight.MEDIUM.value,
#     padding="0 30px",
#     outline="none",
#     cursor="pointer",
# )

# icon_show_style = dict(
#     display="inline_block",
#     font_size=FontSize.REGULAR.value,
#     position="absolute",
#     rigth="0",
#     top="0",
# )

# h4_style = dict(
#     margin_top="0",
#     line_height="1.2",
#     display="block",
#     margin_block_start="1.33em",
#     margin_block_end="1.33em",
#     margin_inline_start="0px",
#     margin_inline_end="0px",
#     unicode_bidi="isolate",
# )

# h4_info_contact_style = dict(
#     padding="0 0 0 60px",
#     font_size=FontSize.INTER.value,
#     font_weight=FontWeight.SEMIBOLD.value,
#     margin_bottom="5px",
# )
