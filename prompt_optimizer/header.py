import reflex as rx


class HeaderState(rx.State):
    @rx.event
    def toggle_sidebar(self): ...


def header() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.button(
                "☰",
                bg="transparent",
                font_size="20px",
                on_click=HeaderState.toggle_sidebar,
            ),
            rx.text("LiteLLM", font_size="18px", font_weight="bold", color="#fff"),
            rx.box(flex="1"),
            rx.button(
                "Star us on GitHub",
                bg="transparent",
                border="1px solid #444",
                color="#fff",
                border_radius="6px",
            ),
            spacing="3",
            align_items="center",
        ),
        height="60px",
        border_bottom="1px solid #333",
    )
