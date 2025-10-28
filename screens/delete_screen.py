from textual import on
from textual.validation import Function
from textual.widgets import Input, Static
from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalGroup
from shared.data import collection_fields_to_types_fake
from shared.db import mongodb_delete, document_field_validator


class DSMain(VerticalGroup):
    field = None
    field_type = None
    value = None

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Feld:",
                    type="text",
                    max_length=12,
                    validators=[Function(document_field_validator)],
                    id="ds_field_input"
                    )
        yield Input(placeholder="Wert:",
                    type="text",
                    max_length=100,
                    validators=[Function(ds_value_validator)],
                    disabled=True,
                    id="ds_value_input"
                    )
        yield Static("", id="ds_static")

    @on(Input.Changed, "#ds_field_input")
    def ds_set_values(self, event: Input.Changed) -> None:
        if event.validation_result.is_valid:
            self.query_one("#ds_value_input", Input).disabled = False
            DSMain.field_type = collection_fields_to_types_fake.get(event.value)
            DSMain.field = event.value
        else:
            self.query_one("#ds_value_input", Input).disabled = True
            self.query_one("#ds_value_input", Input).value = ""

    @on(Input.Submitted, "#ds_value_input")
    def match_validation(self, event: Input.Submitted) -> None:
        if event.validation_result.is_valid:
            match DSMain.field_type:
                case "int":
                    DSMain.value = int(event.value.strip())
                case "float":
                    DSMain.value = float(event.value.strip())
                case _:
                    DSMain.value = str(event.value.strip())

            if bool(mongodb_delete({DSMain.field: {"$regex": f"{DSMain.value}", "$options": "i"}})):
                self.query_one("#ds_static", Static).update("Datensatz wurde erfolgreich entfernt")


def ds_value_validator(value: str) -> bool:
    if DSMain.field_type is None:
        return False

    match DSMain.field_type:
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


class DeleteScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Horizontal(DSMain())
