from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class KivySimpleWindowExamples(GridLayout):
    def __init__(self, **kwargs):
        super(KivySimpleWindowExamples, self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text='Username'))
        self.username= TextInput(multiline=True)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True,multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label(text='Confirm Password'))
        self.confirmPassword = TextInput(password=True,multiline=True)
        self.add_widget(self.confirmPassword)

class SimpleWindowRunner(App):
    def build(self):
        return KivySimpleWindowExamples()

def main():
    SimpleWindowRunner().run()


if __name__ == '__main__':
    main()