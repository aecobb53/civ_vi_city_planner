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
from pydantic import BaseModel

from backend import common_tile
from backend import tile_container
from backend import tile_manager
from backend.bin.logger import Logger

environment = os.getenv('ENVIRONMENT')
if environment != 'prod':
    log_prefix = environment
    # c_level = 'DEBUG'
    c_level = 'INFO'
else:
    c_level = 'WARNING'

# Logging
logger = Logger('civ_vi', \
    log_directory='logs/backend/', \
    app_name_in_file=True, \
    log_suffix=log_prefix, \
    log_prefix='main', \
    date_in_file=False, \
    time_in_file=False, \
    utc_in_file=False, \
    f_level='DEBUG', \
    c_level=c_level)
logit = logger.return_logit()
# default_log_file = logger.file_name
# return logit, logger

# Config
with open('etc/backend.yml') as ycf:
    config = yaml.load(ycf, Loader=yaml.FullLoader)


class Terrain(BaseModel):
    name: str
    hill: bool = None


class Feature(BaseModel):
    name: str
    river: bool = None


class Resource(BaseModel):
    name: str


class Imporovement(BaseModel):
    name: str


class District(BaseModel):
    name: str
    powered: bool = True
    buildings: List[str] = []


class Wonder(BaseModel):
    name: str


class Tile(BaseModel):
    terrain: Optional[Terrain] = None
    feature: Optional[Feature] = None
    resource: Optional[Resource] = None
    imporovement: Optional[Imporovement] = None
    district: Optional[District] = None
    wonder: Optional[Wonder] = None


class CityPlan(BaseModel):
    name: str = None
    center: List[Tile] = None
    inner: List[Tile] = None
    middle: List[Tile] = None
    outer: List[Tile] = None
    nearby: List[Tile] = None

    
    # logit.debug(f"center item here {center}")
    # logit.debug(f"center item here {self.center}")
    # logit.debug(f"center type {type(center)}")

    # if len(center) < 6:
    #     center.append(None)

        


# class Item(BaseModel):
#     # name: str = None
#     # center: str = None
#     # inner: str = None
#     # middle: str = None
#     # outer: str = None
#     # nearby: str = None
#     # name: str = ''
#     # center: List[Tile]
#     # inner: List[Tile]
#     # middle: List[Tile]
#     # outer: List[Tile]
#     # nearby: List[Tile]

#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


def create_tile_manager_object(city_object):
    logit.debug('creating tile manager object')
    circles = config['circle_layers']
    tile_layers = config['tile_layers']
    city_dct = {k:[] for k in config['tile_index_list']}
    for attribute in city_object.__dict__.keys():
        if attribute in circles:
            for index, tile in enumerate(getattr(city_object, attribute)):
                tile_index = attribute[0] + str(index)
                if tile_index == 'c0':
                    tile_index = 'cc'
                if tile_index not in config['tile_index_list'] and tile_index != 'cc':
                    continue
                logit.debug(f"tile {tile_index}: {tile}")
                tile_list = []
                for layer in tile_layers:
                    try:
                        if getattr(tile, layer) is not None:
                            logit.debug(f"layer details {tile_index}-{layer}: {getattr(tile, layer)}")
                            tile_list.append(getattr(tile, layer).name)
                    except AttributeError:
                        pass
                city_dct[tile_index] = tile_list
                logit.debug(f"tile_list for {tile_index}: {tile_list}")
    tm = tile_manager.TileManager(**city_dct)
    return tm

def analize_tm(tile_object):
    indent = '    '
    for tile_index in config['tile_index_list']:
        logit.debug(f"index: {tile_index}, {getattr(tile_object, tile_index)}")
        if getattr(tile_object, tile_index) is not None:
            for layer in config['tile_layers']:
                if getattr(getattr(tile_object, tile_index), layer) is not None:
                    logit.debug(f"{indent}layer: {layer}, {getattr(getattr(tile_object, tile_index), layer)}")


app = FastAPI()
logit.debug('\npage break\n')

@app.get('/')
def heartbeat(request: Request):
    logit.debug('base endpoint hit')
    return "thump thump..."


# @app.post("/items/")
# async def create_item(item: Item):
#     logit.debug('items endpoint hit')
#     return item

@app.post("/city_plan/")
async def create_city(city: CityPlan):
    tile_object = create_tile_manager_object(city)
    analize_tm(tile_object)


    # create_tile_manager_object(city)
    # cd = city.__dict__
    # logit.debug('city plan endpoint hit')
    # logit.debug(f"type of city plan {type(city)}")
    # # logit.debug(f"city plan layout {city.__dict__}")
    # logit.debug(f"city plan layout {cd}")
    # logit.debug(f"city plan keys {cd.keys()}")
    # logit.debug(f"city plan name {city.name}")
    # logit.debug(f"city plan center {city.center}")
    # for item in city.center:
    #     logit.debug(f"center item {item}")
    #     if item.terrain is not None:
    #         logit.debug(f"center terrain item {item.terrain}")
    # logit.debug('\n\n')
    # logit.debug('listing out center tiles')
    # for index, tl in enumerate(city.center):
    #     logit.debug(f"{index} : {tl}")


    # tile_object = create_tile_manager_object()
    # analize_tm(tile_object)
    # logit.info('break between two managers')
    # tile_object = create_tile_manager_object('placeholder')
    # analize_tm(tile_object)
    # logit.debug(f"Tile object {tile_object}")
    # logit.debug(f"Tile object dict {tile_object.__dict__}")
    
        
    # logit.debug(f"Tile object dict {tile_object.__dict__.keys()}")


    # return str(type(city))
    return str(city)








# class Backend:

#     def __init__(self):
#         pass



# # be = Backend()

# class CityPlan(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# app = FastAPI()  # noqa

# @app.get('/')
# def heartbeat(request: Request):
#     return "thump thump..."

# @app.post('/items')
# async def create_item(item: CityPlan):
#     return item

# @app.post('/city_plan')
# def post_city_plan(
#     request: Request,
    
# ):

# tm = tile_manager.TileManager(
#     erah=8,
#     # cc=[
#     #     'grassland',
#     #     'floodplains',
#     #     'farm',
#     #     # 'grassland',
#     # ],
#     cc=[
#         'plains',
#         'rainforest',
#         'plantation',
#         # 'aluminum',
#         # 'river',
#         'city_center'
#         # 'floodplains',
#         # 'campus:1'
#         # 'campus'
#         # 'theater_square'
#         # 'farm'
#         # 'desert',
#         # 'campus',
#         # 'river'
#     ],
#     i0=[
#         'grasslandh',
#         'floodplains',
#         'farm'
#     ],
#     i1=[
#         'grassland',
#         'floodplains',
#         # 'farm'
#         'plantation'
#     ]
# )

# # for item, val in tm.cc.terrain.__dict__.items():
# #     print(f"    {item} : {val}")

# print(tm.cc.__dict__)
# print(tm.cc.terrain)
# print(tm.cc.feature)
# print(tm.cc.river)
# print(tm.cc.resource)
# print(tm.cc.improvement)
# print(tm.cc.district)
# print('')
# print(f"food: {tm.cc.food}")
# print(f"production: {tm.cc.production}")
# print(f"gold: {tm.cc.gold}")
# print(f"science: {tm.cc.science}")
# # print('\n\ndict keys here')
# # print(tm.cc.__dict__.keys())
# # print('')
# # print(tm.cc.terrain.__dict__.keys())
# # print('')
# # print(tm.cc.improvement.__dict__.keys())
# # print('\n\n')
# tm.calculate_city_yield()
# # tm.calculate_tile_yield()
# # print(tm.cc.district.__dict__)
# print(f"food: {tm.cc.food}")
# print(f"production: {tm.cc.production}")
# print(f"gold: {tm.cc.gold}")
# print(f"science: {tm.cc.science}")
