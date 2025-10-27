from textual.screen import Screen


class CreateScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
