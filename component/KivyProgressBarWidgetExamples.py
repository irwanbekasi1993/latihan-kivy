from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class KivyProgressBarWidgetExamples(Widget):

    progressBar = ObjectProperty()

    def __init__(self, **kwargs):
        super(KivyProgressBarWidgetExamples, self).__init__(**kwargs)
        self.progressBar = ProgressBar()
        self.popup = Popup(title='Download',content=self.progressBar)    
        self.popup.bind(on_open=self.puopen)
        self.add_widget(Button(text='Download',on_release=self.pop))

    def pop(self,instance):
        self.progressBar.value=1
        self.popup.open()

    def next(self,dt):
        if self.progressBar.value>=100:
            return False
        self.progressBar.value+=1

    def puopen(self,instance):
        Clock.schedule_interval(self.next,1/25)

class ProgressBarRunner(App):
    def build(self):
        return KivyProgressBarWidgetExamples()

def main():
        ProgressBarRunner().run()


if __name__ == '__main__':
    main()