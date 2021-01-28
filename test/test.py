from joke.jokes import *
import pyttsx3

import time

# joke = icanhazdad()

# engine = pyttsx3.init()
# engine.say(str(jokee))
# engine.runAndWait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
index = 0

# v = [0, 2, 16, 30, 35, 52, 61, 62]

v = [22]
memes = [7, 22, 68]

for voice in voices:
    # joke = icanhazdad()
    if(index in v): 
        print(f'index-> {index} -- {voice.name}')
        engine.setProperty('voice', voice.id)
        engine.say(f"I am Brew in bot and I am the best around")
        engine.runAndWait()
        index += 1
   


# Alex(2), Agnes(0), Daniel(16), Karen (30), Lee(35),  Samantha(52), Victoria (62), Vicki (61)
# Good News, Bad News, Zarvox (68)

Bad News - 7
Bells - 9
Boing - 10
Bubbles - 12
Cellos - 14
Good News - 22 (sing)
Pipe Organ - 48
Trinoids - 59
Whisper - 63
Zarvox - 68



# Sing feature -- change voice

# Karen, Daniel
# Daniel
# Samantha, Victoria

# Alex, Daniel, Vicki, Lee, 

# Alex, Daniel, Karen
# Marshall QIAN to Everyone (2:09 PM)
# Daniel, Lee, Vicki
# Rebecca Celsi to Everyone (2:09 PM)
# Alex, Victoria, Daniel
# ZACHARY YUAN to Everyone (2:09 PM)
# Daniel, Samantha
# Hayato Kato to Everyone (2:09 PM)
# Daniel, Vicki, Karen
# Matthew Lacaire to Everyone (2:09 PM)
# Daniel, Karen, Samantha
# Nicholas Zhao to Everyone (2:12 PM)
# I like Alex is the best tbh