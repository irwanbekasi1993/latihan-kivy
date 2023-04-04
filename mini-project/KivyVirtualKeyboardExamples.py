from kivy.app import App
from kivy.uix.vkeyboard import VKeyboard

class KivyVirtualKeyboardExamples(VKeyboard):
    player = VKeyboard()

class VirtualKeyboardRunner(App):
    def build(self):
        return KivyVirtualKeyboardExamples()

def main():
    VirtualKeyboardRunner().run()


if __name__ == '__main__':
    main()