#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import getcwd
import functools
from SimpleCV import Image
from SimpleCV.Camera import ScreenCamera    # need pyscreenshot
from pymouse import PyMouse
from pykeyboard import PyKeyboard

def cwd(func):
    @functools.wraps(func)
    def wrapper(path, *args, **kwargs):
        if not path.startswith('/'):
            path = '{}/images/{}'.format(getcwd(), path)
        return func(path, *args, **kwargs)
    return wrapper

Image = cwd(Image)

Screen = ScreenCamera()
Mouse = PyMouse()
Keyboard = PyKeyboard()

def getpos(image):
    source = Screen.getImage()
    fs = source.findTemplate(image,threshold=5,method='CCOEFF_NORM')
    return fs

def getimage(image):
    if isinstance(image, str):
        image = Image(image)
    return image

def click(image, button=1, n=1):
    """
    Click a mouse button n times at the place that image can be found
    Button is defined as 1 = left, 2 = right, 3 = middle
    """

    done = False
    image = getimage(image)

    while not done:
        fs = getpos(image)

        for match in fs:
            # it will math at the left top point
            # so add half of width and height to change to middle
            x = match.x + match.width()/2
            y = match.y + match.height()/2
            for i in range(n):
                Mouse.click(x, y, button)

        if fs:
            done = True

def doubleClick(image):
    click(image, 1, 2)

def rightClick(image):
    click(image, 2, 1)

def typeword(text, image=None):
    if image:
        image = getimage(image)
        fs = getpos(image)

        done = False

        while not done:

            if len(fs) > 0:
                match = fs[0]
                x = match.x + match.width()/2
                y = match.y + match.height()/2
                Mouse.click(x, y, 1)
                Keyboard.type_string(text)

            if fs:
                done = True

    else:
        Keyboard.type_string(text)
