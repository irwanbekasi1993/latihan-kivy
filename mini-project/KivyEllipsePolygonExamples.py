from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string('''
<KivyEllipsePolygonExamples>:
# Row1
    cols:4
    canvas:
        Color:
            rgb: 0,0,1
        Rectangle: 
            pos: self.pos
            size: self.size

    RelativeLayout:
        canvas:
            Color:
                rgb: 1,.8,.5
            Ellipse:
                pos:0,0
                size: self.size

    RelativeLayout:
        canvas:
            Ellipse:
                segments:5
                pos:0,0
                size:self.size

    RelativeLayout:
        canvas:
            Ellipse:
                segments:4
                pos:0,0
                size:self.size

    RelativeLayout:
        canvas:
            Ellipse:
                segments:3
                pos:0,0
                size: self.size

# Row2

    RelativeLayout:
        canvas:
            Color: 
                rgb: 1,.59,.86
            Ellipse:
                angle_start: 240
                angle_end: 480
                pos:0,0
                size:self.size

    RelativeLayout:
        canvas:
            Ellipse:
                angle_start: 240
                angle_end: 480
                segments:5
                pos:0,0
                size:self.size

    RelativeLayout:
        canvas:
            Ellipse:
                angle_start: 240
                angle_end: 480
                segments:4
                pos:0,0
                size:self.size

    RelativeLayout:
        canvas:
            Ellipse:
                angle_start: 240
                angle_end: 480
                segments:3
                pos:0,0
                size:self.size

    # Row3

    RelativeLayout:
        canvas:
            Color:
                rgb: .5,.5,.5
            Ellipse:
                angle_start: 120
                angle_end: 240
                pos:0,0
                size:self.size

    RelativeLayout:
        canvas:
            Ellipse:
                angle_start: 120
                angle_end: 240
                segments:5
                pos:0,0
                size:self.size

    RelativeLayout:
        canvas:
            Ellipse:
                angle_start: 120
                angle_end: 240
                segments:4
                pos:0,0
                size:self.size

    RelativeLayout:
        canvas:
            Ellipse:
                angle_start: 120
                angle_end: 240
                segments:3
                pos:0,0
                size:self.size

''')

class KivyEllipsePolygonExamples(GridLayout):
    pass

class EllipsePolygonRunner(App):
    def build(self):
        return KivyEllipsePolygonExamples()

def main():
    EllipsePolygonRunner().run()


if __name__ == '__main__':
    main()