# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:47:00 2019

@author: James
"""

import time
import io

import numpy as np

from PIL import Image

from noxemu.noxemu import NoxEmulator

from .defs import PHONE_RESOLUTION, POGO_PACKAGE_NAME, GAME_STATE_ARRAYS, GAME_STATE_IMAGE_INDEXES, MSE_ATMOST, UNKNOWN_STATE, EMULATOR_WINDOW_SHAPE

from .utils import (
    image_to_array,
    load_image_as_array,
    compare_mse_at_most,
)


class PyGo:
    def __init__(self):
        self._emu = NoxEmulator(title=f"PyGo", resolution=PHONE_RESOLUTION)
        time.sleep(2)
        try:
            self._emu.launch_package(POGO_PACKAGE_NAME)
        except ValueError:
            del self._emu
            raise ValueError("Unable to launch pokemon go. make sure it is installed on enough clones.")
        
    def get_state(self):
        img = Image.open(io.BytesIO(self._emu.adb_device.screencap()))
        img_array = np.empty(EMULATOR_WINDOW_SHAPE)
        img_array[32:1312,2:722,:] = image_to_array(img)
        mse_dict = {}
        for name, state_array in GAME_STATE_ARRAYS.items():
            index = GAME_STATE_IMAGE_INDEXES[name]
            mse_dict[name] = compare_mse_at_most(
                img_array[index], state_array[index], MSE_ATMOST
            )

        # check for nan values
        if all(val == np.inf for val in mse_dict.values()):
            return UNKNOWN_STATE, np.inf
        else:
            state = min(mse_dict, key=mse_dict.get)
            return state, mse_dict[state]    
    
    def __enter__(self):
        return self
    
    def __exit__(self):
        del self
        
    def __del__(self):
        del self._emu

