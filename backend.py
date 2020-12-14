import datetime
import yaml
import os


from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from typing import Optional, List  # noqa

# from pymongo import MongoClient
# from pprint import pprint

# client = MongoClient(<<0.0.0.0:8305>>)

class Backend:

    def __init__(self):
        pass

app = FastAPI()

be = Backend()
