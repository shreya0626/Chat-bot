import streamlit as st
import json
import os
import time

# Set page config
st.set_page_config(page_title="CDP Chatbot", page_icon="🤖", layout="centered")

# Custom CSS for styling and animations
st.markdown(
    """
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .stTextInput, .stSelectbox, .stButton button {
            font-size: 16px;
            padding: 10px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stMarkdown {
            font-size: 18px;
            font-weight: bold;
        }
        .chat-container {
            background-color: #D1E7DD;
            color: #1B5E20;
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 80%;
            margin: 10px 0;
            font-size: 16px;
            opacity: 0;
            animation: fadeIn 1s forwards;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with emoji
st.markdown("<h1 style='text-align: center;'>🤖 CDP Chatbot</h1>", unsafe_allow_html=True)

# Directory containing JSON files
json_dir = "data"  # Adjust if necessary

# Load all JSON files into a dictionary
answers_data = {}

for filename in os.listdir(json_dir):
    if filename.endswith(".json"):
        cdp_name = filename.replace(".json", "")  # Keep original case
        with open(os.path.join(json_dir, filename), "r") as f:
            answers_data[cdp_name] = json.load(f)

# UI layout
st.write("---")
st.subheader("💡 Ask about Customer Data Platforms")

# Dropdown for CDP selection
cdp = st.selectbox("📌 Select a CDP", list(answers_data.keys()))

# Text input for question
query = st.text_input("💬 Ask a question")

# Submit button
if st.button("🔍 Get Answer"):
    if query and cdp:
        # Fetch the answer from the JSON file
        answer = answers_data.get(cdp, {}).get(query, "❌ No direct information found.")

        # Simulate typing effect before displaying answer
        with st.empty():
            for i in range(3):
                dots = "." * (i + 1)
                st.markdown(f"⌛ Fetching answer{dots}")
                time.sleep(0.5)

        # Display the full answer in a single animated chat bubble
        st.markdown("### 📖 Answer:")
        st.markdown(
            f"<div class='chat-container'>{answer}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.warning("⚠️ Please enter a question and select a CDP.")

# Footer
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>❤️ Support Agent Chatbot</h2>", unsafe_allow_html=True)
