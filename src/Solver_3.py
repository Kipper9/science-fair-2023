import time
import collections
import pickle
from Cube import Cube
solvedCubes = {}

def load():
    global solvedCubes
    print('Importing')
    start_time = time.perf_counter()
    with open('cubeDepth.pkl','rb') as f:
        solvedCubes = pickle.load(f)
    endTime = time.perf_counter()
    print('Finished import')
    print (f'Time: {endTime - start_time: 0.3f}s')

def parentSwap(cubeA, cubeB):
    nextMove = cubeB.move
    parent = cubeA
    cube = cubeB.parent
    while cube:
        newCube = Cube(cube.cubies, parent, nextMove or parent.move)
        nextMove = cube.reverse()
        parent = newCube
        cube = cube.parent
    return parent

def solve(cube):
    cube.reset()
    visitedCubes = {}
    queue = collections.deque([(0, cube)])
    while queue:
        depth, currentCube = queue.popleft()
        # checks if the cube is found in the presolved file
        if currentCube in solvedCubes:
            return parentSwap(currentCube, solvedCubes[currentCube])
        # loops over each of the moves
        moves = [currentCube.d(), currentCube.dp(), currentCube.dt(), 
        currentCube.l(), currentCube.lp(), currentCube.lt(), 
        currentCube.b(), currentCube.bt(),currentCube.bp()]
        for newcube in moves:
            if not newcube in visitedCubes:
                queue.append((depth + 1, newcube))
            if not depth in visitedCubes:
                visitedCubes[depth] = set()
        visitedCubes[depth].add(currentCube)