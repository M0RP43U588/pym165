version: str = "1.0.0"

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
    - Tab um das nächste Element zu fokusieren
    - Shift Tab um das vorherig Element zu fokusieren
    - Enter um einen Button zu klicken oder einen Input zu bestätigen
    - Control+Q um das Programm zu beenden
    - Escape um zum Hauptmenu zurückzugelangen
    - Der Mauszeiger kann auch verwendet werden
"""

collection_fields: list[str] = [
        "name", "art", "jahr",
        "regisseur", "schauspieler",
        "rating", "min_alter", "bemerkungen"
        ]

collection_fields_to_types_fake: set[str, str] = {
        "name": "str",
        "art": "str",
        "jahr": "int",
        "regisseur": "str",
        "schauspieler": "str",
        "rating": "float",
        "min_alter": "int",
        "bemerkungen": "str"
        }

field_info_string = "name, art, jahr, regisseur, schauspieler, rating, min_alter, bemerkungen"

filter_type = dict[str, str | int | float]

actual_doc_type = dict[str, str | int | float | list[str, ...]]
