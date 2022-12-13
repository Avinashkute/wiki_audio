from django.shortcuts import render

# Create your views here.
import pyttsx3
import speech_recognition as sr
import wikipedia




def start(r):
    listner = sr.Recognizer()
    global engine
    engine = pyttsx3.init()
    engine.say('Hey i am wiki_audio')
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
            engine.stop()

    except:
        engine.say('Something went wrong')
        engine.runAndWait()
        engine.stop()

    return render(r,'thank.html')

def welcome(r):
    return render(r,'base.html/')
def stop(r):
    engine.endLoop()
    return render(r,'base.html/')
