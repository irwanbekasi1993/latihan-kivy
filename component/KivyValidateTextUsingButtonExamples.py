from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics','resizeable',True)

class KivyValidateTextUsingButtonExamples(App):
    def build(self):
        b= BoxLayout(orientation='vertical')
        t= TextInput(font_size=30, size_hint_y=None, height=100)
        f=Button(text='Push This', font_size="20sp", background_color=(.67,1,.33,1),
                 color=(1,1,1,1))
        
        b.add_widget(t)
        b.add_widget(f)
        
        f.bind(on_press=self.validateMessage)
        return b
    
    def validateMessage(self,event):
        event.text='validated'
        event.disabled=True
        self.root.children[1].text='Validated'
        self.root.children[1].disabled=True

def main():
    KivyValidateTextUsingButtonExamples().run()


if __name__ == '__main__':
    main()