import Solver_3b as solver
from Cube import Cube

cubes = [
    # depth 3
    Cube(['W', 'Y', 'O', 'G', 'B', 'Y', 'G', 'R', 'W', 'O', 'R', 'W', 'O', 'B', 'Y', 'G', 'B', 'R', 'Y', 'W', 'G', 'O', 'R', 'B']),
    # depth 4
    Cube(['W', 'Y', 'O', 'G', 'B', 'Y', 'G', 'R', 'W', 'O', 'Y', 'G', 'O', 'G', 'R', 'W', 'W', 'Y', 'R', 'B', 'B', 'O', 'R', 'B']),
    # depth 5
    Cube(['W', 'Y', 'Y', 'W', 'B', 'R', 'G', 'O', 'G', 'O', 'Y', 'W', 'R', 'G', 'Y', 'W', 'G', 'O', 'R', 'B', 'B', 'O', 'R', 'B']),
    # depth 6
    Cube(['G', 'Y', 'R', 'W', 'R', 'W', 'G', 'O', 'G', 'O', 'B', 'Y', 'R', 'G', 'Y', 'W', 'B', 'O', 'R', 'B', 'W', 'O', 'Y', 'B'])
]
for x, cube in enumerate(cubes):
    print(f'Solving depth {x + 3}')
    solver.solve(cube)
