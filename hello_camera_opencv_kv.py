#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
 
import cv2
import numpy as np


class HelloCameraOpenCVLayout(BoxLayout):
    def play(self):
        print("play")


class HelloCameraOpenCV(App):
    def build(self):
        # OpenCV video capture        
        self.capture = cv2.VideoCapture(1)

        # Window Layout
        self.layout = HelloCameraOpenCVLayout()
        self.img1 = self.layout.ids['img1']
        
        # Schedule screen update
        Clock.schedule_interval(self.updateScreen, 1.0/30.0)

        return self.layout

    def updateScreen(self, dt):
        # capture frame
        ret, frame = self.capture.read()
         
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring() # convert in texture
         
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
         
        self.img1.texture = texture1

    def on_stop(self):
        self.capture.release()
        del self.capture
        print("stop")


def main():
    HelloCameraOpenCV().run()


if __name__ == '__main__':
    main()