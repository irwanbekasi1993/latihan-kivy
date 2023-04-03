from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<KivyButtonActionExamples>:
    lbl:myLabel
    BoxLayout:
        orientation: 'vertical'
        size:[1,.25]
    Button:
        text:'Click Me'
        font_size: "50sp"
        color: [0,255,255,.67]
        on_press: root.btnClk()
    Label:
        id: myLabel
        text: 'Not Clicked Yet'
        color: [0,84,80,19]
''')

class KivyButtonActionExamples(BoxLayout):
    def btnClk(self):
        self.lbl.text='You Have Been Pressed The Button'

class ButtonPressedAction(App):
    def build(self):
        return KivyButtonActionExamples()

def main():
    ButtonPressedAction().run()


if __name__ == '__main__':
    main()