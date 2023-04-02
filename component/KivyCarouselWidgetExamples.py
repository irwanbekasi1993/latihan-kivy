from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel

class KivyCarouselWidgetExamples(App):
    def build(self):
        carousel = Carousel(direction='right')
        for i in range(10):
            src = "image/Handwritten_2022-09-23_075950.jpg"
            image= AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)    
        return carousel

def main():
    KivyCarouselWidgetExamples().run()


if __name__ == '__main__':
    main()