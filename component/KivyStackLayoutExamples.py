from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

class KivyStackLayoutExamples(App):
    def build(self):
        # ['lr-bt','bt-lr','rl-bt','bt-rl']
        sl = StackLayout(orientation='bt-rl')

        btn1 = Button(text='B1',font_size=20,size_hint=(.2, .1))
        btn2 = Button(text='B2',font_size=20,size_hint=(.2, .1))
        btn3 = Button(text='B3',font_size=20,size_hint=(.2, .1))
        btn4 = Button(text='B4',font_size=20,size_hint=(.2, .1))
        btn5 = Button(text='B5',font_size=20,size_hint=(.2, .1))
        btn6 = Button(text='B6',font_size=20,size_hint=(.2, .1))
        btn7 = Button(text='B7',font_size=20,size_hint=(.2, .1))
        btn8 = Button(text='B8',font_size=20,size_hint=(.2, .1))
        btn9 = Button(text='B9',font_size=20,size_hint=(.2, .1))
        btn10 = Button(text='B10',font_size=20,size_hint=(.2, .1))

        sl.add_widget(btn1)
        sl.add_widget(btn2)
        sl.add_widget(btn3)
        sl.add_widget(btn4)
        sl.add_widget(btn5)
        sl.add_widget(btn6)
        sl.add_widget(btn7)
        sl.add_widget(btn8)
        sl.add_widget(btn9)
        sl.add_widget(btn10)

        return sl
        


def main():
    KivyStackLayoutExamples().run()


if __name__ == '__main__':
    main()