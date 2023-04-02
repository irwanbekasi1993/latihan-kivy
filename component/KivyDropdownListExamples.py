from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

dropdown = DropDown()
for index in range(10):    
    btn = Button(text='Value % d ' % index,size_hint_y=None, height=40)
    btn.bind()
    dropdown.add_widget(btn)
mainButton = Button(text='Hello', size_hint=(None,None), pos=(350,300))
mainButton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x:setattr(mainButton,'text',x))
runTouchApp(mainButton)