from textual.screen import Screen


class UpdateScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
