import reflex as rx

MAX_TOKENS = 4096

models = ["gpt-4o", "gpt-4o-mini", "claude-3-5-sonnet", "gemini-1.5-pro"]


class ModelConfigState(rx.State):
    selected_model: str
    prompt: str
    temperature: float = 1.0
    max_tokens: int = 1024

    @rx.event
    def set_selected_model(self): ...

    @rx.event
    def call_model(self): ...


def _label(title: str | int | float):
    return rx.text(title, font_size="13px", color="#888", font_weight=300)


def _model_config_panel() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.heading("Configurations", size="5"),
            rx.flex(
                _label("Prompt Template"),
                rx.text_area(
                    placeholder="Enter prompt template...",
                    border="1px solid #333",
                    border_radius="6px",
                ),
                direction="column",
                spacing="1",
            ),
            rx.flex(
                _label("Select Model"),
                rx.select.root(
                    rx.select.trigger(placeholder="Select a Model"),
                    rx.select.content(
                        rx.select.group(
                            rx.foreach(models, lambda x: rx.select.item(x, value=x))
                        )
                    ),
                    value=ModelConfigState.selected_model,
                    on_change=ModelConfigState.set_selected_model,
                ),
                direction="column",
                spacing="1",
                width="100%",
            ),
            rx.flex(
                _label("Temperature"),
                rx.flex(
                    rx.slider(
                        default_value=ModelConfigState.temperature,
                        min=0,
                        max=1,
                        step=0.1,
                        width="150px",
                    ),
                    _label(ModelConfigState.temperature),
                    spacing="2",
                    align_items="center",
                ),
                direction="column",
                spacing="1",
            ),
            rx.flex(
                _label("Max Tokens"),
                rx.flex(
                    rx.slider(
                        default_value=ModelConfigState.max_tokens,
                        min=1,
                        max=MAX_TOKENS,
                        step=1,
                        width="150px",
                    ),
                    _label(ModelConfigState.max_tokens),
                    spacing="2",
                    align_items="center",
                ),
                direction="column",
                spacing="1",
            ),
            # rx.spacer(),
            rx.button("Run", color_scheme="grass", border_radius="6px", width="100%"),
            direction="column",
            spacing="3",
            bg="#262626",
            # margin="10px",
            padding_x="10px",
            padding_y="20px",
        ),
        rx.box(flex=1),
        # height="calc(100vh - 50px)",
        border_radius="8px",
        border="1px solid #333",
        padding_x="10px",
        padding_y="10px",
    )


def _evaluation_panel():
    return rx.flex(flex="1")


def main_content():
    return rx.flex(_model_config_panel(), _evaluation_panel(), padding="10px")
