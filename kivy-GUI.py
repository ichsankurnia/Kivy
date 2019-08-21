from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
# from kivy.config import Config

# Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
# Config.set('graphics', 'width', '1400')
# Config.set('graphics', 'height', '720')
# Config.write()

# Config.set('graphics', 'fullscreen', 'auto')
# Config.set('graphics', 'window_state', 'maximized')
# Config.write()

# Window.size = (300, 100)
# Window.fullscreen = 'auto'
Window.fullscreen = False

Builder.load_string('''

<MainScreen>:
    name: 'main'        # Nama screen

    BoxLayout:
        Button:
            text: 'Add Data'
            # on_release => program akan dijalankan ketika tombol dilepas/atau selesai ditekan
            # on_press => program akan dijalankan ketika tombol ditekan
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'add_data'   # Panggil screen add_data
        Button:
            text: 'Absent'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'do_absent'

<ScreenOne>:
    name: 'do_absent'

    GridLayout:
        cols: 1
        Label:
            size_hint: 1, .1
            color: 0.5,0.5,0.5,1          # R,G,B,A ( a harus 1) nilai default 1,1,1,1 R=1, B=1, C=1, D=1
            text: 'Verify Your Data'
        
        GridLayout:
            cols: 3
            size_hint: 0.5, .5
            Button:
                text: 'Scan Your Face Now, Click Here'
            TextInput:
                size_hint: 1, .1
                text: 'Photo'    
            Button:
                text:'Try Again'
                    
        GridLayout:
            orientation: 'horizontal'
            cols: 2
            Label:
                text: 'Name'
            TextInput:
                id: nama_id
                multiline: False
            Label:
                text: 'N I M'
            TextInput:
                id: nim_id
                multiline: False
            Label:
                text: 'Class'
            TextInput:
                id: kelas_id
                multiline: False
            Label:
                text: 'Date'
            TextInput:
                id: tgl_id
                multiline: False
            Label:
                text: 'Time'
            TextInput:
                id: jam_id
                multiline: False
            
        BoxLayout:
            size_hint_y: .2
            Button:
                size_hint_x: 0.15
                text: '<'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'main'
            Button:
                text:'Confirm'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'main'


<ScreenTwo>:
    name: 'add_data'

    nama: nama_id
    nim: nim_id
    kelas: kelas_id
    tmp_lahir: tmp_lahir_id
    tgl_lahir_y: tgl_lahir_y_id
    tgl_lahir_m: tgl_lahir_m_id
    tgl_lahir_d: tgl_lahir_d_id
    j_kel: j_kel_id
    alamat: alamat_id
    no_telp: no_telp_id
    email: email_id

    GridLayout:
        cols:1
        size: root.width, root.height
        GridLayout:
            cols: 2
            Label:
                text: 'Name'
            TextInput:
                id: nama_id
                multiline: False

            Label:
                text: 'Nim'
            TextInput:
                id: nim_id
                multiline: False

            Label:
                text: 'Class'
            Spinner:
                text: "Define your class, Click Here.."
                values: ["EC2A", "EC2B", "EC2C", "EC2D", "EC4A", "EC4B", "EC4C", "EC4D", "EC6A", "EC6B", "EC6C", "EC6D", "IKI2", "IKI4", "IKI6", "IKI8"]
                id: kelas_id
                on_text: kelas_id.text
                # on_text: root.spinner_clicked(kelas_id.text)

            Label:
                text: 'Birth Place'
            TextInput:
                id: tmp_lahir_id
                multiline: False

            Label:
                text: 'Birth Date'
            GridLayout:
                orientation: 'horizontal'
                cols: 3
                Spinner:
                    text: "Year"
                    values: ["1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003"]
                    id: tgl_lahir_y_id
                    on_text: tgl_lahir_y_id.text
                Spinner:
                    text: "Month"
                    values: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                    id: tgl_lahir_m_id
                    on_text: tgl_lahir_m_id.text
                Spinner:
                    text: "Day"
                    values: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
                    id: tgl_lahir_d_id
                    on_text: tgl_lahir_d_id.text

            Label:
                text: 'Gender'
            BoxLayout:
                orientation: "horizontal"
                Button:
                    text: 'Man'
                    on_press: root.btn_j_kel_l()
                Label:
                    id: j_kel_id
                    text: ''
                Button:
                    text: 'Woman'
                    on_press: root.btn_j_kel_p()

            Label:
                text: 'Address'
            TextInput:
                id: alamat_id
                multiline: False

            Label:
                text: 'Telp(+62)'
            TextInput:
                id: no_telp_id
                multiline: False

            Label:
                text: 'Email'
            TextInput:
                id: email_id
                multiline: False

            Button:
                text: 'Back to Main Menu'
                on_press:
                    root.btn_back()
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


class ScreenOne(BoxLayout, Screen):  # Class Absent
    pass


class ScreenTwo(Screen):
    nama = ObjectProperty(None)
    nim = ObjectProperty(None)
    kelas = ObjectProperty(None)
    tmp_lahir = ObjectProperty(None)
    tgl_lahir_y = ObjectProperty(None)
    tgl_lahir_m = ObjectProperty(None)
    tgl_lahir_d = ObjectProperty(None)
    j_kel = ObjectProperty(None)
    alamat = ObjectProperty(None)
    no_telp = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn_j_kel_l(self):
        self.j_kel.text = 'Man'
    def btn_j_kel_p(self):
        self.j_kel.text = 'Woman'

    def btn_back(self):
        self.nama.text = ''
        self.nim.text = ''
        self.kelas.text = 'Define Your Class, Click Here!'
        self.tmp_lahir.text = ''
        self.tgl_lahir_y.text = 'Year'
        self.tgl_lahir_m.text = 'Month'
        self.tgl_lahir_d.text = 'Day'
        self.j_kel.text = ''
        self.alamat.text = ''
        self.no_telp.text = ''
        self.email.text = ''

    def save(self):
        tgl_m = self.tgl_lahir_m.text
        if tgl_m == 'January':
            tgl_m = '1'
        elif tgl_m == 'February':
            tgl_m = '2'
        elif tgl_m == 'March':
            tgl_m = '3'
        elif tgl_m == 'April':
            tgl_m = '4'
        elif tgl_m == 'May':
            tgl_m = '5'
        elif tgl_m == 'June':
            tgl_m = '6'
        elif tgl_m == 'July':
            tgl_m = '7'
        elif tgl_m == 'August':
            tgl_m = '8'
        elif tgl_m == 'September':
            tgl_m = '9'
        elif tgl_m == 'October':
            tgl_m = '10'
        elif tgl_m == 'November':
            tgl_m = '11'
        else:
            tgl_m = '12'

        name = self.nama.text
        nim = self.nim.text
        clas = self.kelas.text
        b_place = self.tmp_lahir.text
        b_date = self.tgl_lahir_y.text + '-' + tgl_m + '-' + self.tgl_lahir_d.text
        gender = self.j_kel.text
        address = self.alamat.text
        telp = '+62' + self.no_telp.text
        mail = self.email.text

        print(name, nim, clas, b_place, b_date, gender, address, telp, mail)

        self.nama.text = ''
        self.nim.text = ''
        self.kelas.text = 'Define Your Class, Click Here!'
        self.tmp_lahir.text = ''
        self.tgl_lahir_y.text = 'Year'
        self.tgl_lahir_m.text = 'Month'
        self.tgl_lahir_d.text = 'Day'
        self.j_kel.text = ''
        self.alamat.text = ''
        self.no_telp.text = ''
        self.email.text = ''


sm = ScreenManager()
sm.add_widget(MainScreen())
sm.add_widget(ScreenOne())
sm.add_widget(ScreenTwo())


class MainApp(App):
    def build(self):
        return sm


app = MainApp()
app.run()
