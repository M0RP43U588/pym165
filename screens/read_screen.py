from shared.textual_shared import Screen


class ReadScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
