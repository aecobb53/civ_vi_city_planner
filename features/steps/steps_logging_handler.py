from backend.bin.logger import Logger

# logging_mod = logger

def setup():
    # Logging
    logger = Logger('civ_vi', \
        log_directory='logs/backend/behave/', \
        app_name_in_file=True, \
        log_prefix='functional_testing', \
        date_in_file=True, \
        time_in_file=True, \
        utc_in_file=True, \
        f_level='DEBUG', \
        c_level='WARNING')
    logit = logger.return_logit()
    default_log_file = logger.file_name
    return logit, logger
