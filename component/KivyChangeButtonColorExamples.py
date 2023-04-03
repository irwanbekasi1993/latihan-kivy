from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random

red=[1,0,0,1]
green=[0,1,0,1]
blue=[0,0,1,1]
purple=[1,0,1,1]

class KivyChangeButtonColorExamples(App):
    def build(self):
        superBox = BoxLayout(orientation='vertical')
        HB = BoxLayout(orientation='horizontal')
        colors=[red,green,purple,blue]
        btn1=Button(text='One',background_color=random.choice(colors),
                    font_size=32,size_hint=(.7, 1))
        btn2=Button(text='Two',background_color=random.choice(colors),
                    font_size=32,size_hint=(.7, 1))
        HB.add_widget(btn1)
        HB.add_widget(btn2)

        VB = BoxLayout(orientation='vertical')

        btn3= Button(text='Three', background_color=random.choice(colors),
                     font_size=32,size_hint=(1, 10))
        btn4= Button(text='Four',background_color=random.choice(colors),
                     font_size=32,size_hint=(1, 10))
        
        VB.add_widget(btn3)
        VB.add_widget(btn4)

        superBox.add_widget(HB)
        superBox.add_widget(VB)

        return superBox


        return superBox


def main():
    KivyChangeButtonColorExamples().run()


if __name__ == '__main__':
    main()