from kivy.app import App
from kivy.lang import Builder
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout

Builder.load_string('''
<SquareWidget>:
    size:100,100
    canvas:
        Color:
            rgb: [.345,.85,.456]
        Rectangle:
            size:self.size
            pos:self.pos

<KivyScatterWidgetExamples>:
    canvas:
        Color:
            rgb:.8,.5,.4
        Rectangle:
            size: self.size
            pos: self.pos
    ScatterWidget:
        id: square_widget_id
        SquareWidget:

    Label:
        text: 'Position: '+str(square_widget_id.pos)
        size_hint: .1,.1
        pos: 500,300
''')

class SquareWidget(Widget):
    pass

class ScatterWidget(Scatter):
    pass

class KivyScatterWidgetExamples(RelativeLayout):
    pass
        
class ScatterRunner(App):
    def build(self):
        return KivyScatterWidgetExamples()

def main():
    ScatterRunner().run()


if __name__ == '__main__':
    main()