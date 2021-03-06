import PySimpleGUI as sg 
import random
import voice

def displayGUI():
    layout = [[sg.Button(f'{row}, {col}') for col in range(4)] for row in range(4)]
    layout = [[sg.Button(button_text='Press To Speak To BruinBot' ,  image_filename='./button.png', image_size=(420,420), image_subsample=5, border_width=0, button_color=(sg.theme_background_color(),sg.theme_background_color()))
    ], # sg.Button('Play some music'), sg.Button('How old are you')],
    [sg.Button(button_text='Press To Speak To BruinBot' ,  image_filename='./button.png', image_size=(300,300), image_subsample=5, border_width=0, button_color=(sg.theme_background_color(),sg.theme_background_color()))],
    [sg.Button('Who are you'),
    sg.Button('Tell me a fun fact'), sg.Button('Whats the weather')]]

    #for commandList use the main keyword for each command you want to call
    #button image must be in the ./images/commands/ folder and named [keyword].png  ex: ./images/commands/weather.png
    commandList = ["weather", "dance", "song", "music", "old", "fact"]
    random_commands = random.sample(commandList, 3)
    
    layout = [
        [sg.Button(key="Who are you?", image_filename='./images/commands/who.png', image_size=(336, 140), border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())),
        sg.Button(key="Lets Play a game", image_filename='./images/commands/game.png', image_size=(336, 140), border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())),
        sg.Button(key="Tell me a joke", image_filename='./images/commands/joke.png', image_size=(336, 140), border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()))],
        [sg.Button(key='Press To Speak To BruinBot', image_filename='./images/speak.png', image_size=(320, 320), border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()))],
        [sg.Button(key=random_commands[0], image_filename=f'./images/commands/{random_commands[0]}.png', image_size=(336, 140), border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())),
        sg.Button(key=random_commands[1], image_filename=f'./images/commands/{random_commands[1]}.png', image_size=(336, 140), border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())),
        sg.Button(key=random_commands[2], image_filename=f'./images/commands/{random_commands[2]}.png', image_size=(336, 140), border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()))]
        #[sg.Button(button_text=random_commands[0], image_filename='./images/green_rectangle.png', image_size=(336, 140), image_subsample=7, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())),
        #sg.Button(button_text=random_commands[1], image_filename='./images/green_rectangle.png', image_size=(336, 140), image_subsample=7, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())),
        #sg.Button(button_text=random_commands[2], image_filename='./images/green_rectangle.png', image_size=(336, 140), image_subsample=7, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()))]

    ]

    #pressToStart = [[sg.Button('Press To Speak To BruinBot', size=(500,500), image_filename='./button_smallest.png', image_size=(500,500))]]
    #isClicked = sg.Window('Speak to BruinBot', pressToStart, no_titlebar=True).read(close=True)
    #event, values = sg.Window('Speak to BruinBot', layout, no_titlebar=True, element_justification='c').read(close=True)
    #event = sg.Window('Speak to BruinBot', layout).read(close=True)
    #window = sg.Window('My window', layout, no_titlebar=True, alpha_channel=0.5)
    #print(event)
    
    event, values = sg.Window('Speak to BruinBot', layout, no_titlebar=True, element_justification='c').read(close=True)
    #print(values)
    #print(event)
    voice.parser(event)


if __name__ == "__main__":
    displayGUI()
