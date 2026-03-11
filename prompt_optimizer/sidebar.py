import reflex as rx

models = ["gpt-4o", "gpt-4o-mini", "claude-3-5-sonnet", "gemini-1.5-pro"]


class SidebarState(rx.State): ...


def sidebar() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.box(
                rx.text("Models", font_size="14px", font_weight="500", color="#888"),
                px="16px",
                py="12px",
            ),
            rx.box(
                rx.input(
                    placeholder="Search models...",
                    bg="#262626",
                    border="1px solid #333",
                    color="#fff",
                    _placeholder={"color": "#666"},
                    border_radius="6px",
                    px="12px",
                    width="100%",
                ),
                px="16px",
                py="8px",
            ),
            rx.vstack(
                rx.foreach(
                    models,
                    lambda model: rx.box(
                        rx.hstack(
                            rx.box(
                                size="20px",
                                border="2px solid #8b5cf6",
                                bg="#8b5cf6",
                                border_radius="full",
                            ),
                            rx.vstack(
                                rx.text(
                                    model,
                                    font_size="14px",
                                    font_weight="500",
                                    color="#fff",
                                ),
                                rx.text("Model", font_size="12px", color="#888"),
                                align_items="start",
                            ),
                            spacing="2",
                            width="100%",
                            py="8px",
                            px="12px",
                        ),
                        bg="rgba(139, 92, 246, 0.1)",
                        border_radius="8px",
                        width="100%",
                        cursor="pointer",
                    ),
                ),
                spacing="1",
                px="8px",
            ),
            spacing="0",
        ),
        width="240px",
        # height="calc(100vh - 50px)",
        border_right="1px solid #333",
    )
