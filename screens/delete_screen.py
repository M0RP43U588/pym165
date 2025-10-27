from textual.screen import Screen


class DeleteScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
