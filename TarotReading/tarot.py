from random import randint, choice
import json

filepath = "TarotReading\\decks\\tarot-rw.json"

question = input("What's your question? ")
print("Pick a card...")
with open(filepath, "r", encoding="utf-8") as fp:
    rw_deck = json.load(fp)
# rw_deck = list(filter(lambda c: len(c["astrology"]) > 1, rw_deck))
num_of_cards = len(rw_deck)
card_num = randint(0, num_of_cards-1)
card = rw_deck[card_num]

directions = ["Upright", "Reversed"]

print(f"Name: {card["name"]}", choice(directions))
print("Qualities: ")

if card["qualities"]["general"] != "null":
    print(f"General: {card["qualities"]["general"]}")
print(f"Upright: {card["qualities"]["upright"]}")
print(f"Reversed: {card["qualities"]["reversed"]}")


if len(card["astrology"]) > 0:
    print("Astrology: ")
    print(", ".join(sorted(card["astrology"])))

if len(card["elements"]) > 0:
    print("Elements:")
    print(*card["elements"], sep=", ")

print(f"Answer: {card["answer"]}")















hoodoo = "TarotReading\\decks\\tarot-hoodoo.json"
with open(hoodoo, "r", encoding="utf-8") as fp:
    hoodoo_deck = json.load(fp)
eq_card = None
for h_card in hoodoo_deck: 
    if h_card["rw-name"] == card["name"]: #if we find the card
        eq_card = h_card
        print("Card found")
        break
#print hoodoo deck name
if eq_card["major"] == False: 
    print("Plant:", eq_card["plant"])
    print("Positive Qualities:", eq_card["qualities"]["positive"])
    print("Negative Qualities:", eq_card["qualities"]["negative"])
else:
    print("Plant:", eq_card["plant"])
    print("Verse:", eq_card["verse"])
    print("Consider the following:", eq_card["qualities"]["consideration"])




    
