#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 一 11/25 20:11:46 2019
# File Name: src/base/point.py
# Description:
"""

class Point(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    def getX(self):
        return self._x
    def getY(self):
        return self._y
