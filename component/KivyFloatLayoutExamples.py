from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout

Config.set('graphics','resizeable',True)

class KivyFloatLayoutExamples(App):
    def build(self):
        fl = FloatLayout()
        btn = Button(text='Tes Float Layout',
                     size_hint=(.3, .5),
                     background_color=(.3,.6,.7,1),
                     pos_hint={'x': .2, 'y': .2})
        fl.add_widget(btn)
        return fl
        


def main():
    KivyFloatLayoutExamples().run()


if __name__ == '__main__':
    main()