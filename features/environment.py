import os

# Logging
from steps import steps_logging
logit, logger = steps_logging.setup()


# sql_database = 'db/weatherman_behave.sql'
# csv_database = 'db/weatherman_behave.csv'

# new_log_dir = 'logs/behave'
# old_log_dir = 'logs/behave/old'



# def database_cleanup():
#     """
#     Delete the testing databases
#     """
#     try:
#         os.remove(sql_database)
#     except:
#         pass
#     try:
#         os.remove(csv_database)
#     except:
#         pass

# def move_logging():
#     """
#     Move all log files to the old directory except the one created for the testing
#     """
#     for log in os.listdir(new_log_dir)[:-1]:
#         if os.path.isfile(os.path.join(new_log_dir, log)):
#             os.rename(os.path.join(new_log_dir, log),os.path.join(old_log_dir, log))

def startup():
    print('starting up')

def before_all(context):
    print('Setting up environment')
    database_cleanup()
    move_logging()

def after_all(context):
    print('Cleaning up environment')
    database_cleanup()
    
# def before_feature(context, feature):
#     print('before')

# def after_feature(context, feature):
#     print('after')

def before_scenario(context, scenario):
    # print(scenario)
    if 'DEBUG' in scenario.tags:
        logger.update_consol_level('DEBUG')
    if 'INFO' in scenario.tags:
        logger.update_consol_level('INFO')
    if 'WARNING' in scenario.tags:
        logger.update_consol_level('WARNING')
    if 'database' in scenario.tags:
        database_cleanup()
    if 'owma' in scenario.tags:
        pass
    if 'on' in scenario.tags:
        context.run = True
    if 'off' in scenario.tags:
        context.run = False

def after_scenario(context, scenario):
    logger.update_consol_level('WARNING')
    pass