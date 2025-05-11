# This is the file for the deck

import random

suits  = { # Initializing the suits
    "h": "/Hearts",
    "d": "/Diamonds",
    "s": "/Spades",
    "c": "/Clubs"
}

numbers = [ # Initializing the card values
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
]

def build_deck(): # Defines building the deck
    deck = [number + suit for number in numbers for suit in suits]
    random.shuffle(deck)
    return deck

def cards_drawing():
    card_lines = [
        "     ._____________.     ._____________.     ._____________.     ._____________.",
        "     | J           |     | Q           |     | K   ___     |     | A    _      |",
        "     |      /\\     |     |   .__  __.  |     |    /   \\    |     |    _/ \\_    |",
        "     |     /  \\    |     |   |  \\/  |  |     |   /     \\   |     |   /     \\   |",
        "     |     \\  /    |     |    \\    /   |     |  |__| |__|  |     |   \\_. ._/   |",
        "     |      \\/     |     |     \\__/    |     |     |_|     |     |     |_|     |",
        "     |           J |     |           Q |     |           K |     |           A |",
        "     |_____________|     |_____________|     |_____________|     |_____________|"
    ]
    for line in card_lines:
        print(line)

if __name__ == "__main__":
    build_deck()
    cards_drawing()