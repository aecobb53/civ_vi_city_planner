

Feature: Testing Terrain Desert

@terrain
Scenario: Basic Setup
Verifying basic setup of a Desert tile works

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | desert         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 0       |
        | production    | 0       |
        | gold          | 0       |

@terrain
Scenario: I try to add hills
Verify I am able to add hills and river

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | desert        | cc        |
        | hills         | cc        |
        | river         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 0       |
        | production    | 0       |
        | gold          | 0       |
