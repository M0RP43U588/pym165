from textual import on
from textual.app import App, ComposeResult
from textual.containers import VerticalGroup, Horizontal
from textual.screen import Screen
from textual.widgets import Footer, Header, Button, Static
from config import version, mongodb_ascii, help_text


class CreateScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]


class ReadScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]


class UpdateScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]


class DeleteScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]


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
    SCREENS = {"cs": CreateScreen,
               "rs": ReadScreen,
               "us": UpdateScreen,
               "ds": DeleteScreen}

    def on_mount(self) -> None:
        self.theme: str = "catppuccin-mocha"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Horizontal(CrudButtons())
        yield Horizontal(WelcomeScreen())

    @on(Button.Pressed, "#create_button")
    def tui_create_mode(self) -> None:
        self.push_screen("cs")

    @on(Button.Pressed, "#read_button")
    def tui_read_mode(self) -> None:
        self.push_screen("rs")

    @on(Button.Pressed, "#update_button")
    def tui_update_mode(self) -> None:
        self.push_screen("us")

    @on(Button.Pressed, "#delete_button")
    def tui_delete_mode(self) -> None:
        self.push_screen("ds")
