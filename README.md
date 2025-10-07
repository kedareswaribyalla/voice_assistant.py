## Voice-Assistant

## Objective:
To create an intelligent voice-controlled assistant that listens to user commands and performs various tasks automatically.

## Tools Used:
# Python

speech_recognition – to capture voice and convert it into text
pyttsx3 – to convert text responses into speech (offline)
os – to perform system-level tasks
webbrowser – to open web pages

## Steps Involved in Building the Project:

- Imported the required libraries.
- Captured audio input using speech_recognition.
- Converted the captured voice into text commands.
- Mapped text commands to system actions (like opening Google or YouTube).
- Used pyttsx3 to give spoken responses to the user.
- Added a continuous loop to keep the assistant listening for commands.
- Included an “exit” or “stop” command to end the session.

## How to Run the Project:

## Install dependencies
- pip install speechrecognition pyttsx3 pyaudio

## Note: If pyaudio installation fails, use
- pip install pipwin
- then pipwin install pyaudio

## Run the script:
- python voice_assistant.py

## Speak your commands — the assistant will respond and act accordingly.
# Example Commands:

- Open Google
- Play music
- What time is it
- Tell me a joke
- Exit

## Deliverables
Python Script (voice_assistant.py)
