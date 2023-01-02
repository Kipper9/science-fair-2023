# science-fair-2023
This is a grade 8 science fair project trying to optimaly solve a 2x2 rubik's cube.

The code keeps track of the cube through an array of the colored cube tiles and has the moves, checking if it's solved, if it's equal to another cube and rendering of the cube hard coded in the cube class. The current solver has a brute forced file of all cubes with their respective depths kept track uf up to depth 8. Using that file it does a look up of the current cube's depth and sets the depth limit of the depth first search to that depth. As we get closer to the solved state we limit the search even more until the cube is solved. In the future I will try to make 3D rendering but for now I will focus on the math side of the problem.
