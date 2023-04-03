from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config

Config.set('graphics','resizeable',True)

class KivyChangeButtonPositionAndSizeExamples(App):
    def build(self):
        r1 = RelativeLayout(size=(.2,.2))
        b1 = Button(size_hint=(.2, .2),pos_hint={'center_x': .7, 'center_y': .5},
                    text='pos_hint')
        b2 = Button(size_hint=(.5, .2),
                    text='size_hint')
        b3 = Button(size_hint=(.2, .2),pos=(200,200),
                    text='pos')
        
        r1.add_widget(b1)
        r1.add_widget(b2)
        r1.add_widget(b3)

        return r1


def main():
    KivyChangeButtonPositionAndSizeExamples().run()


if __name__ == '__main__':
    main()