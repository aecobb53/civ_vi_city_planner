

Feature: Testing Campus

@district @DEBUG
Scenario Outline: Adjacent Mountains
Testing a ring of mountains around the Campus for yields

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland | cc |
        | forrest   | cc |
        | campus    | cc |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 23      |

