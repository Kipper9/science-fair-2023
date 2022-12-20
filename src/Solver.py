def solve(cube):
    visitedCubes = set()
    queue = [cube]

    while queue:
        currentCube = queue.pop(0)

        if currentCube.isSolved():
            print('Solved!') 
            currentCube.render()
            break

        # loop over each of the moves
        moves = [currentCube.u(), currentCube.r()]
        for newcube in moves:
            if not newcube in visitedCubes:
                queue.append(newcube)
            visitedCubes.add(currentCube)        