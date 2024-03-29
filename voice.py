import speech_recognition as sr
import pyttsx3
import time
from joke.jokes import *
import requests, json
import pytemperature
import random
import pafy
import vlc
import os
import makeRequest

# pyttsx3 is not compatible with kivy for Mac so say is used instead for speech
onMac = False
if onMac:
    from say import *


#listend to incoming audio and returns recognized text
def speech_recognition(recognizer, microphone):
    
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        print("Listening...")
        # recognizer.adjust_for_ambient_noise(source)
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


#function that speaks out a given string
def speak(command):
    microphone = sr.Microphone()
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english')
    engine.setProperty('rate', 130)
    engine.say(command)
    if(onMac):
        os.system(f"say {command}")
    else:
        engine.runAndWait()

#Takes in a string input command and responds to that command
#If command is "" or "Press To Speak To BruinBot" calls speech_recognition 
#   function to listen to user audio input
def parser(button_input=""):
    weather_words = ['weather', 'weather?', 'whether', 'temperature', 'climate', 'sun', 'sunny']

    joke_words = ['joke','tell', 'humour', 'laugh']
    dance_words = ['dance', 'dance!', 'move', 'spin']
    goodbye_words = ['bye', 'goodbye', 'later']
    self_words = ['you', 'you?']
    sing_words = ['sing', 'Sing'] #check if case matters
    music_words = ['music']
    age_words = ['age', 'old']
    facts_words = ['fact', 'interesting']
    game_words = ['game', 'game.', 'guess']
    facts_list = [ #list of all fun facts available for bruinbot to say
        "Gene Block is 72 years young",
        "UCLA is 101 years old"
        ]
    music_list = [  #urls to youtube videos bruinbot will play as audio
        #entries in music list are of the form ("Youtube URL", StartingTime, RunTime)
        ("https://www.youtube.com/watch?v=dQw4w9WgXcQ",42.5, 9) # "Never Gonna Give You Up", Rick Astley, 18.4 for full chorus, 9 for first half of chorus
    ]
    # Sing feature - Goodnews(22)
    # Play Music - gmusicapi, vlc
    # Age
    # Interesting Facts about UCLA, ASME, Gene Block
    # Guess the number game

    weather_api_key = "2dfe2376a8e9b86b3e835b7abaac64cf"

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    

    if(button_input=="Press To Speak To BruinBot" or button_input== ""):
        action = speech_recognition(recognizer, microphone)
        try: 
            words = action['transcription'].split()
        except AttributeError:
            words = ['']
    else:
        action = {
        "success": True,
        "error": None,
        "transcription": button_input
        }

        words = action['transcription'].split()

    print("You said: {}".format(action["transcription"]))
    for word in words:
        if(word in weather_words):
            action_taken = True
            city = "Los Angeles"
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
            response = requests.get(weather_url)
            current_weather = response.json()
            temperature = pytemperature.k2f(current_weather["main"]["temp"])
            return f"In Los Angeles, it is currently {temperature} degrees farenheit"
        elif(word in joke_words):
            joke = icanhazdad()
            engine = pyttsx3.init()
            makeRequest.callEmotion("happy_emphasis")
            return f'Here is a joke - {joke}'
        elif(word in dance_words):
            return "I like to dance"
        elif(word in goodbye_words):
            return "See ya"
        elif(word in self_words):
            return "I am Brew in bot. I am immortal. Pleased to meet you."
        elif (word in sing_words):
            lyrics = "I am Brew in bot. I am an immortal. Nice to meet you."
            return lyrics
        elif(word in music_words):
            return "This is one of my favorite songs. I hope you enjoy."
        elif (word in age_words):
            min_age = 0
            max_age = 186
            age = random.randint(min_age, max_age)
            return f"I am {age} years old"
        elif (word in facts_words):
            fact = random.choice(facts_list)
            return fact
        elif(word in game_words):
            return "Lets play a game"

    if action["error"]:
        print("ERROR: {}".format(action["error"]))

    return "I did not understand that, please try again"     

def button(sentence):
    weather_words = ['weather', 'whether', 'temperature', 'climate', 'sun', 'sunny']
    joke_words = ['joke','tell', 'humour', 'laugh']
    dance_words = ['dance', 'move', 'spin']
    goodbye_words = ['bye', 'goodbye', 'later']
    self_words = ['you']
    sing_words = ['sing', 'Sing'] #check if case matters
    music_words = ['music']
    age_words = ['age', 'old']
    facts_words = ['fact', 'interesting']
    game_words = ['game', 'guess']
    facts_list = [ #list of all fun facts available for bruinbot to say
        "Gene Block is Old",
        "UCLA is 101 years old"
        ]
    music_list = [  #urls to youtube videos bruinbot will play as audio
        #entries in music list are of the form ("Youtube URL", StartingTime, RunTime)
        ("https://www.youtube.com/watch?v=dQw4w9WgXcQ",42.5, 18.7)
    ]
    # Sing feature - Goodnews(22)
    # Play Music - gmusicapi, vlc
    # Age
    # Interesting Facts about UCLA, ASME, Gene Block
    # Guess the number game
    
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')

    weather_api_key = "2dfe2376a8e9b86b3e835b7abaac64cf"

    action = sentence
    words = action.split()
    print("You said: {}".format(action))
    for word in words:
        if(word in weather_words):
            city = "Los Angeles"
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
            response = requests.get(weather_url)
            current_weather = response.json()
            temperature = pytemperature.k2f(current_weather["main"]["temp"])
            engine.say(f"In Los Angeles, it is currently {temperature} degrees farenheit")
            break
        elif(word in joke_words):
            joke = icanhazdad()
            engine = pyttsx3.init()
            engine.say(f'Here is a joke - {joke}')
            break
        elif(word in dance_words):
            engine.say("I like to dance")
            break
        elif(word in goodbye_words):
            engine.say("See ya")
            break
        elif(word in self_words):
            engine.say("I am Brew in bot. I am immortal. Pleased to meet you.")
            break
        elif (word in sing_words):
            engine.setProperty('voice', 'com.apple.speech.synthesis.voice.goodnews')
            lyrics = "I am Brew in bot. I am an immortal. Nice to meet you."
            engine.say(lyrics)
            engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')
            break
        elif(word in music_words):
            engine.say("This is one of my favorite songs. I hope you enjoy.")
            engine.runAndWait()
            song = random.choice(music_list)                                                                                       
            video = pafy.new(song[0])                                                                                                           
            best = video.getbestaudio()                                                                                                                 
            playurl = best.url                                                                                                                        
            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(playurl)
            Media.add_option(f"start-time={song[1]}")
            Media.add_option(f"run-time={song[2]}") 
            player.set_media(Media)
            player.play()
            time.sleep(song[2])
            break
        elif (word in age_words):
            min_age = 0
            max_age = 186
            age = random.randint(min_age, max_age)
            engine.say(f"I am {age} years old")
            break
        elif (word in facts_words):
            fact = random.choice(facts_list)
            engine.say(fact)
            break
        elif(word in game_words):
            engine.say("Lets play a game")
            guessingGame()
            break
    return engine.runAndWait()
    
        

def guessingGame():
    NUM_GUESSES = 2
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    min = 1
    max = 10
    answer = random.randint(min, max)
    engine.say(f"I'm thinking of a number from {min} to {max}. See if you can guess it")
    engine.runAndWait()
    while(NUM_GUESSES > 0):
        action = speech_recognition(recognizer, microphone)
        try: 
            words = action['transcription'].split()
        except AttributeError:
            words = ['']
        nums = {"one": 1, "1": 1, "two": 2, "2": 2, "to": 2, "too": 2, "three": 3, "3": 3, "four": 4, "4": 4, "for": 4, "five": 5, "5": 5,
        "5:00":5, "six": 6, "6": 6,"seven":7, "7":7, "eight":8, "8":8, "ate":8, "nine":9, "9":9, "ten":10, "10":10
        }
        made_guess = False #indicates if user made a proper guess this turn
        for word in words:
            guess = nums.get(word, -1)
            if guess != -1:  #if user guessed a number compare to bruinbots number 
                if guess == answer:
                    engine.say(f"Thats correct, {answer} was my number.")
                    NUM_GUESSES = 0
                else:
                    if NUM_GUESSES == 1:  #if this is the final guess say losing message
                        engine.say(f"Sorry, I was thinking of the number {answer}. Better luck next time.")
                    elif answer>guess: #if first guess give hint and allow another guess
                        engine.say(f"My number is greater than {guess}. I'll give you one more guess")
                    else:
                        engine.say(f"My number is less than {guess}. I'll give you one more guess")
                NUM_GUESSES -= 1
                made_guess = True
                break
        if not made_guess:
            engine.say(f"Try guessing a number from {min} to {max}")
        print("You said: {}".format(action["transcription"]))
        return engine.runAndWait()



if __name__ == "__main__":
    parser()
    





