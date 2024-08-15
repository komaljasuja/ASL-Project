import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


word_to_speak = "Salut tout le monde"
speak(word_to_speak)
