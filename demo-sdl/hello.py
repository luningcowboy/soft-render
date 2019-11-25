#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 一 11/25 13:31:17 2019
# File Name: demo-sdl/hello.py
# Description:
"""
import sys
import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, "resources")

def run():
    sdl2.ext.init()
    win = sdl2.ext.Window("HelloWorld", size=(800, 600))
    renderer = sdl2.ext.Renderer(win)
    factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer = renderer)
    win.show()
    processor = sdl2.ext.TestEventProcessor()
    processor.run(win)
    sdl2.ext.quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())

