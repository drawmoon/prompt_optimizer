import reflex as rx

from .header import header
from .main_content import main_content
from .sidebar import sidebar


class AppState(rx.State):
    sidebar_visible: bool = True


def index() -> rx.Component:
    return rx.flex(
        header(),
        rx.cond(
            AppState.sidebar_visible,
            rx.flex(sidebar(), main_content()),
        ),
        direction="column",
    )


app = rx.App()
app.add_page(index)
