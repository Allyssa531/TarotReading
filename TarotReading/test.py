
import streamlit as st
import json
from random import randint, choice

if "rand_num" not in st.session_state:
    st.session_state.rand_num = None
if "card_direction" not in st.session_state:
    st.session_state.card_direction = None
filepath = "TarotReading\\decks\\tarot-rw.json"
with open(filepath, 'r', encoding='utf-8') as fp:
    rw_deck = json.load(fp)
hoodoo = "TarotReading\\decks\\tarot-hoodoo.json"
with open(hoodoo, "r", encoding="utf-8") as fp:
    hoodoo_deck = json.load(fp)
st.title("Tarot Deck")
deck_choice = st.segmented_control("Decks", ["Rider-Waite", "Hoodoo"], default="Rider-Waite")
question = st.text_input("What is your question?")
#st.write(question + deck_choice)
num_of_cards = len(rw_deck)
directions = ["Upright", "Reversed"]
if st.button("Draw a card."):
    st.session_state.rand_num = randint(0, num_of_cards-1)
    st.session_state.card_direction = choice(directions)

card = rw_deck[st.session_state.rand_num]

eq_card = None
for h_card in hoodoo_deck: 
    if h_card["rw-name"] == card["name"]: #if we find the card
        eq_card = h_card
            # print("Card found")
        break

if deck_choice == "Rider-Waite":
    st.write(f"Name: {card["name"]}", st.session_state.card_direction)
    st.write("Qualities: ")

    if card["qualities"]["general"] != "null": 
        st.write(f"General: {card["qualities"]["general"]}")
    st.write(f"Upright: {card["qualities"]["upright"]}")
    st.write(f"Reversed: {card["qualities"]["reversed"]}")

    if len(card["astrology"]) > 0: 
        st.write("Astrology: ")
        st.write(", ".join(sorted(card["astrology"])))

    if len(card["elements"]) > 0:
        st.write("Elements:")
        st.write(*card["elements"], sep=", ")

    st.write(f"Answer: {card["answer"]}")

if deck_choice == "Hoodoo":
  
    if eq_card["major"] == False: 
        st.write(eq_card["name"], st.session_state.card_direction)
        st.write("Plant:", ", ".join(sorted(eq_card["plant"])))
        st.write("Positive Qualities:", eq_card["qualities"]["positive"])
        st.write("Negative Qualities:", eq_card["qualities"]["negative"])
    else:
        st.write(eq_card["name"] )
        st.write("Plant:", ", ".join(sorted(eq_card["plant"])))
        st.write("Verse:", eq_card["verse"])
        st.write("Consider the following:")
        for consideration in eq_card["qualities"]["consideration"]:
            st.write(consideration)


