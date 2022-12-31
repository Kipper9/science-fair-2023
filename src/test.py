import pickle
from Cube import Cube
with open('cubeDepth.pkl','rb') as f:
    cubes = pickle.load(f)

cube = Cube(['W', 'W', 'W', 'W', 'O', 'O', 'G', 'G', 'R', 'R', 'R', 'R', 'B', 'B', 'O', 'O', 'Y', 'Y', 'Y', 'Y', 'G', 'G', 'B', 'B'])

if cube in cubes:
    print('it worked. The depth was: ', cubes[cube])

else:
    print(':(')

# for cube, depth in cubes.items():
#     cube.render()
#     print("('__________________________________________________________________________________________________________________________________')")