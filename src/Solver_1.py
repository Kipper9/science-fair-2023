import time
def solve(cube):
    start_time = time.perf_counter()
    visitedCubes = set()
    queue = [cube]

    while queue:
        currentCube = queue.pop(0)

        # checks if the cube is solved
        if currentCube.isSolved():
            endTime = time.perf_counter()
            print('Solved!') 
            currentCube.render()
            print (f'It took: {endTime - start_time: 0.4f}')
            break

        # loop over each of the moves
        moves = [currentCube.u(), currentCube.up(), currentCube.ut(), currentCube.d(), currentCube.dp(), currentCube.dt(), currentCube.r(), currentCube.rp(), currentCube.rt(), currentCube.l(), currentCube.lp(), currentCube.lt(), currentCube.f(), currentCube.fp(), currentCube.ft(), currentCube.b(), currentCube.bp(), currentCube.bt()]
        for newcube in moves:
            if not newcube in visitedCubes:
                queue.append(newcube)
            visitedCubes.add(currentCube)        