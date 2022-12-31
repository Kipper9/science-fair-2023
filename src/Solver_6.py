import time
import collections
import pickle

def solve(cube):
    start_time = time.perf_counter()
    visitedCubes = {}
    queue = collections.deque([(0, cube)])
    
    with open('cubeDepth8.pkl','rb') as f:
        cubes = pickle.load(f)
    
    while queue:
        depth, currentCube = queue.popleft()

        if cube in cubes:
            depthlimit = cubes[cube]

        # checks if the cube is solved
        if currentCube.isSolved():
            endTime = time.perf_counter()
            print('Solved!') 
            currentCube.render()
            print (f'It took: {endTime - start_time: 0.3f}')
            break
        # makes sure the code doesn't go past the max depth
        if depth == depthlimit:
            continue

        # loop over each of the moves
        moves = [currentCube.u(), currentCube.up(), currentCube.ut(), currentCube.r(), currentCube.rp(), currentCube.rt(), currentCube.f(), currentCube.fp(), currentCube.ft()]
        for newcube in moves:
            if newcube in visitedCubes:
                queue.appendleft((depth + 1, newcube))
            if not depth in visitedCubes:
                visitedCubes[depth] = set()
        visitedCubes[depth].add(currentCube)