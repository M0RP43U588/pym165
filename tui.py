from textual.app import App, ComposeResult
from textual.containers import VerticalGroup, Horizontal
from textual.widgets import Footer, Header, Button, Static
from config import version, mongodb_ascii, help_text


class CrudButtons(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield Button("Create",
                     id="create_button", classes="crud_buttons")
        yield Button("Read",
                     id="read_button", classes="crud_buttons")
        yield Button("Update",
                     id="update_button", classes="crud_buttons")
        yield Button("Delete",
                     id="delete_button", classes="crud_buttons")


class WelcomeScreen(VerticalGroup):
    def compose(self) -> ComposeResult:
        yield Static(f"{version} - PyM165 TUI",
                     classes="welcome_widgets", id="version_static")
        yield Static(mongodb_ascii,
                     classes="welcome_widgets", id="mongodb_ascii")
        yield Static(help_text,
                     classes="welcome_widgets", id="help_text")


class Tui(App):
    CSS_PATH = ["classes.tcss", "ids.tcss"]

    def on_mount(self) -> None:
        self.theme: str = "catppuccin-mocha"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Horizontal(CrudButtons())
        yield Horizontal(WelcomeScreen())
