import solver_4 as solver
from Cube import Cube

cubes = [
    # depth 3
    Cube(['W', 'Y', 'O', 'G', 'B', 'Y', 'G', 'R', 'W', 'O', 'R', 'W', 'O', 'B', 'Y', 'G', 'B', 'R', 'Y', 'W', 'G', 'O', 'R', 'B']),
    # Solution: F, Rt, Up
    # depth 4
    Cube(['W', 'Y', 'O', 'G', 'B', 'Y', 'G', 'R', 'W', 'O', 'Y', 'G', 'O', 'G', 'R', 'W', 'W', 'Y', 'R', 'B', 'B', 'O', 'R', 'B']),
    # Solution: Ut, F, Ut, Rp
    # depth 5
    Cube(['W', 'Y', 'Y', 'W', 'B', 'R', 'G', 'O', 'G', 'O', 'Y', 'W', 'R', 'G', 'Y', 'W', 'G', 'O', 'R', 'B', 'B', 'O', 'R', 'B']),
    # Solution: Ft, Ut, F, Ut, Rp
    # depth 6
    Cube(['W', 'Y', 'Y', 'W', 'G', 'O', 'B', 'R', 'B', 'R', 'Y', 'W', 'R', 'G', 'Y', 'W', 'G', 'O', 'R', 'B', 'B', 'O', 'O', 'G'])
    # Solution: Rt, Ft, Ut, F, Ut, Rp 
]
for x, cube in enumerate(cubes):
    print(f'Solving depth {x + 3}')
    solver.solve(cube)