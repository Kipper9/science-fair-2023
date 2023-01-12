import collections
import pickle
from Cube import Cube
# depth -> set { cubes }
# cube -> depth
visitedCubes = {}
queue = collections.deque([(0, Cube())])
depth = 0
maxDepth = 0
while depth < 6 and queue:
  depth, currentCube = queue.popleft()
  if currentCube in visitedCubes:
    continue
  if (depth > maxDepth):
    print('New depth:',maxDepth)
    maxDepth = depth

    # loop over each of the moves
  moves = [currentCube.u(), currentCube.up(), currentCube.ut(), currentCube.r(), currentCube.rp(), currentCube.rt(), currentCube.f(), currentCube.ft(), currentCube.fp(),
  currentCube.d(), currentCube.dp(), currentCube.dt(), currentCube.l(), currentCube.lp(), currentCube.lt(), currentCube.b(), currentCube.bt(), currentCube.bp()]
  for newcube in moves:
    if newcube not in visitedCubes:
      queue.append((depth + 1, newcube))
  visitedCubes[currentCube] = currentCube
print('Solved!')
print('')
print('Pickling')
with open('cubeDepth.pkl','wb') as j:
    pickle.dump(visitedCubes,j)
print('Done')