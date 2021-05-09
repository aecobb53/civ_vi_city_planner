

Feature: Testing Terrain Tundra

@terrain
Scenario: Basic Setup
Verifying basic setup of a Tundra tile works

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | tundra        | cc        |
        | woods         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 1       |
        | production    | 1       |
        | gold          | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | tundra    |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | woods     |
        | resource      | none      |
        | improvement   | none      |

@terrain
Scenario: I try to add hills and a river
Verify I am able to add hills and a river

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | tundra        | cc        |
        | hills         | cc        |
        | river         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 1       |
        | production    | 1       |
        | gold          | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | tundra    |
        | hills         | hills     |
        | river         | river     |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |


# # @terrain
# # Scenario: Provides fresh water to nearby tiles
# # Verifying I can provide a fresh water housing bonus to adjacent tiles

# # @terrain
# # Scenario: Provides appeal to adjacent tiles
# # Verifying I can provide a 1 appeal to adjacent tiles
