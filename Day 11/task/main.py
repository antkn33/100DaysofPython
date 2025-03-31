import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards(player):
    card1 = 0
    card2 = 0
    card1 = (random.choice(cards))
    card2 = (random.choice(cards))
    total_cards = card1 + card2
    if total_cards == 21:
        return f"{player} scored 21. They win!"
    else:
        return f"{player} Cards: {card1}, {card2}. For a total of: {total_cards}."

print(deal_cards("User"))

print(deal_cards("Dealer"))


