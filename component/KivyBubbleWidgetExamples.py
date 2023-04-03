from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.bubble import Bubble
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_string('''
<Cut_Copy_Paste>:
    size_hint: (None,None)
    size: (160,120)
    pos_hint: {'center_x':.5,'y':.6}
    BubbleButton:
        text:'Cut'
    BubbleButton:
        text:'Copy'
    BubbleButton:
        text:'Paste'
''')

class Cut_Copy_Paste(Bubble):
    pass

class KivyBubbleWidgetExamples(FloatLayout):
    def __init__(self, **kwargs):
        super(KivyBubbleWidgetExamples, self).__init__(**kwargs)
        self.butBubble= Button(text='Press To Show Bubble')
        self.butBubble.bind(on_release=self.showBubble)
        self.add_widget(self.butBubble)
        self.bubb= Cut_Copy_Paste()
    
    def showBubble(self, *l):
        self.add_widget(self.bubb)

    
class BubbleRunner(App):
    def build(self):
        return KivyBubbleWidgetExamples()

def main():
    BubbleRunner().run()


if __name__ == '__main__':
    main()