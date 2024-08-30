import reflex as rx


def dark_mode_toggle():
    """Creates a dark mode toggle button with sun and moon icons."""
    return rx.el.button(
        rx.icon(
            alt="Dark mode",
            class_name="dark:hidden",
            tag="moon",
            height="1.5rem",
            width="1.5rem",
        ),
        rx.icon(
            alt="Light mode",
            class_name="dark:inline",
            tag="sun",
            height="1.5rem",
            display="none",
            width="1.5rem",
        ),
        class_name="dark:hover:text-blue-400 dark:text-gray-300",
        onclick="toggleDarkMode()",
        _hover={"color": "#3B82F6"},
        color="#4B5563",
    )
