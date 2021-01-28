from joke.jokes import *
import pyttsx3
import time

def file_read():
    with open('filename.txt', 'r') as file:
        data = file.read().replace('\n', '')
    return data



def parser():
    inp = file_read()
    words = inp.split()
    weather_words = ['weather', 'whether', 'temperature', 'climate', 'sun', 'sunny']
    joke_words = ['joke','tell', 'humour', 'laugh']
    dance_words = ['dance', 'move', 'spin']
    goodbye_words = ['bye', 'goodbye', 'later']

    engine = pyttsx3.init()

    for word in words:
        if(word in weather_words):
            weather(engine)
        elif(word in joke_words):
            joke(engine)
        elif(word in dance_words):
            dance(engine)
        elif(word in goodbye_words):
            goodbye(engine)
    return

def joke(engine):
    joke = icanhazdad()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')
    engine.say(joke)
    engine.runAndWait()

def main():
    engine = pyttsx3.init()
    
    parser()
    

if __name__ == "__main__":
    main()