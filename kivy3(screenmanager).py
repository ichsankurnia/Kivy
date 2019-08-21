from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty

# class MainScreen(Screen):
#     pass
#
# class AnotherScreen(Screen):
#     pass
#
# class ScreenManagement(ScreenManager):
#     transition = FadeTransition()
#
# presentation = Builder.load_file("kivy3.kv")
#
# class MainApp(App):
#     def build(self):
#         return presentation
#
# MainApp().run()

Builder.load_string('''

<MainScreen>:
    name: 'main'

    BoxLayout:
        Button:
            text: 'Add Data'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'add_data'
        Button:
            text: 'Absent'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'do_absent'
    
<ScreenOne>:
    name: 'do_absent'
    BoxLayout:
        Button:
            text: 'Click to Back to Main Menu'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'main'
                
<ScreenTwo>:
    name: 'add_data'
    
    nama: nama
    nim: nim
    kelas: kelas
                
    GridLayout:
        cols:1
        size: root.width, root.height
        GridLayout:
            cols: 2
            Label:
                text: 'Name'
            TextInput:
                id: nama
                multiline: False
            Label:
                text: 'Nim'
            TextInput:
                id: nim
                multiline: False
            Label:
                text: 'Class'
            TextInput:
                id: kelas
                multiline: False

        Button:
            text: 'Back to Main Menu'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'main'
        Button:
            text: 'Save'
            on_press:
                root.save()
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'main'
''')

class MainScreen(Screen):
    pass

class ScreenOne(Screen): # Class Absent
    pass

class ScreenTwo(Screen):
    nama = ObjectProperty(None)
    nim = ObjectProperty(None)
    kelas = ObjectProperty(None)

    def save(self):
        name = self.nama.text
        nim = self.nim.text
        clas = self.kelas.text

        print(name, nim, clas)

        self.nama.text = ''
        self.nim.text = ''
        self.kelas.text = ''

sm = ScreenManager()
sm.add_widget(MainScreen())
sm.add_widget(ScreenOne())
sm.add_widget(ScreenTwo())

class MainApp(App):
    def build(self):
        return sm

app =  MainApp()
app.run()
