from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

# Define the main app class
class SimpleApp(MDApp):

    def build(self):
        # Load the KV file that defines the app's user interface
        return Builder.load_string(KV)

# Define the user interface layout using KivyMD's KV language
KV = '''
ScreenManager:
    MenuScreen:
    InputScreen:

<MenuScreen>:
    name: 'menu'
    
    BoxLayout:
        orientation: 'vertical'
        padding: dp(48)
        spacing: dp(24)

        MDLabel:
            text: 'Simple KivyMD App'
            theme_text_color: "Primary"
            font_style: 'H4'

        MDRaisedButton:
            text: 'Input Screen'
            on_press: root.manager.current = 'input'

<InputScreen>:
    name: 'input'
    
    BoxLayout:
        orientation: 'vertical'
        padding: dp(48)
        spacing: dp(24)

        MDTextField:
            id: input_text
            hint_text: "Enter something"
            helper_text: "You can enter text here"
            helper_text_mode: "on_focus"

        MDRaisedButton:
            text: 'Submit'
            on_press: root.show_result()

        MDLabel:
            id: result_label
            text: ''
            theme_text_color: "Primary"
            font_style: 'H5'
'''

# Define the screens for the app
class MenuScreen(Screen):
    pass

class InputScreen(Screen):

    def show_result(self):
        input_text = self.ids.input_text.text
        self.ids.result_label.text = f'You entered: {input_text}'

# Create and run the app
if __name__ == '__main__':
    SimpleApp().run()
