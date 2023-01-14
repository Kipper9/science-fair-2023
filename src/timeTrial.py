import Solver_7 as solver
from Cube import Cube

cubes = [
    # depth 2
    Cube(['R', 'R', 'W', 'W', 'W', 'O', 'G', 'G', 'R', 'Y', 'R', 'Y', 'B', 'B', 'W', 'O', 'O', 'O', 'Y', 'Y', 'G', 'G', 'B', 'B']),
    # Solution: Ut, Fp
    
    # depth 3
    Cube(['W', 'Y', 'O', 'G', 'B', 'Y', 'G', 'R', 'W', 'O', 'R', 'W', 'O', 'B', 'Y', 'G', 'B', 'R', 'Y', 'W', 'G', 'O', 'R', 'B']),
    # Solution: F, Rt, Up
    
    # depth 4
    Cube(['W', 'Y', 'O', 'G', 'B', 'Y', 'G', 'R', 'W', 'O', 'Y', 'G', 'O', 'G', 'R', 'W', 'W', 'Y', 'R', 'B', 'B', 'O', 'R', 'B']),
    # Solution: Ut, F, Ut, Rp
    
    # depth 5
    Cube(['W', 'Y', 'Y', 'W', 'B', 'R', 'G', 'O', 'G', 'O', 'Y', 'W', 'R', 'G', 'Y', 'W', 'G', 'O', 'R', 'B', 'B', 'O', 'R', 'B']),
    # Solution: Ft, Ut, F, Ut, Rp
    
    # depth 9
    Cube(['B', 'R', 'G', 'G', 'Y', 'R', 'W', 'O', 'Y', 'B', 'O', 'W', 'O', 'R', 'Y', 'O', 'B', 'G', 'W', 'B', 'G', 'Y', 'R', 'W']),
    # Solution: Rp, Ut, Rp, Fp, Rt, Fp, U, Ft, Rt

    # depth 10
    Cube(['G', 'B', 'B', 'R', 'Y', 'Y', 'O', 'Y', 'B', 'O', 'W', 'W', 'B', 'R', 'Y', 'W', 'R', 'G', 'R', 'O', 'G', 'G', 'O', 'W']),
    
    # depth 11
    Cube(['W', 'W', 'W', 'W', 'B', 'G', 'R', 'O', 'G', 'B', 'R', 'R', 'B', 'B', 'O', 'O', 'Y', 'Y', 'Y', 'Y', 'G', 'G', 'R', 'O'])
]
solver.load()
print('')

for x, cube in enumerate(cubes):
    solver.solve(cube)
    print("")