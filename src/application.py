#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 一 11/25 20:19:52 2019
# File Name: src/app.py
# Description:
"""

from tkinter import *
import render as render

class Application(object):
    def __init__(self):
        self._width = 800
        self._height = 600
        self._bgColor = 'black'
        self._title = 'test'
        self.init()
    def init(self):
        self.root = Tk()
        self.root.title(self._title)
        self.canvas = Canvas(self.root, background=self._bgColor, width=self._width, height=self._height)
        self.canvas.pack(fill=BOTH, expand=YES)
    def draw(self):
        #self.canvas.create_line(0, 10, 10, 10, fill="#FF0000")
        render.draw.drawPoint()
    def run(self):
        self.draw()
        self.root.mainloop()
