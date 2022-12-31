import time
import collections
def solve(cube):
    depthlimit = 5
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
        # makes sure the code doesn't go past the max depth
        if depth == depthlimit:
            continue

        # loop over each of the moves
        moves = [currentCube.u(), currentCube.up(), currentCube.ut(), currentCube.r(), currentCube.rp(), currentCube.rt(), currentCube.f(), currentCube.fp(), currentCube.ft()]
        for newcube in moves:
            if newcube in visitedCubes.get(depth, set()) or not newcube in visitedCubes.get(depth - 1, set()) or not newcube in visitedCubes.get(depth + 1, set()):
                queue.appendleft((depth + 1, newcube))
            if not depth in visitedCubes:
                visitedCubes[depth] = set()
        visitedCubes[depth].add(currentCube)