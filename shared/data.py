version: str = "0.1.0"

mongodb_ascii = r"""
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

help_text = """
Willkommen, die navigation funktioniert wie folgt:
    - Tab zum auswählen der Buttons (nächster)
    - Shift Tab zum auswählen der Buttons (vorheriger)
    - Enter um einen Button zu klicken
    - Control+Q um das Programm zu beenden
    - Escape um zum Hauptmenu zurückzugelangen
    - Der Mauszeiger kann auch verwendet werden
"""

collection_fields = ["name", "art", "jahr",
                     "regisseur", "schauspieler",
                     "rating", "min_alter", "bemerkungen"]
