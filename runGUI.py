from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, FadeTransition, SlideTransition
from kivy.graphics import Color
from kivy.core.window import Window
import time
import voice

commandList = ["What's the\n weather like", "Do a dance", "Sing a song", "Play music", "How old are you", "Tell me a fun fact"]
import random
# Window.fullscreen=True
# from kivy.lang import Builder
# from kivy.config import Config
# from kivy.uix.floatlayout import FloatLayout

class BruinBotApp(App):
    def build(self):
        # Hides the kivy window in display
        sm = ScreenManager()
        sm.transition = NoTransition()
        # sm.transition = FadeTransition
        Window.borderless = True
        testGui = MyLayout() #create instance of starting layout

        # #randomly select 4 commands from commandList
        # random_commands = random.sample(commandList, 4)

        # #Set buttons to display the 4 random commands
        # testGui.ids.command1.text = random_commands[0]
        # testGui.ids.command2.text = random_commands[1]
        # testGui.ids.command3.text = random_commands[2]
        # testGui.ids.command4.text = random_commands[3]
        sm.add_widget(testGui)
        secondWindow = SecondWindow()
        sm.add_widget(secondWindow)
        return sm
    def runVoice(self, val):
        # pass
        response = voice.parser(val)
        self.setTranscript(response)
        # voice.speak(response)
        # voice.hello()
    def speak(self, command):
        voice.speak(command)
    def runListen(self):
        voice.parser("Press To Speak To BruinBot")
    def setTranscript(self, message):
        self.root.current_screen.ids.transcript.text = message
    def goodbye(self):
        voice.speak('Goodbye')
        self.stop()
        # App.get_running_app().stop()
    def dispenseGift(self, giftNum):
        print(giftNum)

    def switchScreen(self, screenName):
        self.root.current = screenName
        # if(screenName=="main"):
        #     pass
        #     randomly select 4 commands from commandList
        #     random_commands = random.sample(commandList, 4)

        #     #Set buttons to display the 4 random commands
        #     self.root.current_screen.ids.command1.text = random_commands[0]
        #     self.root.current_screen.ids.command2.text = random_commands[1]
        #     self.root.current_screen.ids.command3.text = random_commands[2]
        #     self.root.current_screen.ids.command4.text = random_commands[3]


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    def build(self):
        return self

class MyLayout(Screen):
    def build(self):
        return self
    def on_enter(self,):
        #randomly selects 4 commands to display
        random_commands = random.sample(commandList, 4)

        #Set buttons to display the 4 random commands
        self.ids.command1.text = random_commands[0]
        self.ids.command2.text = random_commands[1]
        self.ids.command3.text = random_commands[2]
        self.ids.command4.text = random_commands[3]

    def runVoice(self, val):
        pass
        #voice.parser(val)

if __name__ == "__main__":
    BruinBotApp().run()