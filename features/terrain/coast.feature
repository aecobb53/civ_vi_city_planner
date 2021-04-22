

Feature: Testing Terrain Coast

@terrain
Scenario: Basic Setup
Verifying basic setup of a Coast tile works

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | coast         | cc        |
        | ice           | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | food    | 1       |
        | gold    | 1       |

# @terrain
# Scenario: Provides fresh water to nearby tiles
# Verifying I can provide a fresh water housing bonus to adjacent tiles

# @terrain
# Scenario: Provides appeal to adjacent tiles
# Verifying I can provide a 1 appeal to adjacent tiles

@terrain
Scenario Outline: Can support expected resources
I verify every resources is or is not able to be added to the tile

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | coast         | cc        |
    Then I try to add a resource and it passes

    Examples: All resources
    | resource  | passes    |
    # | aluminum  | false     |
    # | amber     | false     |
    # | bananas   | false     |
    # | cattle    | false     |
    # | cinnamon  | false     |
    # | citrus    | false     |
    # | cloves    | false     |
    # | coal      | false     |
    # | cocoa     | false     |
    # | coffee    | false     |
    # | copper    | false     |
    # | cosmetics | false     |
    # | cotton    | false     |
    | crabs     | false     |
    # | deer      | false     |
    # | diamonds  | false     |
    # | dyes      | false     |
    # | fish      | false     |
    # | furs      | false     |
    # | gold_ore  | false     |
    # | gypsum    | false     |
    # | honey     | false     |
    # | horses    | false     |
    # | insense   | false     |
    # | iron      | false     |
    # | ivory     | false     |
    # | jade      | false     |
    # | jeans     | false     |
    # | maize     | false     |
    # | marble    | false     |
    # | murcury   | false     |
    # | niter     | false     |
    # | oil       | false     |
    # | olives    | false     |
    # | pearls    | false     |
    # | perfume   | false     |
    # | rice      | false     |
    # | salt      | false     |
    # | sheep     | false     |
    # | silk      | false     |
    # | silver    | false     |
    # | spices    | false     |
    # | stone     | false     |
    # | sugar     | false     |
    # | tea       | false     |
    # | tobacco   | false     |
    # | toys      | false     |
    # | truffles  | false     |
    # | turtles   | false     |
    # | uranium   | false     |
    # | whales    | false     |
    # | wheat     | false     |
    # | wine      | false     |

# Scenario: Adjacent Mountains
# Testing a ring of mountains around the Campus for yields

#     Given I set up a new tile check
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | grassland | cc |
#         | forrest   | cc |
#         | campus    | cc |
#         | grassland | i0 |
#         | mountain  | i0 |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element | value   |
#         | science | 24      |
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | grassland | i1 |
#         | mountain  | i1 |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element | value   |
#         | science | 25      |
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | grassland | i2 |
#         | mountain  | i2 |
#         | grassland | i3 |
#         | mountain  | i3 |
#         | grassland | i4 |
#         | mountain  | i4 |
#         | grassland | i5 |
#         | mountain  | i5 |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element | value   |
#         | science | 29      |

# @district
# Scenario: Adjacent Mountains
# Testing a ring of mountains around the Campus for yields

#     Given I set up a new tile check
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | grassland          | cc |
#         | campus             | cc |
#         | coast              | i0 |
#         | reef               | i0 |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element | value   |
#         | science | 25      |
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | tundra                  | i1 |
#         | geothermal_fissure      | i1 |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element | value   |
#         | science | 27      |
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | coast              | i2 |
#         | reef               | i2 |
#         | tundra             | i3 |
#         | geothermal_fissure | i3 |
#         | coast              | i4 |
#         | reef               | i4 |
#         | tundra             | i5 |
#         | geothermal_fissure | i5 |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element | value   |
#         | science | 35      |

# @district
# Scenario: Adjacent Mountains
# Testing a ring of mountains around the Campus for yields

#     Given I set up a new tile check
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | grassland  | cc |
#         | campus     | cc |
#         | plains     | i0 |
#         | rainforest | i0 |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element | value   |
#         | science | 23      |
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | plains     | i1 |
#         | rainforest | i1 |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element | value   |
#         | science | 24      |
#     When I add element tile_addition to tile_name
#         | tile_addition | tile_name |
#         | plains     | i2 |
#         | rainforest | i2 |
#         | plains     | i3 |
#         | rainforest | i3 |
#         | plains     | i4 |
#         | rainforest | i4 |
#         | plains     | i5 |
#         | rainforest | i5 |
#     When I calculate the yields
#     Then I verify the tiles elements match the expected value
#         | element | value   |
#         | science | 26      |
