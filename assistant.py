import speech_recognition as sr
import pyttsx3
import subprocess

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def query_ollama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.2:latest"],  # Make sure model is correct
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )

        output = result.stdout.decode("utf-8", errors="ignore").strip()
        lines = output.splitlines()
        clean_lines = [line for line in lines if line.strip() != "" and not line.lower().startswith("download")]
        final_output = "\n".join(clean_lines)

        return final_output if final_output else "No response received."
    except Exception as e:
        return f"Error from Ollama: {e}"

# Mode selection
mode = input("Choose interaction mode (voice/text): ").strip().lower()

# Main loop
while True:
    if mode == "voice":
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            speak("Listening for your command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            speak(f"You said: {command}")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand your voice.")
            continue
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            continue

    elif mode == "text":
        command = input("You: ")

    else:
        print("Invalid mode. Please restart the script and choose 'voice' or 'text'.")
        break

    # Exit check
    if command.lower() in ["exit", "quit", "bye"]:
        speak("Goodbye!")
        break

    # Get response from Ollama
    response = query_ollama(command)
    speak(response)