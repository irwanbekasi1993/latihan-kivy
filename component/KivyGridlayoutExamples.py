from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string('''
<MainWidget>:
    cols:2
    rows:2
    row_force_default: True
    row_default_height: 40
    Button:
        text:'Hello1'
        size_hint_x: None
        width:100
    Button:
        text: 'World1'
    Button:
        text:'Hello2'
        size_hint_x:None
        width:100
    Button:
        text:'World2'
''')

class MainWidget(GridLayout):
    pass

class KivyGridlayoutExamples(App):
    def build(self):
        return MainWidget()        


def main():
    KivyGridlayoutExamples().run()


if __name__ == '__main__':
    main()