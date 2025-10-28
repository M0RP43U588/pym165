version: str = "0.7.0"

mongodb_ascii: str = r"""
 /$$      /$$                                         /$$$$$$$  /$$$$$$$
| $$$    /$$$                                        | $$__  $$| $$__  $$
| $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ | $$  \ $$| $$  \ $$
| $$ $$/$$ $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  | $$| $$$$$$$
| $$  $$$| $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  | $$| $$__  $$
| $$\  $ | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  \ $$
| $$ \/  | $$|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$/| $$$$$$$/| $$$$$$$/
|__/     |__/ \______/ |__/  |__/ \____  $$ \______/ |_______/ |_______/
                                  /$$  \ $$
                                 |  $$$$$$/
                                  \______/
"""

help_text: str = """
Willkommen, die navigation funktioniert wie folgt:
    - Tab zum auswählen der Buttons (nächster)
    - Shift Tab zum auswählen der Buttons (vorheriger)
    - Enter um einen Button zu klicken
    - Control+Q um das Programm zu beenden
    - Escape um zum Hauptmenu zurückzugelangen
    - Der Mauszeiger kann auch verwendet werden
"""

collection_fields: list[str] = [
        "name", "art", "jahr",
        "regisseur", "schauspieler",
        "rating", "min_alter", "bemerkungen"
        ]

collection_fields_to_types: set[str, str] = {
        "name": "str",
        "art": "str",
        "jahr": "int",
        "regisseur": "str",
        "schauspieler": "str",
        "rating": "float",
        "min_alter": "int",
        "bemerkungen": "str"
        }
