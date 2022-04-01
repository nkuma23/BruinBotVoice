#cd Documents\Github\BruinBot\BruinBotVoice\Kivy
#conda activate PyAudioEnv1
#python kivyTest.py
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
# from kivy.lang import Builder
# from kivy.config import Config
# from kivy.uix.floatlayout import FloatLayout
import voice

commandList = ["What's the weather like", "Do a dance", "Sing a song", "Play music", "How old are you", "Tell me a fun fact"]
import random


class TestGUI(BoxLayout):
    def build(self):
        self.ids.random1.text="random1"
    def updateText(self):
        pass
        # self.ids.clicked.text="Has been clicked"
    def runVoice(self, val):
        voice.parser(val)


class TestWidget(BoxLayout):
    def updateText(self):
        self.ids.clicked.text="Has been clicked"

class TestApp(App):
    def build(self):
        # return TestWidget()
        print("hello")
        random_commands = random.sample(commandList, 3)
        testGui = TestGUI()
        testGui.ids.random1.text = random_commands[0]
        testGui.ids.random2.text = random_commands[1]
        testGui.ids.random3.text = random_commands[2]
        #return TestButtons()
        return testGui
        #return Button(text="Hello!", background_color=(0,0,1,1), font_size=150)


class TestButtons(BoxLayout):
    def build(self):
        pass



class testMyButtonsApp(App):
    def build(self):
        testButtons = TestGUI()
        return testButtons

if __name__ == "__main__":
    TestApp().run()