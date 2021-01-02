from behave import given, when, then

from backend.tile_manager import TileManager
# from backend.districts.campus import Campus

# Logging
import steps_logging_handler
logit, logger = steps_logging_handler.setup()

@given('I set up a new tile check')
def init_tile_manager(context):
    context.cc_list = []
    context.i1_list = []
    context.i2_list = []
    context.i3_list = []
    context.i4_list = []
    context.i5_list = []
    context.i6_list = []
    context.erah = 8

@when('I add element tile_addition to tile_name')
def add_element(context):
    for row in context.table:
        tile = row['tile_name'] + '_list'
        getattr(context, tile).append(row['tile_addition'])

@when('I calculate the yields')
def calculate_tile(context):
    context.tm = TileManager(
        erah=context.erah,
        cc=context.cc_list,
        i1=context.i1_list,
        i2=context.i2_list,
        i3=context.i3_list,
        i4=context.i4_list,
        i5=context.i5_list,
        i6=context.i6_list,
    )
    context.tm.calculate_city_yield()

@then('I verify the tiles elements match the expected value')
def element_validation(context):
    for row in context.table:
        # logit.debug(f'Comparing {getattr(context.tm.cc, row['element'])} to {row['value']}')
        value = int(row['value'])
        if not getattr(context.tm.cc, row['element']) == value:
            raise ValueError(f"Element {row['element']} is {getattr(context.tm.cc, row['element'])} not {value}")


@then('I verify the tiles {element} is {value}')
def element_validation(context, element, value):
    logit.debug(f'Comparing {getattr(context.tm.cc, element)} to {value}')
    value = int(value)
    if not getattr(context.tm.cc, element) == value:
        raise ValueError(f"Element {element} is {getattr(context.tm.cc, element)} not {value}")
