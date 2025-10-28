from textual import on
from textual.validation import Number
from textual.widgets import Input, Static
from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalGroup
from shared.db import mongodb_create


class CSMain(VerticalGroup):
    art: str = None
    sch: str = None

    def compose(self) -> ComposeResult:
        yield Input(
                placeholder="Name / Titel",
                type="text",
                max_length=50,
                id="cs_name_input"
                )
        yield Input(
                placeholder="Art",
                type="text",
                max_length=50,
                id="cs_art_input"
                )
        yield Input(
                placeholder="Jahr",
                type="integer",
                max_length=4,
                id="cs_jahr_input",
                validators=[
                    Number(minimum=1800, maximum=2025)
                    ]
                )
        yield Input(
                placeholder="Regisseur",
                type="text",
                max_length=30,
                id="cs_reg_input"
                )
        yield Input(
                placeholder="Schauspieler",
                type="text",
                max_length=60,
                id="cs_sch_input"
                )
        yield Input(
                placeholder="Rating",
                type="number",
                max_length=4,
                id="cs_rating_input",
                validators=[
                    Number(minimum=0, maximum=10)
                    ]
                )
        yield Input(
                placeholder="Mind. Alter",
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
        CSMain.art = event.value.split(",")

    @on(Input.Blurred, "#cs_sch_input")
    def split_sch(self, event: Input.Blurred) -> None:
        CSMain.sch = event.value.split(",")

    @on(Input.Submitted, "#cs_bem_input")
    def run_create(self, event: Input.Submitted) -> None:

        name = self.query_one("#cs_name_input").value
        art: list = CSMain.art
        jahr = self.query_one("#cs_jahr_input").value
        regisseur = self.query_one("#cs_reg_input").value
        sch: list = CSMain.sch
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

        if bool(mongodb_create(json)):
            self.query_one("#cs_static").update("Datensatz erfolgreich eingefügt")


class CreateScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Horizontal(CSMain())
