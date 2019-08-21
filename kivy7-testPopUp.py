# # import kivy
# # kivy.require('1.9.1')
# # from kivy.app import App
# # from kivy.lang import Builder
# # from kivy.uix.boxlayout import BoxLayout
# # from kivy.clock import Clock
# # from kivy.properties import ObjectProperty
# #
# # Builder.load_string("""
# # <SingleScreen>:
# #     id: single_screen
# #     orientation: 'vertical'
# #     Change_Label:
# #         id: gb
# #
# # <Change_Label>:
# #     _python_access: ChangeLabel
# #     Label:
# #         id: ChangeLabel
# #         text: "I'm Gonna Change."
# # """)
# #
# # class SingleScreen(BoxLayout):
# #     pass
# #
# #
# # class Change_Label(BoxLayout):
# #     _python_access = ObjectProperty(None)
# #
# #
# # class OneScreen(App):
# #
# #     def build(self):
# #         Clock.schedule_interval(self.Callback_Clock, 3)
# #         return SingleScreen()
# #
# #     def Callback_Clock(self, dt):
# #         self.root.ids.gb._python_access.text = "I Changed It By Clock! dt=" + str(dt)
# #
# #
# # if __name__ == '__main__':
# #     OneScreen().run()
#
# ## IMPORT THE DIFFERENT PACKAGES AND PROGRAMS NEEDED FOR THE APP TO WORK
# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SwapTransition, FadeTransition, WipeTransition, FallOutTransition, RiseInTransition
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
#
#
# ## THE BUILDER HAS THE CODE THAT DEFINES THE APPEARANCE OF THE APP. IT IS THE KIVY CODE
# Builder.load_string("""
# #:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#
# <ScreenManagement>:
#     transition: FallOutTransition()
#     Screen1:
#         id: screen1
#         name: 'screen1'
#     Screen2:
#         id: screen2
#         name: 'screen2'
#
# ############################################################SCREEN 1########################################
# <Screen1>:
#
#     RelativeLayout:
#
#         Label:
#             id: screen1_label
#             text: 'This screen just shows a TextInput and a slider'
#             pos_hint: {'x': 0.5, 'y': 0.9}
#             size_hint: (0.15, 0.05)
#             font_size: (screen1_label.width + screen1_label.height) / 6
#             bold: True
#
#         TextInput:
#             id: screen1_textinput
#             text: ''
#             hint_text: 'This is a TextInput. Just enter some text'
#             background_color: (1, 0, 0, 1)
#             foreground_color: (1, 1, 1, 1)
#             pos_hint: {'x': 0.05, 'y': 0.8}
#             size_hint: (0.5, 0.05)
#             font_size: (screen1_textinput.width + screen1_textinput.height) / 32
#
#         Button:
#             id: screen1_buttontoscreen2
#             text: 'Move to screen 2'
#             pos_hint: {'x': 0.18, 'y': 0.02}
#             size_hint: (0.2, 0.05)
#             background_color: (1, 1, 1, 1)
#             color: (0, 0, 1, 1)
#             font_size: (screen1_buttontoscreen2.width + screen1_buttontoscreen2.height) / 12
#             on_release:
#                 root.manager.current = 'screen2'
#
#
# <Screen2>:
#
#     screen2_textinput: screen2_textinput
#
#     RelativeLayout:
#
#         Label:    # Label is just text
#             id: screen2_label
#             text: 'This screen just collects the inputs from Screen 1'
#             pos_hint: {'x': 0.5, 'y': 0.9}
#             size_hint: (0.15, 0.05)
#             font_size: (screen2_label.width + screen2_label.height) / 6
#             bold: True
#
#         TextInput:
#             id: screen2_textinput
#             text: ''
#             background_color: (1, 0, 0, 1)
#             foreground_color: (1, 1, 1, 1)
#             pos_hint: {'x': 0.5, 'y': 0.45}
#             size_hint: (0.3, 0.05)
#             font_size: (screen2_textinput.width + screen2_textinput.height) / 10
#
#         Button:
#             id: screen2_buttontoscreen1
#             text: 'Move to screen 1'
#             pos_hint: {'x': 0.18, 'y': 0.02}
#             size_hint: (0.2, 0.05)
#             background_color: (1, 1, 1, 1)
#             color: (0, 0, 1, 1)
#             font_size: (screen2_buttontoscreen1.width + screen2_buttontoscreen1.height) / 12
#             on_release:
#                 root.manager.current = 'screen1'
#
# """)
#
#
# ## THIS PART IS THE PYTHON CODE
# class Screen1(Screen):
#     pass
#
#
# class Screen2(Screen):
#     def on_enter(self, *args):
#         self.screen2_textinput.text = self.manager.ids.screen1.ids.screen1_textinput.text
#
#
# class ScreenManagement(ScreenManager):
#     pass
#
#
# class whAppever(App):
#     def build(self):
#         return ScreenManagement()
#
#
# if __name__ == '__main__':
#     whAppever().run()

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pop
    size_hint: .4, .4
    auto_dismiss: False
    title: 'Hello world!!'
    Button:
        text: 'Click here to dismiss'
        on_press: pop.dismiss()
''')


class SimplePopup(Popup):
    pass

class SimpleButton(Button):
    text = "Fire Popup !"
    def fire_popup(self):
        pops=SimplePopup()
        pops.open()

class SampleApp(App):
    def build(self):
        return SimpleButton()

SampleApp().run()