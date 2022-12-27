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
    
    # depth 8
    Cube(['W', 'W', 'W', 'B', 'G', 'G', 'R', 'R','Y', 'B', 'O', 'Y', 'G', 'O', 'G', 'W', 'R', 'Y', 'Y', 'R', 'B', 'B', 'O','O'])
    # Solution: Ut, Ft, Ut, F, Ut, Rp 
    
    # depth 9
    #Cube(['B', 'R', 'G', 'G', 'Y', 'R', 'W', 'O','Y', 'B', 'O', 'W', 'O', 'R', 'Y', 'O', 'B', 'G', 'W', 'B', 'G','Y','R', 'W',])
    # Solution: Rp, Ut, Rp, Fp, Rt, Fp, U, Ft, Rt
]
for x, cube in enumerate(cubes):
    print(f'Solving depth {x + 3}')
    solver.solve(cube)