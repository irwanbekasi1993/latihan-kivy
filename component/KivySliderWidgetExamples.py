from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties import StringProperty

class KivySliderWidgetExamples(GridLayout):
    def __init__(self, **kwargs):
        super(KivySliderWidgetExamples, self).__init__(**kwargs)
        self.cols=4
        self.brightnessControl = Slider(min=0,max=100,orientation='horizontal',value_track=True,value_track_color=[1,0,0,1])
        self.add_widget(Label(text='brightness'))
        self.add_widget(self.brightnessControl)

        self.add_widget(Label(text='Slider Value'))
        self.brightnessValue = Label(text='0')
        self.add_widget(self.brightnessValue)

        self.brightnessControl.bind(value=self.on_value)

    def on_value(self,instance,brightness):
        self.brightnessValue.text = "% d"% brightness

class SliderRunner(App):
    def build(self):
        runner = KivySliderWidgetExamples()
        return runner    

def main():
    SliderRunner().run()


if __name__ == '__main__':
    main()