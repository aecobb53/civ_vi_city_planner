from behave import given, when, then

from backend.tile_manager import TileManager
# from backend.districts.campus import Campus

# Logging
import steps_logging_handler
logit, logger = steps_logging_handler.setup()

@given('I set up a new tile check')
def init_tile_manager(context):
    context.cc_list = []
    context.i0_list = []
    context.i1_list = []
    context.i2_list = []
    context.i3_list = []
    context.i4_list = []
    context.i5_list = []
    context.erah = 8

@when('I add element tile_addition to tile_name')
def add_element(context):
    for row in context.table:
        logit.debug(f"adding info to tile manager {row}")
        tile = row['tile_name'] + '_list'
        getattr(context, tile).append(row['tile_addition'])

@when('I calculate the yields')
def calculate_tile(context):
    context.tm = TileManager(
        erah=context.erah,
        cc=context.cc_list,
        i0=context.i0_list,
        i1=context.i1_list,
        i2=context.i2_list,
        i3=context.i3_list,
        i4=context.i4_list,
        i5=context.i5_list,
    )
    context.tm.calculate_city_yield()

@then('I verify the tiles elements match the expected value')
def element_validation(context):
    for row in context.table:
        try:
            value = int(row['value'])
        except ValueError:
            value = row['value']
        logit.debug(f"Comparing {row['element']}:{row['value']} to {getattr(context.tm.cc, row['element'])}")
        # logit.debug(f"{getattr(context.tm.cc, row['element'])}/{value} == {getattr(context.tm.cc, row['element']) == value}")
        # logit.warning(f"{context.tm.i0}")
        if not getattr(context.tm.cc, row['element']) == value:
            logit.error(f"Element {row['element']} is {getattr(context.tm.cc, row['element'])} not {value}")
            logit.info(f"cc: list:{context.cc_list}, T:{context.tm.cc.terrain}, F:{context.tm.cc.feature}")
            logit.info(f"i0: list:{context.i0_list}, T:{context.tm.i0.terrain}, F:{context.tm.i0.feature}")
            logit.info(f"i1: list:{context.i1_list}, T:{context.tm.i1.terrain}, F:{context.tm.i1.feature}")
            logit.info(f"i2: list:{context.i2_list}, T:{context.tm.i2.terrain}, F:{context.tm.i2.feature}")
            logit.info(f"i3: list:{context.i3_list}, T:{context.tm.i3.terrain}, F:{context.tm.i3.feature}")
            logit.info(f"i4: list:{context.i4_list}, T:{context.tm.i4.terrain}, F:{context.tm.i4.feature}")
            logit.info(f"i5: list:{context.i5_list}, T:{context.tm.i5.terrain}, F:{context.tm.i5.feature}")
            raise ValueError('values do not match')

@then('I try to add a resource and it passes')
def add_resource(context):
    # print(context)
    # print(context.active_outline)
    logit.error(f"{context.active_outline}")
    logit.error(f"{type(context.active_outline)}")
    logit.error(f"{context.active_outline[0]}")
    logit.error(f"{context.active_outline[1]}")
    context.cc_list.append(context.active_outline[0])

    context.tm = TileManager(
        erah=context.erah,
        cc=context.cc_list,
        i0=context.i0_list,
        i1=context.i1_list,
        i2=context.i2_list,
        i3=context.i3_list,
        i4=context.i4_list,
        i5=context.i5_list,
    )
    # context.tm.calculate_city_yield()

    # logit.error(f"{context.active_outline[2]}")
    # for row in context.active_outline:
    #     logit.error(f"{row}")
        # print(f"    {row['resource']} -- {row['passes']}")
        # logit.debug(f"adding info to tile manager {row}")
        # tile = row['tile_name'] + '_list'
        # getattr(context, tile).append(row['tile_addition'])

# @then('I verify the tiles {element} is {value}')
# def element_validation(context, element, value):
#     logit.debug(f'Comparing {getattr(context.tm.cc, element)} to {value}')
#     value = int(value)
#     if not getattr(context.tm.cc, element) == value:
#         raise ValueError(f"Element {element} is {getattr(context.tm.cc, element)} not {value}")
