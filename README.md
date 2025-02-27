
# 📢 CDP Chatbot  

A **Streamlit-based chatbot** that answers "How-to" questions related to different **Customer Data Platforms (CDPs)**, including **Segment, mParticle, Lytics, and Zeotap**. The chatbot retrieves pre-scraped answers from JSON files and displays responses dynamically with a smooth UI experience.  

## 🚀 Features  

- 📚 **Pre-loaded Answers**: Uses JSON-based data to fetch answers instantly.  
- 🎨 **Enhanced UI**: Color-coded responses with animated text balloons.  
- 🔎 **User-Friendly**: Simple input for selecting CDP and asking questions.  
- ⚡ **Fast & Efficient**: No API calls—everything runs locally for quick responses.  

## 🛠️ Tech Stack  

- **Frontend**: Streamlit  
- **Backend**: Python  
- **Storage**: JSON files  

## 📂 Project Structure  

```bash
📦 CDP-Chatbot
 ┣ 📂 data                 # JSON files containing Q&A for each CDP
 ┃ ┣ 📜 segment.json
 ┃ ┣ 📜 mparticle.json
 ┃ ┣ 📜 lytics.json
 ┃ ┣ 📜 zeotap.json
 ┣ 📜 app.py               # Streamlit application
 ┣ 📜 requirements.txt      # Required dependencies
 ┣ 📜 .gitignore            # Ignore unnecessary files
 ┣ 📜 README.md             # Project documentation
```

## 🎯 How to Run  

### 1️⃣ Clone the repository  

```sh
git clone https://github.com/shreya0626/Chat-bot
cd CDP-Chatbot
```

### 2️⃣ Install dependencies  

```sh
pip install -r requirements.txt
```

### 3️⃣ Run the chatbot  

```sh
streamlit run app.py
```

The chatbot will open in your browser! 🎉  

## 🚀 Deployment  

This chatbot is **deployed on Streamlit Cloud**:  
🔗 [Live Demo](https://shreya0626-chat-bot-app-3wasqc.streamlit.app/)  

## 🤝 Contributing  

Feel free to **fork this repository**, raise issues, or submit pull requests.  



