from textual import on
from textual.validation import Function
from textual.widgets import Input, Static
from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalGroup
from shared.data import collection_fields


class RSMain(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Feld:",
                    type="text",
                    max_length=12,
                    validators=[Function(rs_input_validator)],
                    id="rs_input"
                    )
        yield Static("", id="rs_static")

    @on(Input.Submitted)
    def show_errormsg(self, event: Input.Submitted) -> None:
        if not event.validation_result.is_valid:
            self.query_one(Static).update("Feld ist ungültig")
        else:
            self.query_one(Static).update("placeholder, might put query result here")


def rs_input_validator(value: str) -> bool:
    return bool(value in collection_fields)


class ReadScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Horizontal(RSMain())
