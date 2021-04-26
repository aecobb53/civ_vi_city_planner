# Overview of the backend flow

## TOC:
- (Common Tile)[#common-tile]
- (Tile Container)[#tile-container]
- (Tile Manager)[#tile-manager]

## Common Tile

Common tile is the default behavior of every tile element. 
It is used as a base class to return expected values if none are already set. 
For example yields default to 0 if no yield has been added. 

## Tile Container

The Tile Container is used to manage an individual tile. 
Much like the common tile, the container has default values if they are not updated. 
The container will be smart enought to build a tile from the ground up. 
This means taking a list of provided tile elements and validating they can be stacked then stacking them if it passes. 
For example you cant add a forrest to an ocean tile but you can add ice. 
Every tile in the game will be made up of one container full of all the individual element classes. 

Order of layers:
`Terrain` > ~~`Natural Wonders`~~ > ~~`Wonders`~~ > `Districts` > `Feature` >  `Resources` > `Improvements`

> Wonders are not MVP1

## Tile Manager

Tile Manager handles the city as a whole. 
It returns default behavior for all tiles unless updated. 
It will take in input and pass the list of tiles to the container for each tile. 
It generates yields and corrilates adjacency bonuses. 
One manager will be used for every itteration of an optimization check. 

## Data flow

City plan will be created as an object that is an array of objects. 
These sub objects represent each tile and contain arays of elements for the tile. 
The manager will create a container for each tile passed and populate the container with elements. 
The container will sanity check the input and retain what is acceptable. 
When the yields are generated, the manager will reference the container to calculate the yields of the city as a whole. 
