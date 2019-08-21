# ---------- KIVY TUTORIAL PT 5  ----------

# ---------- kivytut.py  ----------

import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.lang import Builder

# ---------- sample.kv  ----------
Builder.load_string('''

#: import CheckBox kivy.uix.checkbox
<CustLabel@Label>:
    color: 0, 0, 0, 1

<CustomPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: "The Popup"
    Button:
        text: "Close"
        on_press: root.dismiss()

<SampBoxLayout>:
    orientation: "vertical"
    padding: 10
    spacing: 10

    # ---------- Holds CheckBox and RadioBox ----------
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .22
            CustLabel:
                text: "Are you over 18"
                size_hint_x: .80
            CheckBox:
                on_active: root.checkbox_18_clicked(self, self.active)
                size_hint_x: .20
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .55
            CustLabel:
                text: "Favorite Color"
                color: 0, 0, 0, 1
                size_hint_x: .265
            CheckBox:
                group: "fav_color"
                value: root.blue
                size_hint_x: .05
            CustLabel:
                text: "Blue"
                color: 0, 0, 0, 1
                size_hint_x: .15
            CheckBox:
                group: "fav_color"
                value: root.red
                size_hint_x: .05
            CustLabel:
                text: "Red"
                color: 0, 0, 0, 1
                size_hint_x: .15
            CheckBox:
                group: "fav_color"
                value: root.green
                size_hint_x: .05
            CustLabel:
                text: "Green"
                color: 0, 0, 0, 1
                size_hint_x: .15

    # ---------- Holds Slider & Switch ----------
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25
            CustLabel:
                text: str(slider_id.value)

            # Define the min, max, starting value and how
            # much the value changes with each move
            Slider:
                id: slider_id
                min: -100
                max: 100
                value: 0
                step: 1

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25
            CustLabel:
                text: "On / Off"

            Switch:
                id: switch_id
                on_active: root.switch_on(self, self.active)

    # ---------- Displays Popup & Spinner ----------
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            # When clicked the popup opens
            Button:
                text: "Open Popup"
                on_press: root.open_popup()

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            Spinner:
                text: "Define your class, Click Here.."
                values: ["EC2A", "EC2B", "EC2C", "EC2D", "EC4A", "EC4B", "EC4C", "EC4D", "EC6A", "EC6B", "EC6C", "EC6D", "IKI2", "IKI4", "IKI6", "IKI8"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)

    # ---------- Displays TabbedPanel ----------
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            TabbedPanel:
                do_default_tab: False

                TabbedPanelItem:
                    text: "1st Tab"
                    Label:
                        text: "Content of First Panel"
                TabbedPanelItem:
                    text: "2nd Tab"
                    Label:
                        text: "Content of Second Panel"
                TabbedPanelItem:
                    text: "3rd Tab"
                    Label:
                        text: "Content of Third Panel"
''')

# Used to display popup
class CustomPopup(Popup):
    pass

class SampBoxLayout(BoxLayout):

    # For checkbox
    checkbox_is_active = ObjectProperty(False)
    def checkbox_18_clicked(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")

    # For radio buttons
    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    # For Switch
    def switch_on(self, instance, value):
        if value is True:
            print("Switch On")
        else:
            print("Switch Off")

    # Opens Popup when called
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

    # For Spinner
    def spinner_clicked(self, value):
        print("Kelas " + value)


class SampleApp(App):
    def build(self):

        # Set the background color for the window
        Window.clearcolor = (1, 1, 1, 1)
        return SampBoxLayout()

sample_app = SampleApp()
sample_app.run()