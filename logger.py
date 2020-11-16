import logging
import datetime
import os
from logging.handlers import RotatingFileHandler



class Borg:

    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state



class Logger(Borg):

    def __init__(self, app_name, **kwargs):
        Borg.__init__(self)
        # Easy way to keep track of what is currently set or not. 
        self.state = {
            'f_level':None,
            'c_level':None,
            'log_rolling':None,
            'log_directory':None,
            'log_prefix':None,
            'log_suffix':None,

            'app_name_in_file':None,
            'date_in_file':None,
            'time_in_file':None,
            'utc_in_file':None,
            'short_datetime':None
        }

        # Update teh state form the kwargs
        self.set_state(kwargs)

        # creating the logging object
        self.logger = logging.getLogger(app_name)
        self.logger.setLevel(logging.DEBUG)

        # Create a filename from self.state
        self.log_file = self.set_file(app_name)

        # Creating handlers file and consol
        self.fh = logging.FileHandler(self.log_file)
        self.ch = logging.StreamHandler()


        """
        Setting handler levels.
        The default is file:DEBUG commandline:INFO
        """
        if self.state['f_level'] == None:
            self._update_file_level('DEBUG')
            self.state['f_level'] = 'DEBUG'
        else:
            self._update_file_level(self.state['f_level'])

        # Set time to use
        if self.state['c_level'] == None:
            self._update_consol_level('INFO')
            self.state['c_level'] = 'INFO'
        else:
            self._update_consol_level(self.state['c_level'])

        

        # create formatter and add it to the handlers
        # Move into if statement based on kwargs?
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s - %(message)s', '%Y-%m-%dT%H:%M:%SZ')


        # create sublogger stuff


        # Log rotating
        # Move into if statement based on kwargs
        #fh = logging.handlers.TimedRotatingFileHandler('logs/testlog.log', when='midnight',interval=1,backupCount=30)

        
        # Adds the formatter to the logging object
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)


        # Add the handlers to the logging object
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def set_state(self, kwargs):
        """
        Set items from kwargs. 
        If you need to un-set somethign set it equal to None
        """
        for k,v in kwargs.items():
            """set to values"""
            if k == 'f_level':
                self.state['f_level'] = v

            if k == 'c_level':
                self.state['c_level'] = v

            if k == 'log_rolling':
                self.state['log_rolling'] = v

            if k == 'log_directory':
                self.state['log_directory'] = v

            if k == 'log_prefix':
                self.state['log_prefix'] = v

            if k == 'log_suffix':
                self.state['log_suffix'] = v
                
            """set to bool"""

            if k == 'app_name_in_file':
                if v:
                    self.state['app_name_in_file'] = True
                else:
                    self.state['app_name_in_file'] = False

            if k == 'date_in_file':
                if v:
                    self.state['date_in_file'] = True
                else:
                    self.state['date_in_file'] = False

            if k == 'time_in_file':
                if v:
                    self.state['time_in_file'] = True
                else:
                    self.state['time_in_file'] = False

            if k == 'utc_in_file':
                if v:
                    self.state['utc_in_file'] = True
                else:
                    self.state['utc_in_file'] = False

            if k == 'short_datetime':
                if v:
                    self.state['short_datetime'] = True
                else:
                    self.state['short_datetime'] = False
        return self.state

    def set_file(self, app_name):
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
        if self.state['log_directory'] == None:
            file_name.append('logs/')
        else:
            if self.state['log_directory'][-1] != '/':
                self.state['log_directory'] += '/'
            file_name.append(self.state['log_directory'])

        if self.state['app_name_in_file']:
            file_name.append(app_name)

        if self.state['log_prefix'] != None:
            file_name.append(self.state['log_prefix'])

        if self.state['utc_in_file']:
            now = datetime.datetime.now(tz=datetime.timezone.utc)
            time_ext = 'Z'
        else:
            now = datetime.datetime.now()
            time_ext = 'L'

        if self.state['date_in_file'] and self.state['time_in_file']:
            if self.state['short_datetime']:
                datetime_string = datetime.datetime.strftime(now, '%y%m%d-%H%M%S' + time_ext)
            else:
                datetime_string = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S.%f' + time_ext)
            file_name.append(datetime_string)
        elif self.state['date_in_file'] and not self.state['time_in_file']:
            if self.state['short_datetime']:
                datetime_string = datetime.datetime.strftime(now, '%y%m%d' + time_ext)
            else:
                datetime_string = datetime.datetime.strftime(now, '%Y-%m-%d' + time_ext)
            file_name.append(datetime_string)
        elif not self.state['date_in_file'] and self.state['time_in_file']:
            if self.state['short_datetime']:
                datetime_string = datetime.datetime.strftime(now, '%d-%H%M%S' + time_ext)
            else:
                datetime_string = datetime.datetime.strftime(now, '%dT%H:%M:%S.%f' + time_ext)
            file_name.append(datetime_string)

        if self.state['log_suffix'] != None:
            file_name.append(self.state['log_suffix'])

        file_name.append('.log')

        if len(file_name) == 2:
            file_name.insert(1,'log')

        if len(file_name) == 3:
            file_name = ''.join(file_name)
        else:
            file_name = file_name[0] + '_'.join(file_name[1:-1]) + file_name[-1]
        return file_name

    def update_file(self, app_name, **kwargs):
        self.logger.removeHandler(self.fh)
        self.set_state(kwargs)
        self.log_file = self.set_file(app_name)
        self.fh = logging.FileHandler(self.log_file)
        self.logger.addHandler(self.fh)
        # print(log_file)
        return self.log_file



    def return_logit(self):
        """
        Return the logger object so it can be set to something like logit in the script. 
        Having logging, logger, and logit are confusing but allow a lot of flexability. 
        """
        return self.logger

    def _update_file_level(self, new_level):
        """
        Log levels for log file:
        debug, info, warning, error, critical
        """
        if new_level.upper() in ['DEBUG']:
            self.fh.setLevel(logging.DEBUG)
            self.state['f_level'] = 'DEBUG'

        elif new_level.upper() in ['INFO']:
            self.fh.setLevel(logging.INFO)
            self.state['f_level'] = 'INFO'

        elif new_level.upper() in ['WARN', 'WARNING']:
            self.fh.setLevel(logging.WARNING)
            self.state['f_level'] = 'WARNING'

        elif new_level.upper() in ['ERROR']:
            self.fh.setLevel(logging.ERROR)
            self.state['f_level'] = 'ERROR'

        elif new_level.upper() in ['CRITICAL']:
            self.fh.setLevel(logging.CRITICAL)
            self.state['f_level'] = 'CRITICAL'

    def _update_consol_level(self, new_level):
        """
        Log levels for command line:
        debug, info, warning, error, critical
        """
        if new_level.upper() in ['DEBUG']:
            self.ch.setLevel(logging.DEBUG)
            self.state['c_level'] = 'DEBUG'

        elif new_level.upper() in ['INFO']:
            self.ch.setLevel(logging.INFO)
            self.state['c_level'] = 'INFO'

        elif new_level.upper() in ['WARN', 'WARNING']:
            self.ch.setLevel(logging.WARNING)
            self.state['c_level'] = 'WARNING'

        elif new_level.upper() in ['ERROR']:
            self.ch.setLevel(logging.ERROR)
            self.state['c_level'] = 'ERROR'

        elif new_level.upper() in ['CRITICAL']:
            self.ch.setLevel(logging.CRITICAL)
            self.state['c_level'] = 'CRITICAL'

    def update_file_level(self, new_level):
        self._update_file_level(new_level)
        self.logger.addHandler(self.fh)

    def update_consol_level(self, new_level):
        self._update_consol_level(new_level)
        self.logger.addHandler(self.ch)




# logger = Logger('the_tester',\
#     app_name_in_file=True,\
#     # date_in_file=True,\
#     # time_in_file=True,\
#     log_prefix='dev',\
#     log_suffix='behave',\
#     log_directory='testlogs/')
# logit = logger.return_logit()
# logit.info('duplicate logging in both')
# logger._update_file_level('DEBUG')
# logit.info('duplicate logging in cmdline1')
# logger.update_file('the_tester',log_suffix='testwo')
# logit.info('duplicate logging in cmdline2')
