from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.core.window import Window
import voice

commandList = ["What's the\n weather like", "Do a dance", "Sing a song", "Play music", "How old are you", "Tell me a fun fact"]
import random
# Window.fullscreen=True
# from kivy.lang import Builder
# from kivy.config import Config
# from kivy.uix.floatlayout import FloatLayout

class RoundButtonApp(App):
    def build(self):
        # Hides the kivy window in display
        Window.borderless = True
        #randomly select 4 commands from commandList
        random_commands = random.sample(commandList, 4)
        testGui = MyLayout() #create instance of starting layout
        #Set buttons to display the 4 random commands
        testGui.ids.command1.text = random_commands[0]
        testGui.ids.command2.text = random_commands[1]
        testGui.ids.command3.text = random_commands[2]
        testGui.ids.command4.text = random_commands[3]
        return testGui
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
        self.root.ids.transcript.text = message
    def goodbye(self):
        voice.speak('Goodbye')
        self.stop()
        # App.get_running_app().stop()



class MyLayout(BoxLayout):
    def build(self):
        pass
    def runVoice(self, val):
        pass
        #voice.parser(val)

if __name__ == "__main__":
    RoundButtonApp().run()