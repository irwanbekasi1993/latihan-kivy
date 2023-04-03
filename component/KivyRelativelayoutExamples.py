from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config

Config.set('graphics','resizeable',True)

class KivyRelativelayoutExamples(App):
    def build(self):
        r1 = RelativeLayout()
        btn = Button(text='Tes Realtive Layout Button 1',
                     size_hint=(.2, .2),
                     pos=(396.0,298.0))
        btn1 = Button(text='Tes Realtive Layout Button 2',
                     size_hint=(.2, .2),
                     pos=(-137.33,298.0))
        r1.add_widget(btn)
        r1.add_widget(btn1)
        return r1


def main():
    KivyRelativelayoutExamples().run()


if __name__ == '__main__':
    main()