# 🤖 Jarvis AI Assistant

**Jarvis** is a voice-activated AI assistant built in Python.  
It can open websites, fetch live news, play Quran translations, and intelligently answer questions using the **Google Gemini API**.

---

## 🧠 Features
- 🎙️ Voice activation with the wake word **"Jarvis"**
- 💬 AI responses powered by **Gemini API (Free Google LLM)**
- 📰 Live news fetching via **NewsAPI**
- 📖 Quran translation playback from YouTube
- 🔊 Natural voice output using **Google gTTS**
- 🌐 Web automation (opens Google, YouTube, X, LinkedIn, etc.)

---

## ⚙️ Tech Stack
**Language:** Python  
**Libraries:** `speechrecognition`, `gtts`, `requests`, `python-dotenv`  
**APIs Used:** Gemini API, NewsAPI  

---

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Jarvis-AI.git
   cd Jarvis-AI


2. **Create a virtual environment**

python -m venv Jarvisenv
source Jarvisenv/Scripts/activate   # (Windows)
# or
source Jarvisenv/bin/activate       # (Mac/Linux)

3. **Install Dependencies**
pip install -r requirements.txt

4. **Set up environment variables**

Create a .env file in the root folder:

GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_news_api_key

5. **Finally Run the assistant**
python main.py

**🧑‍💻Author: Moeed Khan**

Built as part of a hands-on DataScience & Python learning journey.
Feel free to fork, improve, or contribute!