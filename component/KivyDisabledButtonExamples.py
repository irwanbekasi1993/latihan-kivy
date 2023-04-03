from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout

class KivyDisabledButtonExamples(App):
    def build(self):
        r1 = RelativeLayout()
        btn1 = Button(text='Push This',
                            font_size="20sp",
                            background_color=(1,1,1,1),
                            color=(1,1,1,1),
                            size=(32,32),
                            size_hint=(.2, .2),
                            pos=(200,250),disabled=False)
        
        r1.add_widget(btn1)

        btn1.bind(on_press=self.callback)
        
        return r1

    def callback(self,event):
        event.disabled=True
        event.text='Disabled'
        print('button cannot be click')

def main():
    KivyDisabledButtonExamples().run()


if __name__ == '__main__':
    main()