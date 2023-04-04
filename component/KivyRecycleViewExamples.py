from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder

Builder.load_string("""
<KivyRecycleViewExamples>:
    viewclass:'Button'
    orientation: 'vertical'
    spacing:40
    padding:10,10
    space_x:self.size[0]/3

    RecycleBoxLayout:
        color:(0,.7,.4,.8)
        default_size:None, dp(56)
        default_size_hint: 0.4,None
        height: self.minimum_height
        orientation: 'vertical'
""")

class KivyRecycleViewExamples(RecycleView):
    def __init__(self, **kwargs):
        super(KivyRecycleViewExamples, self).__init__(**kwargs)
        self.data=[{'text':str(x)} for x in range(10)]


class RecycleViewRunner(App):
    def build(self):
        return KivyRecycleViewExamples()

def main():
    RecycleViewRunner().run()


if __name__ == '__main__':
    main()