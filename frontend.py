import datetime
import json
import yaml
import os

from fastapi import FastAPI, Request, Form, Query
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import PlainTextResponse, RedirectResponse
from typing import Optional, List

import backend

appname = 'civ_vi_frontend'

# Logging
import logger
logger = logger.Logger(appname, app_name_in_file=True, log_suffix='startup')
logit = logger.return_logit()
default_log_file = logger.log_file

class Frontend:

    def __init__(self):
        self.master_config = 'etc/frontend.yml'
        with open(self.master_config) as ycf:
            self.config = yaml.load(ycf, Loader=yaml.FullLoader)
        self.name = appname
        self.state = self.config['starting_state']
        logit.info(f"Frontend spun up: {self.state}")

        # Setup
        if os.environ.get('ENVIRONMENT') == 'prod':
            environment = 'prod'
        elif os.environ.get('ENVIRONMENT') == 'dev':
            environment = 'dev'
        elif os.environ.get('ENVIRONMENT') == 'test':
            environment = 'test'
        else:
            raise TypeError('The environment is not recognized. App closing')

        logger.update_file_level(self.config['environments'][environment]['file_handler_level'])
        logger.update_consol_level(self.config['environments'][environment]['consol_handler_level'])
        self.environment = environment
        self.testing = self.config['environments'][environment]['testing_flag']
        self.working_directory = self.config['environments'][environment]['docker_working_dir']

        self.state['env'] = environment
        self.state['testing'] = self.config['environments'][environment]['testing_flag']
        self.state['fh_logging'] = self.config['environments'][environment]['file_handler_level']
        self.state['ch_logging'] = self.config['environments'][environment]['consol_handler_level']
        self.state['log_file'] = logger.update_file(
            self.name,
            app_name_in_file=True,
            log_suffix=self.config['environments'][environment]['log_parameters']['log_suffix']
        )
        # self.state['log_file'] = logger.update_file(self.name, app_name_in_file=True, log_suffix=None)
        self.state['working_directory'] = self.config['environments'][environment]['docker_working_dir']

        logit.info(f"Starting in {environment}")
        logit.info(f"logging levels set to fh:{self.state['fh_logging']} ch:{self.state['ch_logging']} testing:{self.testing}")
        logit.debug(f'State: {self.state}')

app = FastAPI()
FE = Frontend()
BE = backend.Backend()
templates = Jinja2Templates(directory="templates/")
app.mount("/static", StaticFiles(directory="static"), name="static")
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root(request: Request):
    logit.debug(f"home endpoint hit")
    return templates.TemplateResponse("home.html", {"request": request})

@app.get('/state')
def state(request: Request):
    logit.debug(f"state endpoint hit")
    state_list = []
    for k,v in FE.state.items():
        state_list.append(str({k,v}))
    return templates.TemplateResponse("home.html", {"request": request, 'list':state_list})











