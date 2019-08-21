from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.camera import Camera

import os
import cv2
import numpy as np
import pickle
import requests
import json
import time

from datetime import date, timedelta, datetime
from functools import partial

from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', '0')  # 0 being off 1 being on as in true/false
# Config.set('graphics', 'width', '1366') # ukuran laptop 12 inch
# Config.set('graphics', 'height', '768')
Config.set('graphics', 'width', '1360')  # ukuran laptop 12 inch
Config.set('graphics', 'height', '765')
Config.write()

Window.size = (1365, 750)
Window.fullscreen = False

Builder.load_string('''

<MainScreen>:
    name: 'main'
    
    # self.lab = (Label(text="Training Finish", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .6}))
    # self.box.add_widget(self.lab)
    # self.but = (Button(text="close", size_hint=(None, None), width=200, height=50, pos_hint={'x': .27, 'y': 0}))
    # size_hint: .5, .25
    # pos_hint: {"x": 50, 'y':10}

    BoxLayout:
        Button:
            text: 'Add Data'
            # size_hint: 0.6, 0.2
            # pos_hint: {"x":0.2, "y":1}
            # on_press => program akan dijalankan ketika tombol ditekan
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'add_data'
        Button:
            text: 'Absent'
            # size_hint: 0.6, 0.2
            # pos_hint: {"x":0.2, "y":2}
            # on_release => program akan dijalankan ketika tombol dilepas/atau selesai ditekan
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'do_absent'
                    

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
                hint_text : 'Tap to input your name...'
                # font_size: 10
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                multiline: False

            Label:
                text: 'N I M'
            TextInput:
                id: nim_id
                hint_text : 'Tap to input your N I M...'
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                multiline: False

            Label:
                text: 'Class'
            Spinner:
                text: "Define your class, Tap Here.."
                values: ["EC2A", "EC2B", "EC2C", "EC2D", "EC4A", "EC4B", "EC4C", "EC4D", "EC6A", "EC6B", "EC6C", "EC6D", "IKI2", "IKI4", "IKI6", "IKI8"]
                id: kelas_id
                on_text: kelas_id.text
                # on_text: root.spinner_clicked(kelas_id.text)

            Label:
                text: 'Birth Place'
            TextInput:
                id: tmp_lahir_id
                hint_text : 'Tap to input your Birth Place...'
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
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
                TextInput:
                    id: j_kel_id
                    padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                    hint_text: 'Tap Man/Woman'
                    halign : 'center'
                Button:
                    text: 'Woman'
                    on_press: root.btn_j_kel_p()

            Label:
                text: 'Address'
            TextInput:
                id: alamat_id
                hint_text : 'Tap to input your Adrress...'
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                multiline: False

            Label:
                text: 'Telp(+62)'
            TextInput:
                id: no_telp_id
                hint_text : 'Tap to input your Phone Number...'
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                multiline: False

            Label:
                text: 'Email'
            TextInput:
                id: email_id
                hint_text : 'Tap to input your Email...'
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
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
                on_release:
                    root.save()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'main'


<ScreenOne>:
    name: 'do_absent'

    nama2: nama_id
    nim2: nim_id
    kelas2: kelas_id
    tgl2: tgl_id
    jam2: jam_id

    GridLayout:
        cols: 1
        Label:
            size_hint: 1, .1
            color: 0,0,1,1          # R,G,B,A ( a harus 1)
            text: 'Verify Your Data'

        GridLayout:
            cols: 3
            size_hint: 0.5, .5
            Button:
                text: 'Scan Now'
                on_release:
                    root.predict()
            Image:
                id: imageView
                source: 'imgs/user.png'
                size_hint: 0.3, .1
                allow_stretch: True     
            Button:
                text:'Train Again'
                on_release: 
                    root.manager.current = 'train_again'

        GridLayout:
            orientation: 'horizontal'
            cols: 2
            Label:
                text: 'Name'
            TextInput:
                id: nama_id
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                hint_text: 'Your Name will appear soon...'
                halign : 'center'
                multiline: False
            Label:
                text: 'N I M'
            TextInput:
                id: nim_id
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                hint_text: 'Your N I M will appear soon...'
                halign : 'center'
                multiline: False
            Label:
                text: 'Class'
            TextInput:
                id: kelas_id
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                hint_text: 'Your Class will appear soon...'
                halign : 'center'
                multiline: False
            Label:
                text: 'Date'
            TextInput:
                id: tgl_id
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                hint_text: 'Current absence Date'
                halign : 'center'
                multiline: False
            Label:
                text: 'Time'
            TextInput:
                id: jam_id
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                hint_text: 'Current absence Time'
                halign : 'center'
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
                    root.send_data()
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'main'
                    
<ScreenThree>:
    name: 'train_again'
    
    nama: nama_id

    GridLayout:
        cols: 1
        padding: 100,100
        # Label:
        #     size_hint_y: .0
        #     color: 1,1,1,1          # R,G,B,A ( a harus 1)
        #     text: 'Train Data for New Images'

        GridLayout:
            orientation: 'horizontal'
            cols: 1
            size_hint_y: .1
            # padding_y: .
            Label:
                text: 'Train New Image'
                # size_hint: 1, .1
                font_size: 20
            TextInput:
                id: nama_id
                # size_hint: 1, .1
                # padding: 10,10
                padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
                hint_text: 'Input Your Name'
                halign : 'center'
                multiline: False
                font_size: 20

        BoxLayout:
            size_hint_y: .1
            Button:
                text: '<'
                size_hint_x: 0.15
                padding: 10,10
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'do_absent'
            Button:
                text:'40 Sample (Recommended)'
                # padding: 10,10
                on_release:
                    root.capt_40()
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'do_absent'
            Button:
                text:'50 Sample'
                # padding: 10,10
                on_release:
                    root.capt_50()
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'do_absent'
<Pop>:
    name: 'pop'
    Label:
        text: "You pressed the button"
        size_hint: 0.6, 0.2
        pos_hint: {"x":0.2, "top":1}

    Button:
        text: "Close"
        size_hint: 0.8, 0.2
        pos_hint: {"x":0.1, "y":0.1}
''')

class MainScreen(Screen):
    pass


class ScreenOne(BoxLayout, Screen):  # Class Absent
    nama2 = ObjectProperty(None)
    nim2 = ObjectProperty(None)
    kelas2 = ObjectProperty(None)
    tgl2 = ObjectProperty(None)
    jam2 = ObjectProperty(None)

    def predict(self):
        recognizer = cv2.face.EigenFaceRecognizer_create()
        recognizer.read('train/40sample.yml')

        with open('pickle/40sample.pickle', 'rb') as f:  # open file pickle yg berisi label orang
            og_labels = pickle.load(f)
            labels = {v: k for k, v in og_labels.items()}  # value : key  dari 'person-name' : 1 =>>> 1 : 'person-name'

        cam = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier('face-detect.xml')

        nama = ""

        finis_time = datetime.now() + timedelta(seconds=5)

        while datetime.now() < finis_time:
            _, frame = cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img = cv2.equalizeHist(gray)
            faces = face_cascade.detectMultiScale(img, 1.3, 5)  # scaleFactor=1.5, minNeighbors = 5

            for x, y, w, h in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                roi_gray = img[y:y + h, x:x + w]
                # recognizer
                id_, conf = recognizer.predict(cv2.resize(roi_gray, (280, 280)))
                if conf >= 45:
                    print(id_)
                    print(labels[id_])
                    cv2.putText(frame, 'Nama = ' + str(labels[int(id_)]).replace('-', ' '), (10, 465),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(frame, 'ID : ' + str(id_), (10, 435), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
                                cv2.LINE_AA)
                    mhs = labels[id_].replace('-', ' ')
                    nama = mhs

            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) == 27:
                break

        cam.release()
        cv2.destroyAllWindows()

        print(nama)
        if nama == "" or nama == "Unknown":
            print("[INFO] Unknown Face, Please Try Again!!!")
            self.predict()
        else:
            with open('images/' + nama.title() + '/data.txt', 'r') as file:
                data = json.load(file)

                for x in data['bio']:
                    jsin = x
                    jsonName = x['Name']
                    jsonNIM = x['N I M']
                    jsonClass = x['Class']

            print(jsin)
            print(jsonName)

            self.nama2.text = jsonName
            self.nim2.text = jsonNIM
            self.kelas2.text = jsonClass
            self.tgl2.text = str(date.today())
            self.jam2.text = str(datetime.now().strftime("%H:%M:%S"))

            self.ids.imageView.source = 'imgs/' + jsonNIM + '.png'

    def send_data(self):
        name = self.nama2.text
        nim = self.nim2.text
        clas = self.kelas2.text
        date = self.tgl2.text
        time = self.jam2.text

        print(name, nim, clas, date, time)

        self.nama2.text = ''
        self.nim2.text = ''
        self.kelas2.text = ''
        self.tgl2.text = ''
        self.jam2.text = ''


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

        # int(datetime.now().strftime('%d'))

        path = "images\\"

        """Create target Directory"""
        if name == "":
            return FileNotFoundError

        try:
            os.mkdir(path + str(name))
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

        """============================ SEND DATA INTO SERVER ==========================="""
        # url = "http://localhost/presensi/input_data.php"
        # payload = {'name': name, 'nim': nim, 'class': clas, 'birth_place': b_place, 'birth_date': b_date,
        #            'gender': gender, 'address': address,
        #            'telp': telp, 'email': mail}
        # r = requests.post(url, data=payload)
        # print(r.text)
        #
        # msgBox.showinfo(title="Success", message="Save data successfully")
        # msgBox.showwarning(title="Attention", message="Take Your Photo!!!")

        """======================================== TAKES PHOTO ================================================"""
        face_cascade = cv2.CascadeClassifier('face-detect.xml')
        cam = cv2.VideoCapture(0)

        sampleN = 0
        while True:
            ret, frame = cam.read()
            ret, img = cam.read()
            # frame = img.copy()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for x, y, w, h in faces:
                cv2.imwrite(path + str(name) + "/" + str(sampleN) + ".jpg", gray[y:y + h, x:x + w])
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleN = sampleN + 1
                cv2.waitKey(300)

            cv2.waitKey(1)
            if sampleN > 39:
                for x, y, w, h in faces:
                    # cv2.imwrite(path + str(name) + "/" + str(nim) + ".png", img[y - 75:y + h + 30, x - 10:x + w + 10])
                    cv2.imwrite('imgs/' + str(nim) + ".png", img[y - 75:y + h + 30, x - 10:x + w + 10])
                break
            cv2.imshow('img', frame)

        cam.release()
        cv2.destroyAllWindows()

        """======================== SEND PHOTO TO SERVER============================"""
        # url = 'http://localhost/presensi/img.php'
        # payload = {'nama': name.title(), 'nim': nim}
        # files = {'image': open('imgs/' + str(nim) + '.png', 'rb')}
        # r = requests.post(url, files=files, data=payload, timeout=60)
        # print(r)

        # msgBox.showinfo(title="Success", message="All your data has been saved")
        # msgBox.showwarning(title="Attention", message="Please wait a moment")

        """====================================== TRAIN IMAGE ========================================="""
        recognizer = cv2.face.EigenFaceRecognizer_create()

        current_id = 1
        label_ids = {}
        y_labels = []
        x_train = []

        BASE_DIR = os.path.dirname(__file__)
        image_dir = os.path.join(BASE_DIR, "images")

        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.endswith('jpg') or file.endswith('JPG'):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(' ', '-').lower()

                    # berikan nomor id pada tiap label sesuai urutannya
                    if not label in label_ids:
                        label_ids[label] = current_id
                        current_id += 1
                    id_ = label_ids[label]
                    print(label_ids)

                    img = cv2.imread(path)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    img = cv2.equalizeHist(img)
                    face = face_cascade.detectMultiScale(img, 1.3, 5)
                    for x, y, w, h in face:
                        roi = img[y:y + h, x:x + w]  # wajah atau objek yg di deteksi wajah dalam matrix
                        x_train.append(cv2.resize(roi, (280, 280)))  # tambahkan roi pada list x_train
                        y_labels.append(id_)

        with open('pickle/40sample.pickle', 'wb') as f:  # labels_ids = nama folder orang, buat pake pickle 'wb'
            pickle.dump(label_ids, f)  # buat file .pickle untuk label

        recognizer.train(x_train, np.array(y_labels))
        recognizer.save('train/40sample.yml')

        print('Trainning Success')
        # msgBox.showinfo(title="Success", message="All your data has been trained")

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


class ScreenThree(Screen):
    nama = ObjectProperty(None)

    def capt_40(self):
        path = "images\\"
        name = self.nama.text

        face_cascade = cv2.CascadeClassifier('face-detect.xml')
        cam = cv2.VideoCapture(0)

        sampleN = 0
        while True:
            ret, frame = cam.read()
            # frame = img.copy()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for x, y, w, h in faces:
                cv2.imwrite(path + str(name) + "/" + str(sampleN) + ".jpg", gray[y:y + h, x:x + w])
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleN = sampleN + 1
                cv2.waitKey(300)

            cv2.waitKey(1)
            if sampleN > 39:
                break
            cv2.imshow('img', frame)

        cam.release()
        cv2.destroyAllWindows()

        # self.manager.current = 'pop'
        self.train_image()

    def capt_50(self):
        path = "images\\"
        name = self.nama.text

        face_cascade = cv2.CascadeClassifier('face-detect.xml')
        cam = cv2.VideoCapture(0)

        sampleN = 0
        while True:
            ret, frame = cam.read()
            # frame = img.copy()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for x, y, w, h in faces:
                cv2.imwrite(path + str(name) + "/" + str(sampleN) + ".jpg", gray[y:y + h, x:x + w])
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleN = sampleN + 1
                cv2.waitKey(300)

            cv2.waitKey(1)
            if sampleN > 49:
                break
            cv2.imshow('img', frame)

        cam.release()
        cv2.destroyAllWindows()

        self.manager.current = 'pop'
        self.train_image()

    def train_image(self):

        face_cascade = cv2.CascadeClassifier('face-detect.xml')
        recognizer = cv2.face.EigenFaceRecognizer_create()

        current_id = 1
        label_ids = {}
        y_labels = []
        x_train = []

        BASE_DIR = os.path.dirname(__file__)
        image_dir = os.path.join(BASE_DIR, "images")

        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.endswith('jpg') or file.endswith('JPG'):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(' ', '-').lower()

                    # berikan nomor id pada tiap label sesuai urutannya
                    if not label in label_ids:
                        label_ids[label] = current_id
                        current_id += 1
                    id_ = label_ids[label]
                    print(label_ids)

                    img = cv2.imread(path)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    img = cv2.equalizeHist(img)
                    face = face_cascade.detectMultiScale(img, 1.3, 5)
                    for x, y, w, h in face:
                        roi = img[y:y + h, x:x + w]  # wajah atau objek yg di deteksi wajah dalam matrix
                        x_train.append(cv2.resize(roi, (280, 280)))  # tambahkan roi pada list x_train
                        y_labels.append(id_)

        with open('pickle/40sample.pickle', 'wb') as f:  # labels_ids = nama folder orang, buat pake pickle 'wb'
            pickle.dump(label_ids, f)  # buat file .pickle untuk label

        recognizer.train(x_train, np.array(y_labels))
        recognizer.save('train/40sample.yml')

        print('Trainning Success')

        # self.show_popup()

    def show_popup(self):
        self.box = FloatLayout()
        self.lab = (Label(text="Training Finish", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .6}))
        self.box.add_widget(self.lab)
        self.but = (Button(text="Close", size_hint=(None, None), width=200, height=50, pos_hint={'x': .27, 'y': 0}))
        self.box.add_widget(self.but)

        self.main_pop = Popup(title="Caution", content=self.box, size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)
        self.but.bind(on_press=self.main_pop.dismiss)
        self.main_pop.open()

class Pop(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen())
sm.add_widget(ScreenOne())
sm.add_widget(ScreenTwo())
sm.add_widget(ScreenThree())
sm.add_widget(Pop())


class MainApp(App):
    def build(self):
        return sm


app = MainApp()
app.run()
