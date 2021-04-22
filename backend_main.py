import datetime
# import time
import json
import os
import yaml
# import threading

from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse, Response
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
logger = Logger('civ_vi',
    log_directory='logs/backend/',
    app_name_in_file=True,
    log_suffix=log_prefix,
    log_prefix='main',
    date_in_file=False,
    time_in_file=False,
    utc_in_file=False,
    f_level='DEBUG',
    c_level=c_level)
logit = logger.return_logit()
# default_log_file = logger.file_name
# return logit, logger

# Config
with open('etc/backend.yml') as ycf:
    config = yaml.load(ycf, Loader=yaml.FullLoader)


class Terrain(BaseModel):
    name: str
    hills: bool = None


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


    # Proposed additions
    # erah
    # city_uuid
    # food
    # production
    # gold
    # science
    # culture
    # faith
    # population
    # housing
    # citizen_slot
    # amenities
    # power
    # maintenance


class CityId(BaseModel):
    name: str
    # logit.debug(f"center item here {center}")
    # logit.debug(f"center item here {self.center}")
    # logit.debug(f"center type {type(center)}")

    # if len(center) < 6:
    #     center.append(None)


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
                logit.warning(f"here is the tile were on {tile.__dict__.keys()}")
                for layer in tile_layers:
                    logit.warning(f"here is the layer were on {layer}")
                    try:
                        if getattr(tile, layer) is None:
                            continue
                    except:
                        continue
                    try:
                            logit.debug(f"layer details {tile_index}-{layer}: {getattr(tile, layer)}")
                            tile_list.append(getattr(tile, layer).name)
                    except AttributeError:
                        pass
                    if layer == 'terrain':
                        if getattr(tile, layer).hills:
                            tile_list.append('hills')
                    if layer == 'feature':
                        if getattr(tile, layer).river:
                            tile_list.append('river')
                city_dct[tile_index] = tile_list
                logit.debug(f"tile_list for {tile_index}: {tile_list}")
    for i,j in city_dct.items():
        logit.debug(f"city dict {i} : {j}")
    tm = tile_manager.TileManager(**city_dct)
    return tm

def create_city_plan_object_from_database(database_entry):
    print(json.dumps(database_entry, indent=2))
    print('create city plan from database dict')
    city_key = {
        'c': 'center',
        'i': 'inner',
        'm': 'middle',
        'o': 'outer',
        'n': 'nearby',
    }
    city_plan = {
        'center': [],
        'inner': [],
        'middle': [],
        'outer': [],
        'nearby': [],
    }

    for tile_index in config['tile_index_list']:
        if tile_index in database_entry:
            ring = city_key[tile_index[0]]
            entry = {}
            for layer in config['tile_layers']:
                try:
                    # print(database_entry[tile_index][layer])
                    temp_value = database_entry[tile_index][layer]
                    if layer == 'hills':
                        entry['terrain']['hills'] = True
                        continue
                    elif layer == 'river':
                        entry['feature']['river'] = True
                        continue
                    else:
                        value = {
                            'name': temp_value
                        }

                    entry[layer] = value
                except KeyError:
                    pass
            city_plan[city_key[tile_index[0]]].append(entry)
        else:
            city_plan[city_key[tile_index[0]]].append({})
    for metric in config['city_metrics']:
        try:
            city_plan[metric] = database_entry[metric]
        except KeyError:
            pass

    print('running through city plan')
    print(json.dumps(city_plan, indent=2))
    return CityPlan(**city_plan)

def analize_tm(tile_object):
    indent = '    '
    for tile_index in config['tile_index_list']:
        logit.debug(f"index: {tile_index}, {getattr(tile_object, tile_index)}")
        if getattr(tile_object, tile_index) is not None:
            for layer in config['tile_layers']:
                if getattr(getattr(tile_object, tile_index), layer) is not None:
                    logit.debug(f"{indent}layer: {layer}, {getattr(getattr(tile_object, tile_index), layer)}")

def analize_yields(tile_object):
    indent = '    '
    for tile_index in config['tile_index_list']:
        # logit.debug(f"index: {tile_index}, {getattr(tile_object, tile_index)}")
        if getattr(tile_object, tile_index) is not None:
            logit.debug(f"index: {tile_index}, {getattr(tile_object, tile_index)}")
            for res in config['tile_resources']:
                if getattr(getattr(tile_object, tile_index), res) is not None and getattr(getattr(tile_object, tile_index), res) != 0:
                    logit.debug(f"{indent}res: {res}, {getattr(getattr(tile_object, tile_index), res)}")


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
    logit.debug('city_plan post endpoint hit')
    tile_object = create_tile_manager_object(city)
    # analize_tm(tile_object)
    tile_object.calculate_city_yield()
    # analize_yields(tile_object)
    json_object = tile_object.converte_to_json()
    logit.debug(f"{json.dumps(json_object, indent=2)}")

    json_response = jsonable_encoder(CityId(name=json_object['city_uuid']))
    logit.debug(f"returned response: {json_response}")
    return JSONResponse(content=json_response)
    # If im supposed to return just the uuid, i have that coded out below
    # return json_object['city_uuid']

@app.get("/city_plan/")
async def return_city(cityId: CityId):
    logit.debug('city_plan get endpoint hit')
    logit.debug(f"cityID: {cityId.name}")
    logit.warning('actually grabbing a city based on its ID is turned off for testing')
    database_example_data = {
        "cc": {
            "terrain": "grassland",
            "hills": 'hills',
            "feature": "woods",
            "river": 'river',
            "district": "campus"
        },
        "i0": {
            "terrain": "grassland",
            "feature": "woods",
            "district": "campus"
        },
        "i1": {
            "terrain": "desert",
            "feature": "floodplains"
        },
        "i2": {
            "terrain": "plains",
            "feature": "rainforest"
        },
        "erah": 8,
        "city_uuid": cityId.name
    }
    city = create_city_plan_object_from_database(database_example_data)
    json_response = jsonable_encoder(city)
    return json_response
