

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

@terrain
Scenario: I try to add hills
Verify I am unable to add hills

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | coast         | cc        |
        | hills         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | food    | 1       |
        | production    | 0       |
        | gold    | 1       |


# @terrain
# Scenario: Provides fresh water to nearby tiles
# Verifying I can provide a fresh water housing bonus to adjacent tiles

# @terrain
# Scenario: Provides appeal to adjacent tiles
# Verifying I can provide a 1 appeal to adjacent tiles
