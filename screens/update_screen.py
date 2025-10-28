from textual import on
from textual.validation import Function
from textual.widgets import Input, Static
from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalGroup
from shared.data import collection_fields_to_types_fake
from shared.db import mongodb_update, document_field_validator


class USMain(VerticalGroup):
    target_field = None
    target_field_type = None
    target_value = None
    changed_field = None
    changed_field_type = None
    changed_value = None

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Feld des Dokuments, welches geändert werden soll",
                    type="text",
                    max_length=12,
                    validators=[Function(document_field_validator)],
                    id="us_target_field"
                    )
        yield Input(placeholder="Wert des Dokuments, welches geändert werden soll",
                    type="text",
                    max_length=100,
                    validators=[Function(us_target_value_validator)],
                    disabled=True,
                    id="us_target_value"
                    )
        yield Input(placeholder="Feld, welches geändert werden soll",
                    type="text",
                    max_length=12,
                    validators=[Function(document_field_validator)],
                    disabled=True,
                    id="us_change_field"
                    )
        yield Input(placeholder="Wert, der geändert werden soll",
                    type="text",
                    max_length=100,
                    validators=[Function(us_change_value_validator)],
                    disabled=True,
                    id="us_change_value"
                    )
        yield Static("", id="us_static")

    @on(Input.Submitted, "#us_target_field")
    def us_action_target_field(self, event: Input.Submitted) -> None:
        if event.validation_result.is_valid:
            self.query_one("#us_target_value").disabled = False
            USMain.target_field_type = collection_fields_to_types_fake.get(event.value)
            USMain.target_field = event.value
        else:
            self.query_one("#us_target_value").disabled = True

    @on(Input.Submitted, "#us_target_value")
    def us_action_target_value(self, event: Input.Submitted) -> None:
        if event.validation_result.is_valid:
            match USMain.target_field_type:
                case "int":
                    USMain.target_value = int(event.value.strip())
                case "float":
                    USMain.target_value = float(event.value.strip())
                case _:
                    USMain.target_value = str(event.value.strip())
            self.query_one("#us_change_field").disabled = False
        else:
            self.query_one("#us_change_field").disabled = True

    @on(Input.Submitted, "#us_change_field")
    def us_action_change_field(self, event: Input.Submitted) -> None:
        if event.validation_result.is_valid:
            self.query_one("#us_change_value").disabled = False
            USMain.change_field_type = collection_fields_to_types_fake.get(event.value)
            USMain.change_field = event.value
        else:
            self.query_one("#us_change_value").disabled = True

    @on(Input.Submitted, "#us_change_value")
    def us_action_change_value(self, event: Input.Submitted) -> None:
        if event.validation_result.is_valid:
            match USMain.change_field_type:
                case "int":
                    USMain.change_value = int(event.value.strip())
                case "float":
                    USMain.change_value = float(event.value.strip())
                case _:
                    USMain.change_value = str(event.value.strip())
            if bool(mongodb_update(
                {USMain.target_field: USMain.target_value},
                {"$set": {USMain.change_field: USMain.change_value}}
                )):
                self.query_one("#us_static").update("Datensatz wurde erfolgreich geändert")

                for widget in self.query(Input):
                    widget.value = ""


def us_target_value_validator(value: str) -> bool:
    if USMain.target_field is None:
        return False

    match USMain.target_field_type:
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


def us_change_value_validator(value: str) -> bool:
    if USMain.change_field is None:
        return False

    match USMain.change_field_type:
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


class UpdateScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Horizontal(USMain())
