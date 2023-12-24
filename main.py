# kivy_app.py
from kivy.app import App
from kivy.uix.button import Button
from Velhinha import Velhinha

class PygameApp(App):
    def build(self):
        return Button(text='Hello Pygame', on_press=rodar_jogo)

def rodar_jogo():
    Velhinha().main()


if __name__ == '__main__':
    PygameApp().run()


