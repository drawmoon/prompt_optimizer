import reflex as rx

config = rx.Config(
    app_name="prompt_optimizer",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
