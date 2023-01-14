import Solver_2 as solver
import time
from Cube import Cube

cubes = [
    # depth 2
    Cube(['R', 'R', 'W', 'W', 'W', 'O', 'G', 'G', 'R', 'Y', 'R', 'Y', 'B', 'B', 'W', 'O', 'O', 'O', 'Y', 'Y', 'G', 'G', 'B', 'B']),
    
    # depth 3
    Cube(['W', 'Y', 'O', 'G', 'B', 'Y', 'G', 'R', 'W', 'O', 'R', 'W', 'O', 'B', 'Y', 'G', 'B', 'R', 'Y', 'W', 'G', 'O', 'R', 'B']),
    
    # depth 4
    Cube(['W', 'Y', 'O', 'G', 'B', 'Y', 'G', 'R', 'W', 'O', 'Y', 'G', 'O', 'G', 'R', 'W', 'W', 'Y', 'R', 'B', 'B', 'O', 'R', 'B']),
    
    # depth 5
    Cube(['W', 'Y', 'Y', 'W', 'B', 'R', 'G', 'O', 'G', 'O', 'Y', 'W', 'R', 'G', 'Y', 'W', 'G', 'O', 'R', 'B', 'B', 'O', 'R', 'B']),
    
    # depth 7
    Cube(['R', 'B', 'G', 'W', 'B', 'O', 'Y', 'B', 'O', 'Y', 'R', 'W', 'R', 'W', 'G', 'R', 'G', 'O', 'Y', 'B', 'G', 'W', 'Y', 'O']),

    # depth 9
    Cube(['B', 'R', 'G', 'G', 'Y', 'R', 'W', 'O', 'Y', 'B', 'O', 'W', 'O', 'R', 'Y', 'O', 'B', 'G', 'W', 'B', 'G', 'Y', 'R', 'W']),

    # depth 10
    Cube(['G', 'B', 'B', 'R', 'Y', 'Y', 'O', 'Y', 'B', 'O', 'W', 'W', 'B', 'R', 'Y', 'W', 'R', 'G', 'R', 'O', 'G', 'G', 'O', 'W']),
    
    # depth 11
    Cube(['W', 'W', 'W', 'W', 'B', 'G', 'R', 'O', 'G', 'B', 'R', 'R', 'B', 'B', 'O', 'O', 'Y', 'Y', 'Y', 'Y', 'G', 'G', 'R', 'O'])
]
solver.load()
print('')

for x, cube in enumerate(cubes):
    print('Solving:    ', end='')
    cube.render()
    start_time = time.perf_counter()
    solution = solver.solve(cube)
    endTime = time.perf_counter()
    print('Solution: ', solution.moves()," (", solution.moves().count(" ") - 1, " moves)", sep = '')
    print (f'Time:      {endTime - start_time: 0.9f}s')
    print('')