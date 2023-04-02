from kivy.app import App
from kivy.uix.label import Label

class AppTitle(App):
    def build(self):
        lbl = Label(text='Hello World')
        return lbl

def main():
    AppTitle().run()


if __name__ == '__main__':
    main()