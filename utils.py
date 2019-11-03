# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:49:27 2019

@author: James
"""

from PIL import Image, ImageGrab
from skimage import measure
import win32gui
import numpy as np
import os


def get_win_box(win_name):
    """
    Get the bounding box of window given it's name
    
    Parameters
    ----------
    win_name: name of the window
    """
    rect = win32gui.GetWindowRect(win32gui.FindWindow(None, win_name))
    return rect


def get_win_image(win_name):
    """
    Get the PIL image object for a given window name
    
    Parameters
    ----------
    win_name: name of the window
    """
    img = ImageGrab.grab(get_win_box(win_name))
    return img


def image_to_array(img, mode="color"):
    if mode == "color":
        return np.asarray(img)[:,:,0:3].reshape(img.size[1], img.size[0], 3)
    elif mode == "gray":
        return np.asarray(img.convert("L")).reshape(img.size[1], img.size[0])
    else:
        raise ValueError(f"invalid mode '{mode}'")


def load_image_as_array(imgpath, mode="color"):
    if isinstance(imgpath, list):
        arraydict = {}
        for ipath in imgpath:
            name = os.path.splitext(os.path.basename(ipath))[0]
            arraydict[name] = load_image_as_array(ipath, mode=mode)
        return arraydict
    else:
        img = Image.open(imgpath)
        return image_to_array(img, mode=mode)


def compare_mse_at_most(img1, img2, atmost=None):
#    print(f"img1.shape: {img1.shape}")
#    print(f"img2.shape: {img2.shape}")
    result = measure.compare_mse(img1, img2)
    if atmost is None:
        return result
    else:
        if result <= atmost:
            return result
        else:
            return np.inf
