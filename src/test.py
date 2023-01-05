import pickle
from Cube import Cube
with open('cubeDepth7b.pkl','rb') as f:
    cubes = pickle.load(f)

cube = Cube(['R', 'R', 'W', 'W', 'W', 'O', 'G', 'G', 'R', 'Y', 'R', 'Y', 'B', 'B', 'W', 'O', 'O', 'O', 'Y', 'Y', 'G', 'G', 'B', 'B'])

if cube in cubes:
    solvedCube, depth = cubes[cube]
    print('It worked. The depth was: ',depth, 'The cube is:')
    solvedCube.render()
else:
    print(':(')

# for cube, depth in cubes.items():
#     cube.render()
#     print(cubes[cube])
#     print("('__________________________________________________________________________________________________________________________________')")