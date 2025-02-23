import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Initialize Text-to-Speech Engine
def speak(response):
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

# Listen for Voice Commands
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""
        except sr.RequestError:
            print("Speech service is unavailable.")
            return ""

# Execute Commands
def execute_command(command):
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "play music" in command:
        speak("Playing music")
        os.system("start spotify")  # Modify this line if you're not using Windows

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I didn't understand that.")

# Main Loop
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you?")
    
    while True:
        command = listen_command()
        if command:
            execute_command(command)
