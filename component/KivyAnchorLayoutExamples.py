from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class KivyAnchorLayoutExamples(App):
    def build(self):
        al = AnchorLayout(anchor_x='right',anchor_y='bottom')
        btn = Button(text='Tes Anchor Layout',size_hint=(.3, .3),
                     background_color=(1.0,0.0,0.0,1.0))
        al.add_widget(btn)
        return al


def main():
    KivyAnchorLayoutExamples().run()


if __name__ == '__main__':
    main()