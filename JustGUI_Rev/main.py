from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from JustGUI_Rev.database import DataBase
from JustGUI_Rev.pop import popRegist, popFinishTrain, popAbsen, popFinishAbs, popNotRecognized, popFinishTrainAgain, emptyForm

import os
import json

from kivy.core.window import Window

Window.fullscreen = False


class MainScreen(Screen):
    pass

class MessageBox(Popup):
    def __init__(self, obj, **kwargs):
        super(MessageBox, self).__init__(**kwargs)
        self.obj = obj

class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def goToAbsen(self):
        if db.validate(self.email.text, self.password.text):
            self.reset()
            sm.current = "absen"
            popAbsen()
        else:
            invalidLogin()

    def gotToLoginAdmin(self):
        popup = MessageBox(self)  # pass screen1 object
        popup.open()

    def regist(self):
        self.reset()
        sm.current = 'loginAdmin'

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class LoginScreenAdmin(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def goTORegist(self):
        if db1.validate(self.email.text, self.password.text):
            self.reset()
            sm.current = "register"
            popRegist()
        else:
            invalidLogin()

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class RegisterScreen(Screen):
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

        path = "images\\"

        """Create target Directory"""
        if name == "" or nim == "" or clas=="" or b_place=="" or b_date=="" or mail=="":
            emptyForm()
            return FileNotFoundError

        try:
            os.mkdir('images/' + str(name))
            print("Directory ", path + str(name), " Created ")

        except FileExistsError:
            print("Directory ", path + str(name), " already exists")

        """Write Data JSON"""
        data = {}
        data['bio'] = [
            {"Name": name, "N I M": nim, "Class": clas, "Birth Place": b_place, "Birth Date": b_date, "Gender": gender,
             "Address": address, "Telp": telp, "E-Mail": mail},
        ]

        with open('images/' + name + '/data.txt', 'w') as file:
            json.dump(data, file)

        """========================== CREATE ACCOUNT LOGIIN =================================="""
        if name != "" and mail != "" and mail.count("@") == 1 and mail.count(".") > 0:
            if nim != "":
                db.add_user(mail, nim, name)
            else:
                invalidForm()
        else:
            invalidForm()

        popFinishTrain()

        self.btn_back()

        sm.current = 'login'


class AbsenScreen(Screen):
    nama2 = ObjectProperty(None)
    nim2 = ObjectProperty(None)
    kelas2 = ObjectProperty(None)
    tgl2 = ObjectProperty(None)
    jam2 = ObjectProperty(None)

    def reset(self):
        self.nama2.text = ''
        self.nim2.text = ''
        self.kelas2.text = ''
        self.tgl2.text = ''
        self.jam2.text = ''
        self.ids.imageView.source = 'img_server/user.jpg'

    def predict(self):
        popNotRecognized()
        self.ids.imageView.source = 'img_server/user.png'

    def send_data(self):
        self.reset()
        popFinishAbs()
        sm.current='main'


class OtherScreen(Screen):
    nama = ObjectProperty(None)

    def capt_40(self):
        name = self.nama.text

        if name == "":
            emptyForm()
            return FileNotFoundError

        popFinishTrainAgain()
        self.nama.text = ""
        sm.current = 'absen'

    def capt_50(self):
        name = self.nama.text

        if name == "":
            emptyForm()
            return FileNotFoundError

        popFinishTrainAgain()
        self.nama.text = ""
        sm.current = 'absen'


def invalidLogin():
    pop = Popup(title='Invalid Login', content=Label(text='Invalid username or password.'), size_hint=(None, None), size=(450, 300))
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='Please fill in all inputs with valid information.'), size_hint=(None, None), size=(450, 300))
    pop.open()


kv = Builder.load_file("my.kv")

sm = ScreenManager()
db = DataBase("users.txt")
db1 = DataBase("admin.txt")

screens = [MainScreen(), LoginScreen(name="login"), LoginScreenAdmin(), RegisterScreen(), AbsenScreen(), OtherScreen()]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()