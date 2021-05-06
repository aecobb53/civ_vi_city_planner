

Feature: Testing Tile Container

@container
Scenario: Tile with Grassland, hills, river, campus
Verifying a tile can be set up with no exceptions

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc        |
        | hills         | cc        |
        | river         | cc        |
        | campus        | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | none      |
        | river         | river     |
        | district      | campus    |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |

@container
Scenario: Tile with Grassland, hills, river, campus, farm
Verifying a tile with a farm is overwritten with a campus and a farm cant be created on a campus

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc        |
        | hills         | cc        |
        | river         | cc        |
        | farm          | cc        |
        | campus        | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | none      |
        | river         | river     |
        | district      | campus    |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |

    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | farm          | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | none      |
        | river         | river     |
        | district      | campus    |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |

@container
Scenario: Tile with Grassland, hills, river, farm, fort
Verifying a tile with a farm is overwritten with a fort

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc        |
        | hills         | cc        |
        | river         | cc        |
        | farm          | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | hills     |
        | river         | river     |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | farm      |

    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | fort          | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | hills     |
        | river         | river     |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | fort      |

@container
Scenario: Tile with Grassland, hills, mine
Verifying a tile with hills can have a mine and without wont

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc        |
        | mine          | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |

    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc        |
        | hills         | cc        |
        | mine          | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | hills     |
        | river         | none      |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | mine      |

@container @DEBUG
Scenario: Tile with Coast, fish, fishing boat
Verifying a water tile can't support a fishing boat without a resource

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | coast         | cc        |
        | fishing_boats | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | coast     |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |

    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | coast         | cc        |
        | fish          | cc        |
        | fishing_boats | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object        |
        | terrain       | coast         |
        | hills         | none          |
        | river         | none          |
        | district      | none          |
        | feature       | none          |
        | resource      | fish          |
        | improvement   | fishing_boats |

@container
Scenario: Tile with Grassland, hills, fishing boat
Verifying a land tile can't support a sea improvement and vice versa

    Given I set up a new tile check
    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | grassland     | cc        |
        | fishing_boat  | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | grassland |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |

    When I add element tile_addition to tile_name
        | tile_addition | tile_name |
        | coast         | cc        |
        | farm          | cc        |
    When I calculate the yields
    Then I verify the tiles elements match the expected objects
        | element       | object    |
        | terrain       | coast     |
        | hills         | none      |
        | river         | none      |
        | district      | none      |
        | feature       | none      |
        | resource      | none      |
        | improvement   | none      |

# switching terrain
# conflicting feature
# conflicting resource with terrain and feature
# having/missing river?
# resource removed from district
# feature removed if improvement removes it?
# resource removed if improvement removes it (wheat is removed with fort)
#     strategic never removed and restricts improvements
#     bonus removed if conflicting improvements
#     luxury is like strategic??
