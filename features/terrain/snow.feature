

Feature: Testing Terrain Snow

@terrain
Scenario: Basic Setup
Verifying basic setup of a Snow tile works

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition         | tile_name |
        | snow                  | cc        |
        | geothermal_fissure    | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 0       |
        | production    | 0       |
        | gold          | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object                |
        | terrain       | snow                  |
        | hills         | none                  |
        | river         | none                  |
        | district      | none                  |
        | feature       | geothermal_fissure    |
        | resource      | none                  |
        | improvement   | none                  |

@terrain
Scenario: I try to add hills and a river
Verify I am unable to add hills and a river

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | snow          | cc        |
        | hills         | cc        |
        | river         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 0       |
        | production    | 1       |
        | gold          | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | snow      |
        | hills         | hills     |
        | river         | river     |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |
