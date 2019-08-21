# # from kivy.app import App
# # from kivy.lang import Builder
# # from kivy.uix.boxlayout import BoxLayout
# # import time
# #
# #
# # Builder.load_string('''
# # <CameraClick>:
# #     orientation: 'vertical'
# #     Camera:
# #         id: camera
# #         resolution: (640, 480)
# #         play: False
# #     ToggleButton:
# #         text: 'Play'
# #         on_press: camera.play = not camera.play
# #         size_hint_y: None
# #         height: '48dp'
# #     Button:
# #         text: 'Capture'
# #         size_hint_y: None
# #         height: '48dp'
# #         on_press: root.capture()
# # ''')
# #
# #
# # class CameraClick(BoxLayout):
# #     def capture(self):
# #         '''
# #         Function to capture the images and give them the names
# #         according to their captured time and date.
# #         '''
# #         camera = self.ids['camera']
# #         timestr = time.strftime("%Y%m%d_%H%M%S")
# #         camera.export_to_png("IMG_{}.png".format(timestr))
# #         print("Captured")
# #
# #
# # class TestCamera(App):
# #
# #     def build(self):
# #         return CameraClick()
# #
# #
# # TestCamera().run()
#
# __author__ = 'bunkus'
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.image import Image
# from kivy.clock import Clock
# from kivy.graphics.texture import Texture
#
# from kivy.core.window import Window
# from kivy.config import Config
# # Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
# # Config.set('graphics', 'width', '1366') # ukuran laptop 12 inch
# # Config.set('graphics', 'height', '768')
# Config.set('graphics', 'width', '1080') # ukuran laptop 12 inch
# Config.set('graphics', 'height', '720')
# Config.write()
#
# # Window.size = (300, 100)
# Window.fullscreen = False
#
# import cv2
#
# class CamApp(App):
#
#     def build(self):
#         self.img1=Image()
#         layout = BoxLayout()
#         layout.add_widget(self.img1)
#         #opencv2 stuffs
#         self.capture = cv2.VideoCapture(0)
#         cv2.namedWindow("CV2 Image")
#         Clock.schedule_interval(self.update, 1.0/33.0)
#         return layout
#
#     def update(self, dt):
#         # display image from cam in opencv window
#         ret, frame = self.capture.read()
#         # cv2.imshow("CV2 Image", frame)
#         # convert it to texture
#         buf1 = cv2.flip(frame, 0)
#         buf = buf1.tostring()
#         texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#         texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#         # display image from the texture
#         self.img1.texture = texture1
#
# if __name__ == '__main__':
#     CamApp().run()
#     cv2.destroyAllWindows()

from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2


class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture


class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        return self.my_camera

    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()


if __name__ == '__main__':
    CamApp().run()