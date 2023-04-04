from kivy.app import App
from kivy.uix.accordion import Accordion
from kivy.lang import Builder

Builder.load_string('''
<MyImage@Image>:
    keep_ratio:False
    allow_stretch:True
<KivyAccordionWithFileExamples>:
    orientation: 'vertical'
    AccordionItem:
        title:'HTML5'
        MyImage:
            source: 'HTML5_badge.png'
    AccordionItem:
        title:'CSS3'
        MyImage:
            source: 'css3-logo-png-transparent.png'
    AccordionItem:
        title:'JS'
        MyImage:
            source: 'OIP_2.jpg'
    AccordionItem:
        title:'NodeJS'
        MyImage:
            source: 'Node_logo_NodeJS.png'
    AccordionItem:
        title:'Bootstrap'
        MyImage:
            source: 'OIP_3.jpg'
''')

class KivyAccordionWithFileExamples(Accordion):
    pass

class KivyAccordionWithFileRunner(App):
    def build(self):
        return KivyAccordionWithFileExamples()

def main():
    KivyAccordionWithFileRunner().run()


if __name__ == '__main__':
    main()