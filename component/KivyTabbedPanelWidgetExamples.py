from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_string('''
<KivyTabbedPanelWidgetExamples>:
    size_hint: .5,.5
    pos_hint: {'center_x':.5,'center_y':.5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'Tab 1'
        Label:
            text: 'First Tab'
    TabbedPanelItem:
        text: 'Tab 2'
        BoxLayout:
            Label:
                text: 'Press Button'
            Button:
                text: 'Click It'
    TabbedPanelItem:
        text: 'Tab 3'
        RstDocument:
            text:'\\n'.join(("Document Description","====","Third Tab"))
''')

class KivyTabbedPanelWidgetExamples(TabbedPanel):
    pass
        
class TabbedPanelRunner(App):
    def build(self):
        return KivyTabbedPanelWidgetExamples()

def main():
    TabbedPanelRunner().run()


if __name__ == '__main__':
    main()