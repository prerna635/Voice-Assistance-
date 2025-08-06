import speech_recognition as sr
import pyttsx3
import datetime
import os
import sys

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except:
            speak("Sorry, I did not understand that.")
            return ""

def run_assistant():
    while True:
        command = listen_command()

        if "hello" in command or "hi" in command:
            speak("Hello! How can I assist you?")
        elif "your name" in command:
            speak("I am your voice assistant.")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}.")
        elif "date" in command:
            today = datetime.datetime.now().strftime("%A, %d %B %Y")
            speak(f"Today is {today}.")
        elif "open notepad" in command:
            speak("Opening Notepad.")
            os.system("notepad.exe")
        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        elif command:
            speak("Sorry, I can't help with that yet.")

run_assistant()
