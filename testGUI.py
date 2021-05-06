import PySimpleGUI as sg 
import random
import pyttsx3
import voice

def displayGUI():
    # layout = [[sg.Button(f'{row}, {col}') for col in range(4)] for row in range(4)]
    # layout = [[sg.Button(button_text='Press To Speak To BruinBot' ,  image_filename='./button.png', image_size=(420,420), image_subsample=5, border_width=0, button_color=(sg.theme_background_color(),sg.theme_background_color()))
    # ], 
    # [sg.Button(button_text='Press To Speak To BruinBot' ,  image_filename='./button.png', image_size=(300,300), image_subsample=5, border_width=0, button_color=(sg.theme_background_color(),sg.theme_background_color()))],
    # [sg.Button('Who are you'),
    # sg.Button('Tell me a fun fact'), sg.Button('Whats the weather')]]
    commandList = ["Whats the weather?", "Do a dance!", "Sing a song", "Play music", "How old are you", "Tell me a fun fact"]
    random_commands = random.sample(commandList, 3)
    sg.SetOptions(
                 button_color = sg.COLOR_SYSTEM_DEFAULT
               , text_color = 'black'
             )
    layout = [
        [sg.Button(button_text="Who are you ?" , image_size=(240, 100), image_subsample=10, border_width=0),
        sg.Button(button_text="Lets play a game", image_size=(240, 100), image_subsample=10, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())),
        sg.Button(button_text="Tell me a joke", image_size=(240, 100), image_subsample=10, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()))],
        [sg.Button(button_text="Press To Speak To BruinBot", image_filename='./images/button.png', image_size=(180, 180), image_subsample=7, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()))],
        [sg.Button(button_text=random_commands[0], image_size=(240, 100), image_subsample=10, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())),
        sg.Button(button_text=random_commands[1], image_size=(240, 100), image_subsample=10, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())),
        sg.Button(button_text=random_commands[2], image_size=(240, 100), image_subsample=10, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()))]
    ]

    #pressToStart = [[sg.Button('Press To Speak To BruinBot', size=(500,500), image_filename='./button_smallest.png', image_size=(500,500))]]
    #isClicked = sg.Window('Speak to BruinBot', pressToStart, no_titlebar=True).read(close=True)
    event, values = sg.Window('Speak to BruinBot', layout, no_titlebar=True, element_justification='c').read()
    #event = sg.Window('Speak to BruinBot', layout).read(close=True)
    #window = sg.Window('My window', layout, no_titlebar=True, alpha_channel=0.5)
    voice.button(event)
    #print(values)

if __name__ == "__main__":
    displayGUI()
