

Feature: Testing Campus

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
        | grassland     | cc |
        | forrest       | cc |
        | campus        | cc |
        | grassland     | i0 |
        | mountain      | i0 |
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

@district @DEBUG
Scenario: Adjacent Features
Testing a ring of different features around the Campus for yields

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition     | tile_name |
        | grassland         | cc |
        | campus            | cc |
        | coast             | i0 |
        | reef              | i0 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 25      |
    When I add element tile_addition to tile_name
        | tile_addition         | tile_name |
        | tundra                | i1 |
        | geothermal_fissure    | i1 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 27      |
    When I add element tile_addition to tile_name
        | tile_addition         | tile_name |
        | coast                 | i2 |
        | reef                  | i2 |
        | tundra                | i3 |
        | geothermal_fissure    | i3 |
        | coast                 | i4 |
        | reef                  | i4 |
        | tundra                | i5 |
        | geothermal_fissure    | i5 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 35      |

@district
Scenario: Adjacent Rainforest
Testing a ring of rainforest around the Campus for yields

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc |
        | campus        | cc |
        | plains        | i0 |
        | rainforest    | i0 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 23      |
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | plains        | i1 |
        | rainforest    | i1 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 24      |
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | plains        | i2 |
        | rainforest    | i2 |
        | plains        | i3 |
        | rainforest    | i3 |
        | plains        | i4 |
        | rainforest    | i4 |
        | plains        | i5 |
        | rainforest    | i5 |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 26      |

# test the different string passing 
@district @district_string_parsing
Scenario: String interpretation campus:0
Validating string creation interpretation

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc |
        | campus:0      | cc |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 4       |

@district @district_string_parsing
Scenario: String interpretation campus:library
Validating string creation interpretation

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition     | tile_name |
        | grassland         | cc |
        | campus:library    | cc |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 4       |

@district @district_string_parsing
Scenario: String interpretation campus:1
Validating string creation interpretation

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc |
        | campus:1      | cc |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 10      |

@district @district_string_parsing
Scenario: String interpretation campus:university
Validating string creation interpretation

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition         | tile_name |
        | grassland             | cc       |
        | campus:university     | cc |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 10      |

@district @district_string_parsing
Scenario: String interpretation campus:2 unpowered
Validating string creation interpretation

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc |
        | campus:2      | cc |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 18      |

@district @district_string_parsing
Scenario: String interpretation campus:2 powered
Validating string creation interpretation

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc |
        | campus:2:T    | cc |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 23      |

@district @district_string_parsing
Scenario: String interpretation campus:research_lab unpowered
Validating string creation interpretation

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition         | tile_name |
        | grassland             | cc |
        | campus:research_lab   | cc |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 18      |

@district @district_string_parsing
Scenario: String interpretation campus:research_lab powered
Validating string creation interpretation

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition         | tile_name |
        | grassland             | cc |
        | campus:research_lab:T | cc |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 23      |


@district @district_string_parsing
Scenario: String interpretation campus:2:false unpowered
Validating string creation interpretation

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition     | tile_name |
        | grassland         | cc |
        | campus:2:false    | cc |
    When I calculate the yields
    Then I verify the tiles elements match the expected value
        | element | value   |
        | science | 18      |
