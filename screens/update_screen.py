from shared.textual_shared import Screen


class UpdateScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
