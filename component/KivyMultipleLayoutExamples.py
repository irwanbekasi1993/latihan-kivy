from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.lang import Builder

Builder.load_string('''
<PageLayout>:
    BoxLayout:
        canvas:
            Color:
                rgba: 216/255.,195/255.,88/255.,1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation:'vertical'

        Label:
            size_hint_y:None
            height: 1.5*self.texture_size[1]
            text:'page 1'

        Button:
            text: 'Button 1'
            on_press: print('First Page')

    BoxLayout:
        orientation:'vertical'
        canvas:
            Color:
                rgba: 109/225.,8/255.,57/255.,1
            Rectangle: 
                pos: self.pos
                size: self.size
        Label:
            text: 'Page 2'

        AsyncImage:
            source: 'http://kivy.org/logos/kivy-logo-black-64.png'

    GridLayout:
        canvas:
            Color:
                rgba: 37/255.,39/255.,30/255.,1
            Rectangle: 
                pos: self.pos
                size: self.size
        cols:2

        Label:
            text:'Page 3'
        AsyncImage:
            source: 'http://kivy.org/slides/kivyandroid-thumb.jpg'
        
        Button:
            text:'User'
            on_press: print('User From Last Page')

        AsyncImage:
            source: 'http://kivy.org/slides/kivypictures-thumb.jpg'

        AsyncImage:
            source: 'http://kivy.org/slides/particlepanda-thumb.jpg'

''')

class MultipleLayout(PageLayout):
    pass

class KivyMultipleLayoutExamples(App):
    def build(self):
        return MultipleLayout()
        
def main():
    KivyMultipleLayoutExamples().run()


if __name__ == '__main__':
    main()