from kivy.app import App
from kivy.uix.widget import Widget
from random import random
from kivy.graphics import Color,Ellipse,Line
from kivy.uix.button import Button

class KivyDrawingExamples(Widget):
    def on_touch_down(self, touch):
        color = (random(),1,1)
        with self.canvas:
            Color(*color,mode='hsv')
            d=30.
            Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d))
            touch.ud['line']= Line(points=(touch.x,touch.y))
        
    def on_touch_move(self,touch):
        touch.ud['line'].points += [touch.x,touch.y]

class DrawingRunner(App):
    def build(self):
        parent= Widget()
        self.painter= KivyDrawingExamples()
        clearBtn = Button(text='clear')
        clearBtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearBtn)
        return parent
    
    def clear_canvas(self,obj):
        self.painter.canvas.clear()
    
def main():
    DrawingRunner().run()


if __name__ == '__main__':
    main()