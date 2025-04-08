from random import randint
import json




print("Pick a card...")
with open("tarot-rw.json", "r", encoding="utf-8") as fp:
    cards = json.load(fp)
num_of_cards = len(cards)
card_num = randint(0, num_of_cards)
card = cards[card_num]

print(f"Name: {card["name"]}")
