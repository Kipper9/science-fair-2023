# science-fair-2023
This is a grade 8 science fair project trying to optimaly solve a 2x2 rubik's cube.

The code keeps track of the cube through an array of the colored cube tiles and has the moves hard coded in the cube class. The current solver uses a brute forced file of the depths of the cubes up to depth 8, with  that information it does a look up of the depth of the current cube's depth and sets the depth limit of the depth first search to that number. As we get closer to the solved state we limit the search even more until the cube is solved.
