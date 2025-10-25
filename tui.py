from textual.app import App, ComposeResult
from textual.containers import VerticalGroup, HorizontalScroll
from textual.widgets import Footer, Header, Button


class CrudButtons(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield Button("Create", id="create_button")
        yield Button("Read", id="read_button")
        yield Button("Update", id="update_button")
        yield Button("Delete", id="delete_button")


class Tui(App):
    def on_mount(self) -> None:
        self.theme: str = "catppuccin-mocha"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield HorizontalScroll(CrudButtons())
