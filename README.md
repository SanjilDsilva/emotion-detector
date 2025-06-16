# Emotion Detector (Offline LLM + Python)

This project is an **Emotion Detection Tool** built using a **local LLM (LLaMA3 via Ollama)** and Python. It allows you to enter a sentence and get a prediction of the emotion being expressed in natural language. It's simple, private, and fully offline — no cloud APIs, no token limits.

## ✨ Features

- **Offline inference** using the [Ollama](https://ollama.com) runtime.
- Uses **LLaMA 3 (llama3:8b or llama3:instruct)** for emotion classification.
- Simple terminal-based interface.
- Can detect emotions like *sadness, happiness, anger, optimism,* etc.
- Easy to extend for web, chatbot, or GUI interfaces.

# 🛠 Setup Instructions

## 1. Clone the Repository

git clone https://github.com/SanjilDsilva/emotion-detector.git
cd emotion-detector

## 2. Set Up a Virtual Environment (optional but recommended)

python -m venv venv
venv\Scripts\activate  # On Windows
 source venv/bin/activate  # On Mac/Linux

## 3. Install Dependencies

pip install -r requirements.txt

## 4. Install Ollama and LLaMA3
Download Ollama: https://ollama.com

Run the following to pull the LLaMA3 model:
ollama pull llama3
You can also use llama3:8b or a smaller model like llama3:instruct if system resources are limited.

## 5. Run the App
python emotion_detector.py

## 📁 File Structure

emotion-detector/
├── emotion_detector.py         # Main script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

Built by Sanjil Dsilva using:

Ollama

LLaMA3 model

Python

# 📜 License
This project is licensed under the MIT License. Feel free to use, modify, and share!

## 🧠 Example

```bash
Enter a sentence (or type 'exit'):
>> i miss my friend a lot today.
Detected emotions: Emotion: Sadness

Sentence: "i miss my friend a lot today."

Explanation: The sentence "i miss my friend a lot today" contains emotional words like "miss" and "a lot", indicating a sense of loss or longing — commonly associated with sadness.
