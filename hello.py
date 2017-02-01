#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

if __name__ == '__main__':
    TestApp().run()