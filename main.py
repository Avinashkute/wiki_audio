import pyttsx3
import speech_recognition as sr
import wikipedia

listner= sr.Recognizer()
engine = pyttsx3.init()
engine.say('Hey i am Bantiii')
engine.say('What can i do for u')
engine.runAndWait()

try:
    with sr.Microphone() as source:
        engine.say('Say something')
        engine.runAndWait()
        print('Listening...')
        voice=listner.listen(source)
        command=listner.recognize_google(voice)
        command=command.lower()
        print(command)
        result = wikipedia.summary(f"{command}", sentences=2)
        print(result)
        engine.say(result)
        engine.runAndWait()
except:
    engine.say('Something went wrong')
    engine.runAndWait()





                




