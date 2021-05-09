

Feature: Testing Terrain Lake

@terrain
Scenario: Basic Setup
Verifying basic setup of a Lake tile works

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | lake          | cc        |
        | ice           | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 1       |
        | production    | 0       |
        | gold          | 1       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | lake      |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | ice       |
        | resource      | none      |
        | improvement   | none      |

@terrain
Scenario: I try to add hills
Verify I am unable to add hills

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | lake          | cc        |
        | hills         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 1       |
        | production    | 0       |
        | gold          | 1       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | lake      |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |

@terrain
Scenario: I try to add a river
Verify I am unable to add a river

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | lake          | cc        |
        | river         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 1       |
        | production    | 0       |
        | gold          | 1       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | lake      |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |

# @terrain
# Scenario: Provides fresh water to nearby tiles
# Verifying I can provide a fresh water housing bonus to adjacent tiles

# @terrain
# Scenario: Provides appeal to adjacent tiles
# Verifying I can provide a 1 appeal to adjacent tiles
