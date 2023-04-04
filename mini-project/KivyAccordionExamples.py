from kivy.app import App
from kivy.uix.accordion import Accordion,AccordionItem
from kivy.uix.label import Label

class KivyAccordionExamples(App):
    def build(self):
        root= Accordion(orientation='vertical')
        for x in range(10):
            item= AccordionItem(title='Title % d' % x)
            item.add_widget(Label(text='Accordion Sample \n' * 5))
            root.add_widget(item)
        return root
def main():
    KivyAccordionExamples().run()


if __name__ == '__main__':
    main()