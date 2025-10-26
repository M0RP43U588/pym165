from textual.app import App, ComposeResult
from textual.containers import VerticalGroup, Horizontal
from textual.widgets import Footer, Header, Button, Static


class CrudButtons(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield Button("Create", id="create_button")
        yield Button("Read", id="read_button")
        yield Button("Update", id="update_button")
        yield Button("Delete", id="delete_button")


class WelcomeScreen(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield Static("version placeholder - PyMongo TUI", id="version_static")


class Tui(App):
    CSS_PATH = "tui.tcss"

    def on_mount(self) -> None:
        self.theme: str = "catppuccin-mocha"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Horizontal(CrudButtons())
        yield Horizontal(WelcomeScreen())
