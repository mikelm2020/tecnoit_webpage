import reflex as rx

config = rx.Config(
    app_name="index",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)