import speech_recognition as sr
import pyttsx3
import datetime

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

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
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I am having trouble connecting to the internet.")
            return ""

def run_assistant():
    while True:
        command = listen_command()

        if 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")
        
        elif 'stop' in command or 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

        elif command != "":
            speak("Sorry, I can't help with that yet.")

run_assistant()
