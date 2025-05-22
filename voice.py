import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Speak the word "Hello"
engine.say("Hello")
engine.runAndWait()