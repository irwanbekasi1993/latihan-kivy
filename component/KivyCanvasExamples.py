from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle,Color

class CanvasWidget(Widget):
    def __init__(self, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)
        with self.canvas:
            Color(1,0,0,1)
            self.rect = Rectangle(source="image/Handwritten_2022-09-23_075950.jpg",pos=self.center,size=(self.width/.2,self.height/.2))
            self.bind(pos=self.update_rect,size=self.update_rect)

    def update_rect(self, *args):
        self.rect_pos=self.pos
        self.rect_size=self.size


class CanvasApp(App):
    def build(self):
        return CanvasWidget()

def main():
    CanvasApp().run()


if __name__ == '__main__':
    main()