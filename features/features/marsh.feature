

Feature: Testing Feature Marsh

@feature
Scenario: Marsh on a Grassland tile
verifying basic setup of a Marsh tile on Grassland

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc        |
        | marsh         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element    | value   |
        | food       | 3       |
        | production | 0       |
        | gold       | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | marsh     |
        | resource      | none      |
        | improvement   | none      |

@feature @DEBUG
Scenario: Marsh on a Plains tile
verifying Marsh does not go on plains tiles

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | plains        | cc        |
        | marsh         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element    | value   |
        | food       | 2       |
        | production | 1       |
        | gold       | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | plains    |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | marsh     |
        | resource      | none      |
        | improvement   | none      |

# @feature
# Scenario: Woods on a Tundra tile
# verifying basic setup of a Woods tile on Tundra

#     Given I set up a new tile check
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | tundra        | cc        |
#         | woods         | cc        |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element    | value   |
#         | food       | 1       |
#         | production | 1       |
#         | gold       | 0       |
#     Then I verify the tiles elements match the expected objects
#         | element       | object    |
#         | terrain       | tundra    |
#         | hills         | none      |
#         | river         | none      |
#         | district      | none      |
#         | feature       | woods     |
#         | resource      | none      |
#         | improvement   | none      |

# @feature
# Scenario: Woods on a Ocean tile
# verifying Woods are not added to a tile on Ocean

#     Given I set up a new tile check
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | ocean         | cc        |
#         | woods         | cc        |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element    | value   |
#         | food       | 1       |
#         | production | 0       |
#         | gold       | 0       |
#     Then I verify the tiles elements match the expected objects
#         | element       | object    |
#         | terrain       | ocean     |
#         | hills         | none      |
#         | river         | none      |
#         | district      | none      |
#         | feature       | none      |
#         | resource      | none      |
#         | improvement   | none      |

# @feature
# Scenario: I try to add hills and a river
# Verify I am able to add hills and river tiles

#     Given I set up a new tile check
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | grassland     | cc        |
#         | woods         | cc        |
#         | hills         | cc        |
#         | river         | cc        |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element       | value   |
#         | food          | 2       |
#         | production    | 2       |
#         | gold          | 0       |
#     Then I verify the tiles elements match the expected objects
#         | element       | object    |
#         | terrain       | grassland |
#         | hills         | hills     |
#         | river         | river     |
#         | district      | none      |
#         | feature       | woods     |
#         | resource      | none      |
#         | improvement   | none      |
