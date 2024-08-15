from googletrans import Translator


# Initialize the translator
translator = Translator()


# Translate a Spanish text to English (by default)
translation = translator.translate("Hello World", dest="fr") #   ("Hello World" , dest="es")   #("Hola Mundo", dest="en")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
print(f"{translation.origin}")
print(f"{translation.text}")
