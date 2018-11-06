import kivy
from kivy.app import App
from kivy.uix.label import *
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class Grid1(GridLayout):
    def __init__(self, **kwargs):
        super(Grid1, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = "User Name:"))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.add_widget(Label(text = "Password:"))
        self.password = TextInput(password = True, multiline = False)
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        return Grid1()


if __name__ == "__main__":
    MyApp().run()