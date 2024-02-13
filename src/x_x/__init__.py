import os.path
import random


EYES = [
    "x",
    "X",
    "O",
    "o",
    "0",
    "U",
    "u",
    "@",
    "*",
    "^",
    "-",
]


def x_x():
    """Return a random face with an eye."""
    return random.choice(EYES) + "_" + random.choice(EYES)


def splash(choice: str) -> str:
    """Return a splash screen"""

    fname = os.path.join(
        os.path.dirname(__file__),
        "splashes",
        f"{choice}.txt",
    )

    with open(fname, "r") as fi:
        return fi.read()
