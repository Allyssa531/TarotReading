from random import randint
import json

filepath = "TarotReading\\decks\\tarot-rw.json"


print("Pick a card...")
with open(filepath, "r", encoding="utf-8") as fp:
    cards = json.load(fp)
num_of_cards = len(cards)
card_num = randint(0, num_of_cards)
card = cards[card_num]

print(f"Name: {card["name"]}")
print("Qualities: ")
print(f"General: {card["qualities"]["general"]}")
print(f"Upright: {card["qualities"]["upright"]}")
print(f"Reversed: {card["qualities"]["reversed"]}")
print("Astrology: ")
for item in card["astrology"]:
    print(item)
print("Elements: ")
for item in card["elements"]:
    print(item)
print(f"Answer: {card["answer"]}")


