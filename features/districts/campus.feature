

Feature: Testing Campus

# test the different string passing 
# campus
# campus:0
# campus:library
# campus:1
# campus:university
# campus:2
# campus:research_lab
# all the highest tier of buildings with
# :False
# :false
# :FALSE
# :0
# :True
# :true
# :TRUE
# :1
# :anything

@district
Scenario: Basic Setup
Verifying basic setup of a Campus works

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

@district
Scenario: Adjacent Mountains
Testing a ring of mountains around the Campus for yields

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland | cc |
        | forrest   | cc |
        | campus    | cc |
        | grassland | i0 |
        | mountain  | i0 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 24      |
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland | i1 |
        | mountain  | i1 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 25      |
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland | i2 |
        | mountain  | i2 |
        | grassland | i3 |
        | mountain  | i3 |
        | grassland | i4 |
        | mountain  | i4 |
        | grassland | i5 |
        | mountain  | i5 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 29      |

@district
Scenario: Adjacent Mountains
Testing a ring of mountains around the Campus for yields

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland          | cc |
        | campus             | cc |
        | coast              | i0 |
        | reef               | i0 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 25      |
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | tundra                  | i1 |
        | geothermal_fissure      | i1 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 27      |
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | coast              | i2 |
        | reef               | i2 |
        | tundra             | i3 |
        | geothermal_fissure | i3 |
        | coast              | i4 |
        | reef               | i4 |
        | tundra             | i5 |
        | geothermal_fissure | i5 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 35      |

@district
Scenario: Adjacent Mountains
Testing a ring of mountains around the Campus for yields

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland  | cc |
        | campus     | cc |
        | plains     | i0 |
        | rainforest | i0 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 23      |
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | plains     | i1 |
        | rainforest | i1 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 24      |
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | plains     | i2 |
        | rainforest | i2 |
        | plains     | i3 |
        | rainforest | i3 |
        | plains     | i4 |
        | rainforest | i4 |
        | plains     | i5 |
        | rainforest | i5 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 26      |
