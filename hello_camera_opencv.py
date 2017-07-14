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


class CameraApp(App):
    def build(self):
        self.img1 = Image()
        labelTitle= Label(text="Hulk Monitor - TPV")
        label2= Label(text="Copyright 2017")
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(labelTitle)
        layout.add_widget(self.img1)
        layout.add_widget(label2)

        # OpenCV video capture
        self.capture = cv2.VideoCapture(0)

        # Schedule screen update
        Clock.schedule_interval(self.updateScreen, 1.0/30.0)

        return layout

    def updateScreen(self, dt):
        ret, frame = self.capture.read()
        if frame is None:
            return

        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring() # convert in texture

        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

        self.img1.texture = texture1


def main():
    CameraApp().run()


if __name__ == '__main__':
    main()