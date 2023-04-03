from kivy.app import App
from kivy.config import Config

Config.set('graphics','resizeable',True)

from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout

class KivySpinnerWidgetExamples(App):
    def build(self):
        layout = FloatLayout()
        self.spinnerObject = Spinner(text='Python',
                                           values=('Python','Java','C++','C','C#','PHP'),
                                           background_color=(.784,.433,.216,1))
        self.spinnerObject.size_hint=(0.3,0.2)
        self.spinnerObject.pos_hint={'x':.35,'y':.75}
        layout.add_widget(self.spinnerObject)

        self.spinnerObject.bind(text=self.on_spinner_select)
        self.spinnerSelection= Label(text="Selected Value In Spinner Is: %s"%self.spinnerObject.text)

        layout.add_widget(self.spinnerSelection)
        self.spinnerSelection.pos_hint={'x':.3,'y':.3}
        return layout
    
    def on_spinner_select(self,spinner,text):
        self.spinnerSelection.text= "Selected Value In Spinner Is: %s" %self.spinnerObject.text
        print('The Spinner',spinner,' have text: ',text)
    
def main():
    KivySpinnerWidgetExamples().run()


if __name__ == '__main__':
    main()