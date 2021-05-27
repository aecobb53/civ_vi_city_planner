

Feature: Testing Feature Rainforest

@feature
Scenario: Rainforest on a Plains tile
verifying basic setup of a rainforest on plains

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | plains        | cc        |
        | rainforest    | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element    | value   |
        | food       | 2       |
        | production | 1       |
        | gold       | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object        |
        | terrain       | plains        |
        | hills         | none          |
        | river         | none          |
        | district      | none          |
        | feature       | rainforest    |
        | resource      | none          |
        | improvement   | none          |

@feature
Scenario: Rainforest on an Ocean tile
verifying Rainforest does not go on an Ocean tile

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | ocean         | cc        |
        | rainforest    | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element    | value   |
        | food       | 1       |
        | production | 0       |
        | gold       | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | ocean     |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |

@feature
Scenario: I try to add hills and a river
Verify I am able to add hills and river tiles

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | plains        | cc        |
        | rainforest    | cc        |
        | hills         | cc        |
        | river         | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element       | value   |
        | food          | 2       |
        | production    | 2       |
        | gold          | 0       |
    Then I verify the tiles elements match the expected objects
        | element       | object        |
        | terrain       | plains        |
        | hills         | hills         |
        | river         | river         |
        | district      | none          |
        | feature       | rainforest    |
        | resource      | none          |
        | improvement   | none          |
