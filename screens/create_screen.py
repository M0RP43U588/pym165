from textual import on
from textual.validation import Number
from textual.widgets import Input, Static
from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalGroup
from shared.db import mongodb_create
from pprint import pformat


class CSMain(VerticalGroup):
    art: list = []
    sch: list = []

    def compose(self) -> ComposeResult:
        yield Input(
                placeholder="Filmtitel",
                type="text",
                max_length=50,
                id="cs_name_input"
                )
        yield Input(
                placeholder="Genre (Komma getrennt)",
                type="text",
                max_length=50,
                id="cs_art_input"
                )
        yield Input(
                placeholder="Jahr der Filmveröffentlichung (Zahl zwischen 1900 - 2025)",
                type="integer",
                max_length=4,
                id="cs_jahr_input",
                validators=[
                    Number(minimum=1900, maximum=2025)
                    ]
                )
        yield Input(
                placeholder="Regisseur",
                type="text",
                max_length=30,
                id="cs_reg_input"
                )
        yield Input(
                placeholder="Schauspieler (Komma getrennt)",
                type="text",
                max_length=60,
                id="cs_sch_input"
                )
        yield Input(
                placeholder="Bewertung (Zahl zwischen 1.00-10.00)",
                type="number",
                max_length=4,
                id="cs_rating_input",
                validators=[
                    Number(minimum=0, maximum=10)
                    ]
                )
        yield Input(
                placeholder="Mindestalter (Zahl zwischen 1-18)",
                type="integer",
                max_length=2,
                id="cs_age_input",
                validators=[
                    Number(minimum=1, maximum=18)
                    ]
                )
        yield Input(
                placeholder="Bemerkungen",
                type="text",
                max_length=100,
                id="cs_bem_input"
                )
        yield Static("", id="cs_static")

    @on(Input.Blurred, "#cs_art_input")
    def split_art(self, event: Input.Blurred) -> None:
        CSMain.art = event.value.strip().split(",")

    @on(Input.Blurred, "#cs_sch_input")
    def split_sch(self, event: Input.Blurred) -> None:
        CSMain.sch = event.value.strip().split(",")

    @on(Input.Submitted, "#cs_bem_input")
    def run_create(self, event: Input.Submitted) -> None:

        name = self.query_one("#cs_name_input").value
        art = CSMain.art or []
        jahr = self.query_one("#cs_jahr_input").value
        regisseur = self.query_one("#cs_reg_input").value
        sch = CSMain.sch or []
        rating = self.query_one("#cs_rating_input").value
        min_alter = self.query_one("#cs_age_input").value
        bemerkungen = self.query_one("#cs_bem_input").value

        json = {
                "name": name,
                "art": art,
                "jahr": jahr,
                "regisseur": regisseur,
                "schauspieler": sch,
                "rating": rating,
                "min_alter": min_alter,
                "bemerkungen": bemerkungen
                }

        success = mongodb_create(json)
        if success:
            self.query_one("#cs_static").update(f"{str(pformat(json))}\n\nObenstehende Daten wurden erfolgreich eingefügt.")
            for widget in self.query(Input):
                widget.value = ""
            self.set_timer(5, lambda: self.query_one("#cs_static", Static).update(""))
        else:
            self.query_one("#cs_static").update("Fehler: Datensatz konnte nicht eingefügt werden")
            self.set_timer(5, lambda: self.query_one("#cs_static", Static).update(""))


class CreateScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Horizontal(CSMain())
