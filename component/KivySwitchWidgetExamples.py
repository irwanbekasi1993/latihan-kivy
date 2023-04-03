from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class KivySwitchWidgetExamples(GridLayout):
    def __init__(self, **kwargs):
        super(KivySwitchWidgetExamples, self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text='Switch'))
        self.setting_sample= Switch(active=False)
        self.add_widget(self.setting_sample)
        self.setting_sample.bind(active= switchCallback)

def switchCallback(switchObject,switchValue):
    if(switchValue):
        print('Swittch Is On')
    else:
        print('Switch Is Off')

class SwitchRunner(App):
    def build(self):
        return KivySwitchWidgetExamples()

def main():
    SwitchRunner().run()


if __name__ == '__main__':
    main()