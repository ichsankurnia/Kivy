from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_string('''
<pop>:
    angka1: angka1_id
    angka2: angka2_id
    hasil: hasil_id
    
    GridLayout:
        cols:1
        size: root.width, root.height
        GridLayout:
            cols:2
            # orientation: 'vertical'
            Label:
                text: 'Masukan angka pertama'
                size_hint: 2, .2
            TextInput:
                id: angka1_id
                size_hint: 1, .1
            Label:
                text: 'Masukan angka kedua'
                size_hint: 2, .2
            TextInput:
                id: angka2_id
                size_hint: 1, .1
            Button:
                id: main_button
                text: "Tambah"
                font_size: 25
                size_hint: None, None
                width: root.width / 2
                height: 60
                on_press: root.tambah()
            Button:
                id: main_button
                text: "Kurang"
                font_size: 25
                size_hint: None, None
                width: root.width / 2
                height: 60
                on_press: root.kurang()
            Button:
                id: main_button
                text: "Kali"
                font_size: 25
                size_hint: None, None
                width: root.width / 2
                height: 60
                on_press: root.kali()
            Button:
                id: main_button
                text: "Bagi"
                font_size: 25
                size_hint: None, None
                width: root.width / 2
                height: 60
                on_press: root.bagi()
        Label:
            id: hasil_id
            text: 'The result will appear soon'
            size_hint: 5, .5
''')


class pop(Widget):
    angka1 = ObjectProperty(None)
    angka2 = ObjectProperty(None)
    hasil = ObjectProperty(None)

    def tambah(self):
        self.show_popup_tambah()
        number1 = self.angka1.text
        number2 = self.angka2.text
        result = int(number1) + int(number2)
        self.hasil.text = str(result)

    def kurang(self):
        self.show_popup_kurang()
        number1 = self.angka1.text
        number2 = self.angka2.text
        result = int(number1) - int(number2)
        self.hasil.text = str(result)

    def kali(self):
        self.show_popup_kali()
        number1 = self.angka1.text
        number2 = self.angka2.text
        result = int(number1) * int(number2)
        self.hasil.text = str(result)

    def bagi(self):
        self.show_popup_bagi()
        number1 = self.angka1.text
        number2 = self.angka2.text
        result = int(number1) / int(number2)
        self.hasil.text = str(result)

    def show_popup_tambah(self):
        self.box = FloatLayout()
        self.lab = (Label(text="Pertambahan", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .6}))
        self.box.add_widget(self.lab)
        self.but = (Button(text="close", size_hint=(None, None), width=200, height=50, pos_hint={'x': .27, 'y': 0}))
        self.box.add_widget(self.but)

        self.main_pop = Popup(title="Caution", content=self.box, size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)
        self.but.bind(on_press=self.main_pop.dismiss)
        self.main_pop.open()

    def show_popup_kurang(self):
        self.box = FloatLayout()
        self.lab = (Label(text="Pengurangan", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .6}))
        self.box.add_widget(self.lab)
        self.but = (Button(text="close", size_hint=(None, None), width=200, height=50, pos_hint={'x': 0, 'y': 0}))
        self.box.add_widget(self.but)
        self.but1 = Button(text="blank", size_hint=(None, None), width=200, height=50, pos_hint={'x': .5, 'y': 0})
        self.box.add_widget(self.but1)

        self.main_pop = Popup(title="Caution", content=self.box, size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)
        self.but.bind(on_press=self.main_pop.dismiss)
        self.but1.bind(on_press=self.main_pop.dismiss)
        self.main_pop.open()

    def show_popup_kali(self):
        self.box = FloatLayout()
        self.lab = (Label(text="Perkalian", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .6}))
        self.box.add_widget(self.lab)
        self.but = (Button(text="close", size_hint=(None, None), width=200, height=50, pos_hint={'x': 0, 'y': 0}))
        self.box.add_widget(self.but)
        self.but1 = Button(text="blank", size_hint=(None, None), width=200, height=50, pos_hint={'x': .5, 'y': 0})
        self.box.add_widget(self.but1)

        self.main_pop = Popup(title="Caution", content=self.box, size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)
        self.but.bind(on_press=self.main_pop.dismiss)
        self.but1.bind(on_press=self.main_pop.dismiss)
        self.main_pop.open()

    def show_popup_bagi(self):
        self.box = FloatLayout()
        self.lab = (Label(text="Pembagian", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .6}))
        self.box.add_widget(self.lab)
        self.but = (Button(text="close", size_hint=(None, None), width=200, height=50, pos_hint={'x': 0, 'y': 0}))
        self.box.add_widget(self.but)
        self.but1 = Button(text="blank", size_hint=(None, None), width=200, height=50, pos_hint={'x': .5, 'y': 0})
        self.box.add_widget(self.but1)

        self.main_pop = Popup(title="Caution", content=self.box, size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)
        self.but.bind(on_press=self.main_pop.dismiss)
        self.but1.bind(on_press=self.main_pop.dismiss)
        self.main_pop.open()

class PopApp(App):
    def build(self):
        return pop()


PopApp().run()
