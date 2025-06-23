import tkinter as tk
import customtkinter as ctk
import subprocess
import pyttsx3
import threading
import re, subprocess

# Initialize TTS engine
engine = pyttsx3.init()

def query_ollama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "tinyllama"],  # Make sure model is correct
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120
        )

        output = result.stdout.decode("utf-8", errors="ignore").strip()
        lines = output.splitlines()
        clean_lines = [line for line in lines if line.strip() != "" and not line.lower().startswith("download")]
        final_output = "\n".join(clean_lines)

        return final_output if final_output else "No response received."
    except Exception as e:
        return f"Error from Ollama: {e}"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# GUI Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x500")
app.title("AI Assistant")

# Widgets
mode_var = tk.StringVar(value="Text + Speech")
mode_menu = ctk.CTkOptionMenu(app, values=["Text only", "Speech only", "Text + Speech"], variable=mode_var)
mode_menu.pack(pady=10)

chat_frame = ctk.CTkTextbox(app, wrap="word", state="disabled")
chat_frame.pack(padx=10, pady=10, fill="both", expand=True)

input_frame = ctk.CTkFrame(app)
input_frame.pack(padx=10, pady=10, fill="x")

user_input = ctk.CTkEntry(input_frame)
user_input.pack(side="left", fill="x", expand=True, padx=(0,10))
send_btn = ctk.CTkButton(input_frame, text="Send", width=80)

# Behavior
def add_chat(sender, msg):
    chat_frame.configure(state="normal")
    chat_frame.insert("end", f"{sender}: {msg}\n\n")
    chat_frame.configure(state="disabled")
    chat_frame.see("end")

def on_send():
    text = user_input.get().strip()
    if not text:
        return
    add_chat("You", text)
    user_input.delete(0, "end")

    if text.lower() == "exit":
        app.quit()
        return

    mode = mode_var.get()
    def task():
        response = query_ollama(text)
        add_chat("Assistant", response)
        if mode in ("Speech only", "Text + Speech"):
            speak(response)
    threading.Thread(target=task, daemon=True).start()

send_btn.configure(command=on_send)
send_btn.pack(side="right")

# Run
app.mainloop()