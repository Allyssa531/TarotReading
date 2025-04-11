import json

with open("TarotReading\\decks\\tarot-hoodoo.json", "r", encoding="utf-8") as fp:
	hd_cards = json.load(fp)
with open("TarotReading\\decks\\tarot-rw.json", "r", encoding="utf-8") as fp:
	rw_cards = json.load(fp)


cards = {suit: set() for suit in ["knives", "sticks", "baskets", "coins", "major"]}


for hd_card in hd_cards:
	for suit in cards.keys():
		if suit.lower() in hd_card["name"].lower():
			cards[suit].add(hd_card["name"])
			break
	else:
		cards["major"].add(hd_card["name"])



total = 0
print("Cards:")
for suit in ["knives", "sticks", "baskets", "coins", "major"]:
	print("#"*25)
	print(f"Suit: {suit}")
	sub_deck = cards[suit]
	print(f"Count: {len(sub_deck)}")
	total += len(sub_deck)
	for card_name in sorted(sub_deck):
		print(card_name)
print(f"Total: {total}")










