from textual import on
from textual.validation import Function
from textual.widgets import Input, Static
from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalGroup
from shared.data import collection_fields_to_types_fake
from shared.db import mongodb_read, document_field_validator
from pprint import pformat


class RSMain(VerticalGroup):
    field_value = None
    field = None
    value = None

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Feld:",
                    type="text",
                    max_length=12,
                    validators=[Function(document_field_validator)],
                    id="rs_field_input"
                    )
        yield Input(placeholder="Wert:",
                    type="text",
                    max_length=100,
                    validators=[Function(rs_value_validator)],
                    disabled=True,
                    id="rs_value_input"
                    )
        yield Static("", id="rs_static")

    @on(Input.Changed, "#rs_field_input")
    def rs_set_values(self, event: Input.Changed) -> None:
        if event.validation_result.is_valid:
            self.query_one("#rs_value_input", Input).disabled = False
            RSMain.field_type = collection_fields_to_types_fake.get(event.value)
            RSMain.field = event.value
        else:
            self.query_one("#rs_value_input", Input).disabled = True
            self.query_one("#rs_value_input", Input).value = ""

    @on(Input.Submitted, "#rs_value_input")
    def match_validation(self, event: Input.Submitted) -> None:
        if event.validation_result.is_valid:
            match RSMain.field_type:
                case "int":
                    RSMain.value = int(event.value.strip())
                    result = mongodb_read({RSMain.field: {"$eq": RSMain.value}})
                case "float":
                    RSMain.value = float(event.value.strip())
                    result = mongodb_read({RSMain.field: {"$eq": RSMain.value}})
                case _:
                    RSMain.value = str(event.value.strip())
                    result = mongodb_read({RSMain.field: {"$regex": f"{RSMain.value}", "$options": "i"}})
            self.query_one("#rs_static", Static).update(pformat(list(result)))




def rs_value_validator(value: str) -> bool:
    if RSMain.field_type is None:
        return False

    match RSMain.field_type:
        case "int":
            try:
                int(value)
                return True
            except ValueError:
                return False
        case "float":
            try:
                float(value)
                return True
            except ValueError:
                return False
        case _:
            return True


class ReadScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Horizontal(RSMain())
