# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:51:18 2019

@author: James
"""

import os
import glob
# import numpy as np

from .utils import load_image_as_array

EMULATOR_WINDOW_SHAPE = (1314, 724, 3)

MODULE_PATH = os.path.dirname(__file__)

GAME_STATE_IMAGE_PATH = f"{MODULE_PATH}\\Resources\\Images\\States\\Game\\"

PERSIST_VALUE = 5

UNKNOWN_STATE = "UNOWN"

GAME_STATE_IMAGE_INDEXES = {
    "catch_screen_day": (slice(1134, 1314), slice(604, 659)),
    "catch_screen_night": (slice(1134, 1314), slice(604, 659)),
    "berry_select_screen": (slice(962, 990), slice(297, 431)),
    "pokeball_select_screen": (slice(961, 989), slice(266, 462)),
    "danger_screen": (slice(239, 327), slice(196, 533)),
    "field_research_screen": (slice(111, 215), slice(74, 324)),
    "friends_screen": (slice(121, 232), slice(406, 571)),
    "gmail_choose_account_screen": (slice(None, None), slice(None, None)),
    "items_screen": (slice(116, 170), slice(300, 422)),
    "landing_screen": (slice(735, 787), slice(192, 529)),
    "loading_screen": (slice(1128, 1200), slice(139, 589)),
    "me_screen": (slice(116, 239), slice(140, 334)),
    "open_world_screen": (slice(1193, 1227), slice(340, 382)),
    "pokedex_screen": (slice(117, 157), slice(291, 442)),
    "pokemon_screen": (slice(121, 163), slice(281, 439)),
    "select_screen": (slice(138, 468), slice(637, 717)),
    "pokestop_screen": (slice(1184, 1218), slice(588, 623)),
    "pokestop_screen_spun": (slice(1184, 1218), slice(588, 623)),
    "returning_player_screen": (slice(725, 791), slice(151, 420)),
    "settings_screen": (slice(118, 168), slice(257, 470)),
    "shop_screen_mid": (slice(132, 154), slice(469, 489)),
    "shop_screen_top": (slice(118, 187), slice(302, 423)),
    "sign_out_screen": (slice(550, 582), slice(112, 610)),
    "special_research_screen": (slice(124, 195), slice(409, 650)),
}

POGO_PACKAGE_NAME = "com.nianticlabs.pokemongo"

PHONE_RESOLUTION = "720x1280"

GAME_STATE_ARRAYS = load_image_as_array(glob.glob(f"{GAME_STATE_IMAGE_PATH}\*"))

MSE_ATMOST = 200
