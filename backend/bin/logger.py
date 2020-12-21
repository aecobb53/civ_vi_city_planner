import logging
import datetime

from logging.handlers import RotatingFileHandler
from logging import FileHandler, StreamHandler


class Logger:

    def __init__(self, app_name, **kwargs):
        # Easy way to keep track of what is currently set or not.
        self.appname = app_name
        self.f_level = None
        self.c_level = None
        self.log_directory = None
        self.log_prefix = None
        self.log_suffix = None
        self.app_name_in_file = None
        self.date_in_file = None
        self.time_in_file = None
        self.utc_in_file = None
        self.short_datetime = None
        self.maxBytes = None
        self.backupCount = None
        self.when = None
        self.interval = None
        self.utc = None
        self.create_fh = None
        self.create_ch = None
        self.create_sh = None
        self.create_th = None

        # Update the state form the kwargs
        self._set_state(kwargs)

        # creating the logging object
        self.logger = logging.getLogger(self.appname)
        self.logger.setLevel(logging.DEBUG)  # Im not sure why but this needs to be set

        # Create a filename from self.state
        self._set_file()

        # Creating handlers file and consol
        self._set_handlers()

        # Setting handler levels.
        self._update_file_level(self.f_level)
        self._update_consol_level(self.c_level)

        # create formatter and add it to the handlers
        # Move into if statement based on kwargs?
        self.formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(module)s %(funcName)s - %(message)s', '%Y-%m-%dT%H:%M:%SZ')

        # Adds the formatter to the logging object
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)

        # Add the handlers to the logging object
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

        # create sublogger stuff

    def _set_state(self, kwargs):
        """
        Set items from kwargs.
        If you need to un-set somethign set it equal to None
        """
        for key, value in kwargs.items():
            if key == 'appname':
                self.appname = value

            if key == 'f_level':
                self.f_level = value

            if key == 'c_level':
                self.c_level = value

            if key == 'log_directory':
                self.log_directory = value

            if key == 'log_prefix':
                self.log_prefix = value

            if key == 'log_suffix':
                self.log_suffix = value

            if key == 'app_name_in_file':
                self.app_name_in_file = value

            if key == 'date_in_file':
                self.date_in_file = value

            if key == 'time_in_file':
                self.time_in_file = value

            if key == 'utc_in_file':
                self.utc_in_file = value

            if key == 'short_datetime':
                self.short_datetime = value

            if key == 'maxBytes':
                self.maxBytes = value

            if key == 'backupCount':
                self.backupCount = value

            if key == 'when':
                self.when = value

            if key == 'interval':
                self.interval = value

            if key == 'utc':
                self.utc = value

            if key == 'maxBytes':
                self.maxBytes = value

            if key == 'backupCoun':
                self.backupCoun = value

            if key == 'when':
                self.when = value

            if key == 'interval':
                self.interval = value

            if key == 'rotating_utc':
                self.rotating_utc = value

            if key == 'create_fh':
                self.create_fh = value

            if key == 'create_ch':
                self.create_ch = value

            if key == 'create_sh':
                self.create_sh = value

            if key == 'create_th':
                self.create_th = value

    def _set_file(self):
        """
        File name
        You can set:
        a new directory, 'logs/' is default
        the app name to be in the log
        a prefix after the app name
        the date
        the time
        short date or time
        utc or local time
        a suffix after the time
        it will end with '.log'
        """
        file_name = []
        if self.log_directory is None:
            file_name.append('logs/')
        else:
            if self.log_directory[-1] != '/':
                self.log_directory += '/'
            file_name.append(self.log_directory)

        if self.app_name_in_file:
            file_name.append(self.appname)

        if self.log_prefix is not None:
            file_name.append(self.log_prefix)

        if self.utc_in_file:
            now = datetime.datetime.now(tz=datetime.timezone.utc)
            time_ext = 'Z'
        else:
            now = datetime.datetime.now()
            time_ext = 'L'

        if self.date_in_file and self.time_in_file:
            if self.short_datetime:
                datetime_string = datetime.datetime.strftime(now, '%y%m%d-%H%M%S' + time_ext)
            else:
                datetime_string = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S.%f' + time_ext)
            file_name.append(datetime_string)
        elif self.date_in_file and not self.time_in_file:
            if self.short_datetime:
                datetime_string = datetime.datetime.strftime(now, '%y%m%d' + time_ext)
            else:
                datetime_string = datetime.datetime.strftime(now, '%Y-%m-%d' + time_ext)
            file_name.append(datetime_string)
        elif not self.date_in_file and self.time_in_file:
            if self.short_datetime:
                datetime_string = datetime.datetime.strftime(now, '%d-%H%M%S' + time_ext)
            else:
                datetime_string = datetime.datetime.strftime(now, '%dT%H:%M:%S.%f' + time_ext)
            file_name.append(datetime_string)

        if self.log_suffix is not None:
            file_name.append(self.log_suffix)

        file_name.append('.log')

        if len(file_name) == 2:
            file_name.insert(1, 'log')

        if len(file_name) == 3:
            file_name = ''.join(file_name)
        else:
            file_name = file_name[0] + '_'.join(file_name[1:-1]) + file_name[-1]
        self.file_name = file_name

    def _set_handlers(self):
        if self.create_fh is None and \
            self.create_ch is None and \
            self.create_sh is None and \
            self.create_th is None:
            
            self.create_fh = True
            self.create_ch = True

        if self.create_fh:
            self._add_fh()

        if self.create_ch:
            self._add_ch()

        if self.create_sh:
            self._add_sh()

        if self.create_th:
            self._add_th()

    def _add_fh(self):
        self.fh = logging.FileHandler(self.file_name)
        return self.fh

    def _add_ch(self):
        self.ch = logging.StreamHandler()
        return self.ch

    def _add_sh(self):
        self.fh = logging.handlers.RotatingFileHandler(
            self.file_name,
            maxBytes=self.maxBytes,
            backupCount=self.backupCount)
        return self.fh

    def _add_th(self):
        self.fh = logging.handlers.TimedRotatingFileHandler(
            self.file_name,
            when=self.when,
            interval=self.interval,
            backupCount=self.backupCount,
            utc=self.utc)
        return self.fh

    def _update_file_level(self, new_level=None):
        """
        Log levels for log file:
        debug, info, warning, error, critical
        """
        self.f_level = new_level
        if self.f_level is None:
            self.f_level = 'DEBUG'

        if self.f_level.upper() in ['DEBUG']:
            self.fh.setLevel(logging.DEBUG)

        elif self.f_level.upper() in ['INFO']:
            self.fh.setLevel(logging.INFO)

        elif self.f_level.upper() in ['WARN', 'WARNING']:
            self.fh.setLevel(logging.WARNING)

        elif self.f_level.upper() in ['ERROR']:
            self.fh.setLevel(logging.ERROR)

        elif self.f_level.upper() in ['CRITICAL']:
            self.fh.setLevel(logging.CRITICAL)

    def _update_consol_level(self, new_level=None):
        """
        Log levels for command line:
        debug, info, warning, error, critical
        """
        self.c_level = new_level
        if self.c_level is None:
            self.c_level = 'DEBUG'

        if self.c_level.upper() in ['DEBUG']:
            self.ch.setLevel(logging.DEBUG)

        elif self.c_level.upper() in ['INFO']:
            self.ch.setLevel(logging.INFO)

        elif self.c_level.upper() in ['WARN', 'WARNING']:
            self.ch.setLevel(logging.WARNING)

        elif self.c_level.upper() in ['ERROR']:
            self.ch.setLevel(logging.ERROR)

        elif self.c_level.upper() in ['CRITICAL']:
            self.ch.setLevel(logging.CRITICAL)

    def return_logit(self):
        """
        Return the logger object so it can be set to something like logit in the script.
        Having logging, logger, and logit are confusing but allow a lot of flexability.
        """
        return self.logger

    def update_file(self, app_name, **kwargs):
        self.logger.removeHandler(self.fh)
        self._set_state(kwargs)
        self._set_file()
        self._set_handlers()
        self._update_file_level(self.f_level)
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

    def append_file_handler(self, app_name, **kwargs):
        # Havnt tested this very well yet
        self._set_state(kwargs)
        self._set_file()
        self._set_handlers()
        self._update_file_level(self.f_level)
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

    def update_file_level(self, new_level):
        self._update_file_level(new_level)
        self.logger.addHandler(self.fh)

    def update_consol_level(self, new_level):
        self._update_consol_level(new_level)
        self.logger.addHandler(self.ch)
