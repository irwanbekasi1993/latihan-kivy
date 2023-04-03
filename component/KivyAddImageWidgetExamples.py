from kivy.app import App
from kivy.uix.image import AsyncImage

class KivyAddImageWidgetExamples(App):
    def build(self):
        return AsyncImage(source='http://kivy.org/logos/kivy-logo-black-64.png')
        


def main():
    KivyAddImageWidgetExamples().run()


if __name__ == '__main__':
    main()