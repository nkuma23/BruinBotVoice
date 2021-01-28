import speech_recognition as sr
import pyttsx3
import time
from joke.jokes import *
import requests, json
import pytemperature

def speech_recognition(recognizer, microphone):
    
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)


    r = sr.Recognizer()

    mic = sr.Microphone()

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def parser():
    weather_words = ['weather', 'whether', 'temperature', 'climate', 'sun', 'sunny']
    joke_words = ['joke','tell', 'humour', 'laugh']
    dance_words = ['dance', 'move', 'spin']
    goodbye_words = ['bye', 'goodbye', 'later']
    self_words = ['you']
    # Sing feature - Goodnews(22)
    # Play Music - gmusicapi, vlc
    # Age
    # Interesting Facts about UCLA, ASME, Gene Block
    # Guess the number game
    PROMPT_LIMIT = 1
    
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')

    weather_api_key = "2dfe2376a8e9b86b3e835b7abaac64cf"

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    while(PROMPT_LIMIT > 0):
        action_taken = False
        action = speech_recognition(recognizer, microphone)
        try: 
            words = action['transcription'].split()
        except AttributeError:
            words = ['']

        for word in words:
            if(word in weather_words):
                action_taken = True
                city = "Los Angeles"
                weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
                response = requests.get(weather_url)
                current_weather = response.json()
                temperature = pytemperature.k2f(current_weather["main"]["temp"])
                engine.say(f"In Los Angeles, it is currently {temperature} degrees farenheit")
                PROMPT_LIMIT -= 1
                break
            elif(word in joke_words):
                joke = icanhazdad()
                engine = pyttsx3.init()
                engine.say(f'Here is a joke - {joke}')
                action_taken = True
                PROMPT_LIMIT -= 1
                break
            elif(word in dance_words):
                engine.say("I like to dance")
                action_taken = True
                PROMPT_LIMIT -= 1
                break
            elif(word in goodbye_words):
                engine.say("See ya")
                action_taken = True
                PROMPT_LIMIT = 0
                break
            elif(word in self_words):
                engine.say("I am Brew in bot. I am immortal. Pleased to meet you.")
                action_taken = True
                PROMPT_LIMIT -= 1
                break
        
        if(action_taken == False):
            engine.say("I did not understand that, please try again")
            
        if action["error"]:
            print("ERROR: {}".format(action["error"]))
            break
        print("You said: {}".format(action["transcription"]))

        engine.runAndWait()
        



if __name__ == "__main__":
    parser()
    





