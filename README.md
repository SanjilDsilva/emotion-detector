# Emotion Detector 🤖

This is a simple Python-based emotion detection app that uses a local language model (via Ollama) to identify the emotions in a given sentence.

## 💻 Features
- Local LLM-powered emotion analysis
- No internet/API required (runs via Ollama)
- User-friendly CLI interface

## 🚀 How to Run

1. Clone the repo:

git clone https://github.com/SanjilDsilva/emotion-detector.git
cd emotion-detector

2. Set up the virtual environment:

python -m venv venv
.\venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Start Ollama (if not already running):

ollama run llama3

5. Run the app:

python emotion_detector.py


## ✍️ Example Input

I miss my friend a lot today.
Detected emotions: Sadness


## 🛠 Built With
- Python
- Ollama
- Llama3

## 📄 License
MIT License

---

Made with ❤️ by [Sanjil Dsilva](https://github.com/SanjilDsilva)