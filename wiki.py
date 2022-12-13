import wikipedia
import pyttsx3
engine=pyttsx3.init()
result = wikipedia.summary("Mahatma Gandhi", sentences = 2)
engine.say(result)
engine.runAndWait()
