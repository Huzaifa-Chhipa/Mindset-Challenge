import streamlit as st
import random

quotes = [
    "Mistakes are proof that you are trying.",
    "The harder you work, the luckier you get.",
    "Every expert was once a beginner.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Don’t stop until you’re proud.",
    "Your only limit is your mindset.",
    "Growth begins when we start to accept our weaknesses.",
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "The only way to grow is to step out of your comfort zone.",
    "Believe you can, and you’re halfway there."
]

st.title("Growth Mindset Motivational Quotes 💪")
st.write("Create a new habit every time and strengthen your growth mindset!")

if st.button("Generate Quote"):
    random_quote = random.choice(quotes)
    st.success(random_quote)

st.header("Save your favourite Qoutes")
favorite_quote = st.text_input("You add your favourite Qoute:")
if st.button("Save Quote"):
    if favorite_quote:
        st.session_state.favorites = st.session_state.get("favorites", []) + [favorite_quote]
        st.success("Quote saved!")

if st.session_state.get("favorites"):
    st.header("Your Favorite Quotes")
    for i, quote in enumerate(st.session_state.favorites, 1):
        st.write(f"{i}. {quote}")