import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def create(self):
        return Label(text = "Mahanth's first python app")

if __name__ == "__main__":
    MyApp.run()


