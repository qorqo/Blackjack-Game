suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random

player_cards = []

house_cards = []
#creates a new, ordeted deck
def form_deck() -> list:
    deck = []

    for elem in suits:

        for i in range(1, 14):

            match i:
                case 1: deck.append((elem, 'A', 11))

                case 11: deck.append((elem, 'J', 10))

                case 12: deck.append((elem, 'Q', 10))

                case 13: deck.append((elem, 'K', 10))

                case _: deck.append((elem, i as char, i))

    return deck

#adds additional decks n to an existing deck, assumes input is already a deck
def add_decks(in_deck: list, n: int):
    
    for i in range(n):
        new_deck = form_deck()
        for elem in new_deck:
            in_deck.append(elem)


def deal_cards(in_deck: list):
    player_cards.append(in_deck.pop())
    house_cards.append((in_deck.pop(), True))
    player_cards.append(in_deck.pop())
    house_cards.append((in_deck.pop(), True))
deck = form_deck()

add_decks(deck, 3)

random.shuffle(deck)

print(deck)
deal_cards(deck)
