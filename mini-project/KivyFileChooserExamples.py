from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<KivyFileChooserExamples>:
    label: label
    orientation: 'vertical'
    BoxLayout:
        FileChooserListView:
            canvas.before:
                Color:
                    rgb: .4,.5,.5
                Rectangle: 
                    pos: self.pos
                    size: self.size
            on_selection: root.select(*args)

        FileChooserIconView:
            canvas.before:
                Color:
                    rgb: .5,.4,.5
                Rectangle: 
                    pos:self.pos
                    size:self.size
            on_selection: root.select(*args)

    Label:
        id: label
        size_hint_y: .1
        canvas.before:
            Color:
                rgb: .5,.5,.4
            Rectangle: 
                pos: self.pos
                size: self.size
''')

class KivyFileChooserExamples(BoxLayout):
    def select(self, *args):
        try: self.label.text= args[1][0]
        except: pass

class FileChooserRunner(App):
    def build(self):
        return KivyFileChooserExamples()


def main():
    FileChooserRunner().run()


if __name__ == '__main__':
    main()