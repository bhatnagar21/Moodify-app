# moodify_streamlit.py

import streamlit as st
from textblob import TextBlob

# --- Set Page Config ---
st.set_page_config(page_title="Moodify Pro – Web", page_icon="🎧")

# --- Songs Playlist Dictionary ---
mood_playlists = {
    "excited": [
        ("Gallan Goodiyan 😄", "https://youtu.be/jCEdTq3j-0U"),
        ("Chunnari Chunnari 🌞", "https://youtu.be/6z1U-kJ3xJE"),
        ("Kar Gayi Chull 💃", "https://youtu.be/-Tdu4uKSZ3M"),
        ("Saturday Saturday 🕺", "https://youtu.be/Hxt3YbQKW4w")
    ],
    "sad": [
        ("Hamari Adhuri Kahani 💔", "https://youtu.be/sVRwZEkXepg"),
        ("Tujhe Bhula Diya 💧", "https://youtu.be/mt8YgPcQe6E"),
        ("Agar Tum Saath Ho 😢", "https://youtu.be/xRb8hxwN8lY"),
        ("Bekhayali 😭", "https://youtu.be/DHhSDbTY9X8")
    ],
    "neutral": [
        ("Humna Mere 🎧", "https://youtu.be/TmRgK-pXH9c"),
        ("Lut Gaye 🎵", "https://youtu.be/sCbbMZ-q4-I"),
        ("Raabta 🎼", "https://youtu.be/0G2VxhV_gXM"),
        ("Tera Zikr 🎶", "https://youtu.be/GAy3lFbgD2U")
    ],
    "disappointed": [
        ("Kyun Main Jaagoon 😞", "https://youtu.be/yHqp0KE7U8s"),
        ("Zarurat 😔", "https://youtu.be/VMEXKJbsUmE"),
        ("Thoda Sa Tu 😟", "https://youtu.be/9oRsJL3sILc"),
        ("Khairiyat 💭", "https://youtu.be/Jn8qR18jI9E")
    ],
    "love": [
        ("Perfect 💖", "https://youtu.be/2Vv-BfVoq4g"),
        ("Jeena Laga Hoon 💞", "https://youtu.be/qpIdoaaPa6U"),
        ("Tum Hi Ho ❤️", "https://youtu.be/Umqb9KENgmk"),
        ("Raatan Lambiyan 💕", "https://youtu.be/gvyUuxdRdR4")
    ]
}

# --- Mood Detection Logic ---
def detect_mood(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.7:
        return "excited"
    elif 0 < polarity <= 0.5:
        return "love"
    elif polarity == 0:
        return "neutral"
    elif -0.5 < polarity < 0:
        return "disappointed"
    return "sad"

# --- UI ---
st.title("🎧 Moodify Pro – AI Mood Music Recommender")
st.markdown("Type your feelings below and get song recommendations based on your **mood** ✨")

user_input = st.text_area("🗣️ How are you feeling today?", height=150)

if st.button("🔍 Analyze Mood"):
    if not user_input.strip():
        st.warning("Please enter your feelings to analyze.")
    else:
        mood = detect_mood(user_input)
        st.success(f"🎯 Detected Mood: **{mood.capitalize()}**")

        st.subheader("🎵 Recommended Songs For You:")
        for title, url in mood_playlists.get(mood, []):
            st.markdown(f"- [{title}]({url})")

st.markdown("---")
st.caption("🔗 Developed with ❤️ using Python + Streamlit")



