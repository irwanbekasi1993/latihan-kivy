from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


Builder.load_string('''
<KivyMultipleSliderWidgetExamples>:
    orientation: 'vertical'
    slider_colors: .5,.5,.5
    canvas.before:
        Color:
            rgb: root.slider_colors
        Rectangle:
            pos: root.pos
            size: root.size

    Slider:
        min:0
        max:1
        value:.5
        on_value: root.slider_colors[0]= self.value

    Slider:
        min:0
        max:1
        value:.5
        on_value: root.slider_colors[1]= self.value

    Slider:
        min:0
        max:1
        value:.5
        on_value: root.slider_colors[2]= self.value

    Label:
        font_size: "30sp"
        text:'Color: '+", ".join(["%.3f" %(i) for i in root.slider_colors])
        color: 0,0,1,1
    
''')
class KivyMultipleSliderWidgetExamples(BoxLayout):
    pass

class MultipleSliderRunner(App):
    def build(self):
        return KivyMultipleSliderWidgetExamples()

def main():
    MultipleSliderRunner().run()


if __name__ == '__main__':
    main()