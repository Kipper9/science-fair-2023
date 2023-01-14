def load():
    pass
def solve(cube):
    visitedCubes = set()
    queue = [cube]
    while queue:
        currentCube = queue.pop(0)
        # checks if the cube is solved
        if currentCube.isSolved():
            return currentCube

        # loop over each of the moves
        moves = [currentCube.u(), currentCube.up(), currentCube.ut(), currentCube.r(), currentCube.rp(), currentCube.rt(), currentCube.f(), currentCube.fp(), currentCube.ft()]
        for newcube in moves:
            if not newcube in visitedCubes:
                queue.append(newcube)
        visitedCubes.add(currentCube)