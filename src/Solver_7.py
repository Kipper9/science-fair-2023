import time
import collections
import pickle
from Cube import Cube
solvedCubes = {}

def load():
    global solvedCubes
    print('Importing')
    start_time = time.perf_counter()
    with open('cubeDepth7c.pkl','rb') as f:
        solvedCubes = pickle.load(f)
    
    endTime = time.perf_counter()
    print('Finished import')
    print (f'It took: {endTime - start_time: 0.3f}')

def parentSwap(cubeA, cubeB):
    cube = cubeB
    parent = cubeA
    while cube.parent:
        cube = cube.parent
        newCube = Cube(cube.cubies, parent, cube.reverse())
        parent = newCube
    
    return parent
        

def solve(cube):
    visitedCubes = {}
    queue = collections.deque([(0, cube)])
    maxDepth = 0
    
    
    start_time2 = time.perf_counter()
    while queue:
        depth, currentCube = queue.popleft()
        
        # checks if we have found a  new depth
        if depth > maxDepth:
            maxDepth = depth
            print('Searching depth: ',maxDepth)

        # checks if the cube is found in the presolved file
        if currentCube in solvedCubes:
            endTime2 = time.perf_counter()
            print('Solved, pickle') 
            currentCube.render()
            print('--')
            solvedCubes[currentCube].render()
            print('++++++++')
            parentSwap(currentCube, solvedCubes[currentCube]).render()
            print (f'It took: {endTime2 - start_time2: 0.3f}')
            break
        
        # loops over each of the moves
        moves = [currentCube.d(), currentCube.dp(), currentCube.dt(), currentCube.l(), currentCube.lp(), currentCube.lt(), currentCube.b(), currentCube.bt(), currentCube.bp()]
        for newcube in moves:
            if not newcube in visitedCubes.get(depth, set()) or not newcube in visitedCubes.get(depth - 1, set()) or not newcube in visitedCubes.get(depth + 1, set()):
                queue.append((depth + 1, newcube))
            if not depth in visitedCubes:
                visitedCubes[depth] = set()
        visitedCubes[depth].add(currentCube)