import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import requests
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

def speak(text):
    "Convert text to speech."
    engine.say(text)
    engine.runAndWait()

def listen_command():
    "Capture voice input from user and convert to text."
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print(" Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f" You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that. Please say it again.")
        return ""
    except sr.RequestError:
        speak("Network error. Please check your connection.")
        return ""

def tell_time():
    "Tell the current time."
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}")

def tell_date():
    "Tell the current date."
    date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {date}")

def tell_joke():
    "Say a random joke."
    jokes = [
        "Why did the computer show up at work late? It had a hard drive!",
        "Why do Python programmers prefer dark mode? Because light attracts bugs!",
        "What did the spider do on the computer? Made a website!"
    ]
    speak(random.choice(jokes))

def open_website(site_name):
    "Open common websites."
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://github.com",
        "news": "https://www.bbc.com/news"
    }
    if site_name in sites:
        webbrowser.open(sites[site_name])
        speak(f"Opening {site_name}")
    else:
        speak("Sorry, I don't know that website.")

def get_news():
    "Fetch latest headlines from News API (optional free API)."
    api_key = "https://newsapi.org"  # Placeholder 
    speak("Fetching today's news headlines is not available in offline mode, but you can add it using a free API key from newsapi.org.")

def create_note():
    "Save a note to a text file."
    speak("What should I write in your note?")
    note = listen_command()
    if note:
        with open("note.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {note}\n")
        speak("Note saved successfully.")

def main():
    speak("Hello! I am your voice-controlled assistant. How can I help you today?")

    while True:
        command = listen_command()

        if "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "joke" in command:
            tell_joke()
        elif "note" in command or "write" in command:
            create_note()
        elif "open youtube" in command:
            open_website("youtube")
        elif "open google" in command:
            open_website("google")
        elif "open github" in command:
            open_website("github")
        elif "open news" in command:
            open_website("news")
        elif "news" in command:
            get_news()
        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.")
            break
        elif command:
            speak("Sorry, I don’t understand that command yet.")

if __name__ == "__main__":
    main()
