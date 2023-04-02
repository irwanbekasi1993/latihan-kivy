from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
Config.set('graphics','resizeable',True)

class KivyWindowAdjustmentExamples(App):
    def __init__(self, **kwargs):
        super(KivyWindowAdjustmentExamples, self).__init__(**kwargs)
        
    def build(self):
        label = Label(text="Halo", font_size='100sp', markup=True)
        return label

def main():
    KivyWindowAdjustmentExamples().run()


if __name__ == '__main__':
    main()