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


# class Terrain(BaseModel):
#     name: str
#     hill: bool = None


# class Feature(BaseModel):
#     name: str
#     river: bool = None


# class Resource(BaseModel):
#     name: str


# class Imporovement(BaseModel):
#     name: str


# class District(BaseModel):
#     name: str
#     powered: bool = True
#     buildings: List(str) = []


# class Wonder(BaseModel):
#     name: str


# class Tile(BaseModel):
#     terrain: Optional[Terrain] = None
#     feature: Optional[Feature] = None
#     resource: Optional[Resource] = None
#     imporovement: Optional[Imporovement] = None
#     district: Optional[District] = None
#     wonder: Optional[Wonder] = None


class Item(BaseModel):
    # name: str = None
    # center: str = None
    # inner: str = None
    # middle: str = None
    # outer: str = None
    # nearby: str = None
    # name: str = ''
    # center: List[Tile]
    # inner: List[Tile]
    # middle: List[Tile]
    # outer: List[Tile]
    # nearby: List[Tile]

    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get('/')
def heartbeat(request: Request):
    return "thump thump..."


@app.post("/items/")
async def create_item(item: Item):
    return item








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
