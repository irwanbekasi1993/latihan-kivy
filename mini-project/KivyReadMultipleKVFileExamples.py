from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string('''
<KivyReadMultipleKVFileExamples>:
    cols:3

    AnchorLayout:
        anchor_x:'left'
        anchor_y: 'center'

        canvas:
            Color:
                rgb: [1,0,0]
            Rectangle: 
                pos: self.pos
                size: self.size

        Box1:
            size_hint: [None,None]
            size:[app.x,app.y]

    AnchorLayout:
        anchor_x:'center'
        anchor_y: 'center'

        canvas:
            Color:
                rgb: [0,1,0]
            Rectangle: 
                pos: self.pos
                size: self.size

        Box2:
            size_hint: [None,None]
            size:[app.x,app.y]

    AnchorLayout:
        anchor_x:'right'
        anchor_y: 'center'

        canvas:
            Color:
                rgb: [0,1,1]
            Rectangle: 
                pos: self.pos
                size: self.size

        Box3:
            size_hint: [None,None]
            size:[app.x,app.y]
     
<Box1@BoxLayout>:
    Button:
        text:'B1a'
    Button:
        text:'B1b'

<Box2@BoxLayout>:
    Button:
        text:'B2a'
    Button:
        text:'B2b'

<Box3@BoxLayout>
    Button:
        text:'B3a'
    Button:
        text:'B3b'
''')

class KivyReadMultipleKVFileExamples(GridLayout):
    pass

class KivyReadMultipleKVFileRunner(App):
    def build(self):
        self.x=150
        self.y=400
        return KivyReadMultipleKVFileExamples()

def main():
    KivyReadMultipleKVFileRunner().run()


if __name__ == '__main__':
    main()