from os import get_terminal_size
from sys import exit as leave
from tui import Tui


def termsize_check() -> bool:
    termsize: tuple = tuple(get_terminal_size())
    return bool(termsize[0] >= 180 and termsize[1] >= 50)


def main() -> None:
    if not termsize_check():
        leave("Terminal muss mindestens 180x50 sein")

    app: Tui = Tui()
    app.run()


if __name__ == "__main__":
    main()
