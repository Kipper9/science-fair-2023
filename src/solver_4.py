import collections
import time
def solve(cube):
    start_time = time.perf_counter()
    visitedCubes = {}
    queue = collections.deque([(0, cube)])

    while queue:
        depth, currentCube = queue.popleft()

        # checks if the cube is solved
        if currentCube.isSolved():
            endTime = time.perf_counter()
            print('Solved!') 
            currentCube.render()
            print (f'It took: {endTime - start_time: 0.3f}')
            break

        # loop over each of the moves
        moves = [currentCube.u(), currentCube.up(), currentCube.ut(), currentCube.r(), currentCube.rp(), currentCube.rt(), currentCube.f(), currentCube.ft(), currentCube.fp()]
        for newcube in moves:
            if not newcube in visitedCubes.get(depth, set()) or not newcube in visitedCubes.get(depth - 1, set()) or not newcube in visitedCubes.get(depth - 2, set()):
                queue.append((depth + 1, newcube))
            
            if not depth in visitedCubes:
                visitedCubes[depth] = set()
            visitedCubes[depth].add(currentCube)