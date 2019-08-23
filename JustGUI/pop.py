from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button


def popRegist():
    box = FloatLayout()
    lab = (Label(text="Enter your data and save", font_size=15, size_hint=(None, None), pos_hint={'x': .37, 'y': .6}))
    box.add_widget(lab)
    lab = (Label(text="Camera will appear to take pictures", font_size=15, size_hint=(None, None), pos_hint={'x': .37, 'y': .4}))
    box.add_widget(lab)
    lab = (Label(text="Wait until the next notification appears \n          and the training is complete", font_size=15, size_hint=(None, None), pos_hint={'x': .37, 'y': .3}))
    box.add_widget(lab)
    but = (Button(text="OK", size_hint=(None, None), width=200, height=50, pos_hint={'x': .27, 'y': 0}))
    box.add_widget(but)

    main_pop = Popup(title="Data Registration", content= box, size_hint=(None, None), size=(470, 300), auto_dismiss=False, title_size=15)
    but.bind(on_press=main_pop.dismiss)
    main_pop.open()

def emptyForm():
    box = FloatLayout()
    lab = (Label(text="Empty Form", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .6}))
    lab1 = (Label(text="There is a form that hasn't been filled yet", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .4}))
    box.add_widget(lab)
    box.add_widget(lab1)
    lab2 = (Label(text="Make sure to fill all form", font_size=15, size_hint=(None, None),pos_hint={'x': .35, 'y': .3}))
    box.add_widget(lab2)
    but = (Button(text="OK", size_hint=(None, None), width=200, height=50, pos_hint={'x': .27, 'y': 0}))
    box.add_widget(but)

    main_pop = Popup(title="Warning", content=box, size_hint=(None, None), size=(450, 300), auto_dismiss=False,
                     title_size=15)
    but.bind(on_press=main_pop.dismiss)
    main_pop.open()

def popFinishTrain():
    box = FloatLayout()
    lab = (Label(text="Data Saved Successfully", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .5}))
    lab1 = (Label(text="Please Login", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .4}))
    box.add_widget(lab)
    box.add_widget(lab1)
    but = (Button(text="OK", size_hint=(None, None), width=200, height=50, pos_hint={'x': .27, 'y': 0}))
    box.add_widget(but)

    main_pop = Popup(title="Training Finish", content= box, size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)
    but.bind(on_press=main_pop.dismiss)
    main_pop.open()

def popFinishTrainAgain():
    box = FloatLayout()
    lab = (Label(text="Data Saved Successfully", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .5}))
    lab1 = (Label(text="Absent Again", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .4}))
    box.add_widget(lab)
    box.add_widget(lab1)
    but = (Button(text="OK", size_hint=(None, None), width=200, height=50, pos_hint={'x': .27, 'y': 0}))
    box.add_widget(but)

    main_pop = Popup(title="Training Finish", content= box, size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)
    but.bind(on_press=main_pop.dismiss)
    main_pop.open()

def popAbsen():
    box = FloatLayout()
    lab = (Label(text="Press Scan Now button to scan your face", font_size=15, size_hint=(None, None), pos_hint={'x': .38, 'y': .6}))
    box.add_widget(lab)
    lab = (Label(text="If the face is not recognized,", font_size=15, size_hint=(None, None), pos_hint={'x': .38, 'y': .4}))
    box.add_widget(lab)
    lab = (Label(text="press Train Again button to train new image", font_size=15,
                 size_hint=(None, None), pos_hint={'x': .38, 'y': .3}))
    box.add_widget(lab)
    but = (Button(text="OK", size_hint=(None, None), width=200, height=50, pos_hint={'x': .27, 'y': 0}))
    box.add_widget(but)

    main_pop = Popup(title="Caution", content= box, size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)
    but.bind(on_press=main_pop.dismiss)
    main_pop.open()

def popFinishAbs():
    box = FloatLayout()
    lab = (Label(text="Absence Finish", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .5}))
    lab1 = (Label(text="Thank You!!!", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .4}))
    box.add_widget(lab)
    box.add_widget(lab1)
    but = (Button(text="OK", size_hint=(None, None), width=200, height=50, pos_hint={'x': .27, 'y': 0}))
    box.add_widget(but)

    main_pop = Popup(title="Success", content= box, size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)
    but.bind(on_press=main_pop.dismiss)
    main_pop.open()

def popNotRecognized():
    box = FloatLayout()
    lab = (Label(text="Face is Not Recognized", font_size=15, size_hint=(None, None), pos_hint={'x': .35, 'y': .5}))
    lab1 = (Label(text="Please try again or Press Train Again Button to train new image", font_size=15, size_hint=(None, None), pos_hint={'x': .38, 'y': .4}))
    box.add_widget(lab)
    box.add_widget(lab1)
    but = (Button(text="OK", size_hint=(None, None), width=200, height=50, pos_hint={'x': .27, 'y': 0}))
    box.add_widget(but)

    main_pop = Popup(title="Warning!!", content= box, size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)
    but.bind(on_press=main_pop.dismiss)
    main_pop.open()