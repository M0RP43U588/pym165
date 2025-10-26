from shared.textual_shared import Screen


class DeleteScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
