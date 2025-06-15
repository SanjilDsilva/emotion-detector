import subprocess
import json

def get_emotion_from_ollama(text):
    # Custom prompt for better emotion extraction
    prompt = f"""
    Analyze the following sentence and return the top 3 emotions it expresses. 
    Only return a list of emotions, no explanation.

    Sentence: "{text}"
    """

    # Run Ollama model using subprocess
    result = subprocess.run(
        ["ollama", "run", "tinyllama"],  # you can replace "mistral" with "tinyllama" or "gemma:2b"
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output = result.stdout.decode("utf-8").strip()
    return output

# Main loop
print("Enter a sentence (or type 'exit'):")
while True:
    user_input = input(">> ")
    if user_input.lower() == "exit":
        break
    emotions = get_emotion_from_ollama(user_input)
    print(f"Detected emotions: {emotions}\n")