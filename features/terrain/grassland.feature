

Feature: Testing Terrain Grassland

@terrain
Scenario: Basic Setup
Verifying basic setup of a Grassland tile works

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc        |
        | woods         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element    | value   |
        | food       | 2       |
        | production | 1       |
        | gold       | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | woods     |
        | resource      | none      |
        | improvement   | none      |

@terrain
Scenario: I try to add hills and a river
Verify I am able to add hills and river tiles

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc        |
        | hills         | cc        |
        | river         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 2       |
        | production    | 1       |
        | gold          | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | hills     |
        | river         | river     |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |
