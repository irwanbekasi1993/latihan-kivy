from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
Config.set('graphics','resizeable',True)

class KivyPopupWidgetExamples(App):
    def build(self):
        self.layout= GridLayout(cols=1,padding=10)
        self.button=Button(text='Click For Popup')
        self.layout.add_widget(self.button)
        self.button.bind(on_press=self.onButtonPress)
        return self.layout

    def onButtonPress(self, button):
        layout = GridLayout(cols=1,padding=10)
        popupLabel= Label(text='Popup Description')
        closeButton= Button(text='Close The Popup')

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        popup = Popup(title='Popup Demo', content=layout,
                      size_hint=(None, None),size=(200,200))
        popup.open()

        closeButton.bind(on_press=popup.dismiss)

def main():
    KivyPopupWidgetExamples().run()


if __name__ == '__main__':
    main()