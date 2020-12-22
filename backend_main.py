import datetime
# import time
# import json
import os
import yaml
# import threading

from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from typing import Optional, List  # noqa

from backend import common_tile
from backend import tile_container
from backend import tile_manager


class Backend:

    def __init__(self):
        pass

app = FastAPI()  # noqa

be = Backend()

tm = tile_manager.TileManager(
    erah=8,
    # cc=[
    #     'grassland',
    #     'floodplains',
    #     'farm',
    #     # 'grassland',
    # ],
    cc=[
        'plains',
        'rainforest',
        'plantation',
        # 'aluminum',
        # 'river',
        'city_center'
        # 'floodplains',
        # 'campus:1'
        # 'campus'
        # 'theater_square'
        # 'farm'
        # 'desert',
        # 'campus',
        # 'river'
    ],
    i0=[
        'grasslandh',
        'floodplains',
        'farm'
    ],
    i1=[
        'grassland',
        'floodplains',
        # 'farm'
        'plantation'
    ]
)

# for item, val in tm.cc.terrain.__dict__.items():
#     print(f"    {item} : {val}")

print(tm.cc.__dict__)
print(tm.cc.terrain)
print(tm.cc.feature)
print(tm.cc.river)
print(tm.cc.resource)
print(tm.cc.improvement)
print(tm.cc.district)
print('')
print(f"food: {tm.cc.food}")
print(f"production: {tm.cc.production}")
print(f"gold: {tm.cc.gold}")
print(f"science: {tm.cc.science}")
# print('\n\ndict keys here')
# print(tm.cc.__dict__.keys())
# print('')
# print(tm.cc.terrain.__dict__.keys())
# print('')
# print(tm.cc.improvement.__dict__.keys())
# print('\n\n')
tm.calculate_city_yield()
# tm.calculate_tile_yield()
# print(tm.cc.district.__dict__)
print(f"food: {tm.cc.food}")
print(f"production: {tm.cc.production}")
print(f"gold: {tm.cc.gold}")
print(f"science: {tm.cc.science}")