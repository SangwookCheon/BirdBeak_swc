from BackEnd_Kivy.logic import print_message
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class Simulation(FloatLayout):
    def __init__(self):
        super(Simulation, self).__init__()
        self.b1 = Button(text = "Button 1")
        self.label1 = Label(text = print_message(), pos = (100,10))
        self.add_widget(self.b1)
        self.add_widget(self.label1)

class MyApp(App):
    def build(self):
        return Simulation()


if __name__ == '__main__':
    MyApp().run()

