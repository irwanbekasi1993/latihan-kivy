from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout

class KivyWidgetCheckBoxExamples(GridLayout):
    def __init__(self, **kwargs):
        super(KivyWidgetCheckBoxExamples, self).__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text='Male'))
        self.activeMale = CheckBox(active=True)
        self.add_widget(self.activeMale)

        self.add_widget(Label(text='Female'))
        self.activeFemale = CheckBox(active=True)
        self.add_widget(self.activeFemale)

        self.add_widget(Label(text='Other'))
        self.active = CheckBox(active=True)
        self.add_widget(self.active)

        self.lbl_active = Label(text='Check Box is Selected')
        self.add_widget(self.lbl_active)

        self.active.bind(active = self.on_checkbox_Active)
        self.activeMale.bind(active = self.on_checkbox_Active)
        self.activeFemale.bind(active = self.on_checkbox_Active)

    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.lbl_active.text = "Check Box Is Selected"
            print("Check Box Selected")
        else:
            self.lbl_active.text = "Check Box Is Not Selected"
            print("Check box is Not Selected")

class CheckBoxApp(App):
    def build(self):
        return KivyWidgetCheckBoxExamples()

def main():
    CheckBoxApp().run()

if __name__ == '__main__':
    main()