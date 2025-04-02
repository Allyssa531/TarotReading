import json


filename = "TarotReading\\decks\\tarot-hoodoo.json"
cards = None
with open(filename, "r", encoding="utf-8") as fp:
	cards = json.load(fp)

filtered_cards = {card["name"]: card for card in cards}

with open(filename, "w", encoding="utf-8") as out:
	json.dump(fp=out, obj=list(filtered_cards.values()), indent="\t")















