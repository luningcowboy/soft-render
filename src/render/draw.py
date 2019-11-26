#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 一 11/25 20:09:40 2019
# File Name: src/render/draw.py
# Description:
"""
from base import *
def drawPoint(canvas, point, color="#FFFFFF"):
    canvas.create_line(point.getX(),point.getY(),point.getX(),point.getY(), fill=color)
