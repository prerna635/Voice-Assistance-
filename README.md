# 🎙️ Voice Assistant using Python

This is a simple **Voice Assistant** built with Python that can recognize your voice, understand basic commands, and speak back responses.

It uses:
- `speech_recognition` for speech input
- `pyttsx3` for voice output (text-to-speech)
- `datetime` for telling the current time

---

## 🚀 Features

- 🎧 Listens to your voice commands
- 🕒 Tells the current time when you say things like:
  - “What is the time?”
  - “Tell me the time”
- ❌ Stops the assistant when you say:
  - “Stop”
  - “Exit”
  - “Quit”
- 🤖 Responds with a default message if it doesn't understand the command

---

## 🛠️ Requirements

Make sure to install the following Python packages:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
