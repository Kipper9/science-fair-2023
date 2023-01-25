from Cube import Cube
from vpython import *
from time import *
import Solver_7 as solver
cube = Cube()

floor = box(pos = vector(0,-5,0), color = color.yellow, size = vector(10,.1,10))
ceiling = box(pos = vector(0,5,0), color = color.white, size = vector(10,.1,10))
backWall = box(pos = vector(0,0,-5), color = color.green, size = vector(10,10,.1))
leftWall = box(pos = vector(-5,0,0), color = color.red, size = vector(.1,10,10))
rightWall = box(pos = vector(5,0,0), color = color.orange, size = vector(.1,10,10))
frontWall = box(pos = vector(0,0,5), color = color.blue, size = vector(10,10,.1))
cubie1 = compound([floor, ceiling, backWall, leftWall, rightWall, frontWall], pos = vector(5.05,5.05,5.05))
cubie2 = cubie1.clone(pos = vector(-5.05,5.05,5.05))
cubie3 = cubie1.clone(pos = vector(5.05,-5.05,5.05))
cubie4 = cubie1.clone(pos = vector(-5.05,-5.05,5.05))
cubie5 = cubie1.clone(pos = vector(-5.05,5.05,-5.05))
cubie6 = cubie1.clone(pos = vector(5.05,-5.05,-5.05))
cubie7 = cubie1.clone(pos = vector(-5.05,-5.05,-5.05))
cubie8 = cubie1.clone(pos = vector(5.05,5.05,-5.05))
cube2 = [cubie1, cubie2, cubie3, cubie4, cubie5, cubie6, cubie7, cubie8]

moves = {
    'R': { "cubes": [0, 2, 7, 5], "rotation": -1, "vector": (1, 0, 0), "swaps": [2,5,0,7]},
    "R'": { "cubes": [0, 2, 7, 5], "rotation": 1, "vector": (1, 0, 0), "swaps": [7,0,5,2]},
    'R2': { "cubes": [0, 2, 7, 5], "rotation": 2, "vector": (1, 0, 0), "swaps": [5,7,2,0]},
    'F': { "cubes": [0, 1, 2, 3], "rotation": -1, "vector": (0, 0, 1), "swaps": [1,3,0,2]},
    "F'": { "cubes": [0, 1, 2, 3], "rotation": 1, "vector": (0, 0, 1), "swaps": [2,0,3,1]},
    'F2': { "cubes": [0, 1, 2, 3], "rotation": 2, "vector": (0, 0, 1), "swaps": [3,2,1,0]},
    'U': { "cubes": [0, 1, 7, 4], "rotation": -1, "vector": (0, 1, 0), "swaps": [7,0,4,1]},
    "U'": { "cubes": [0, 1, 7, 4], "rotation": 1, "vector": (0, 1, 0), "swaps": [1,4,0,7]},
    'U2': { "cubes": [0, 1, 7, 4], "rotation": 2, "vector": (0, 1, 0), "swaps": [4,7,1,0]},
    'B': { "cubes": [4, 7, 5, 6], "rotation": 1, "vector": (0, 0, 1), "swaps": [7,5,6,4]},
    "B'": { "cubes": [4, 7, 5, 6], "rotation": -1, "vector": (0, 0, 1), "swaps": [6,4,7,5]},
    'B2': { "cubes": [4, 7, 5, 6], "rotation": 2, "vector": (0, 0, 1), "swaps": [5,6,4,7]},
    'L': { "cubes": [4, 1, 3, 6], "rotation": 1, "vector": (1, 0, 0), "swaps": [6,4,1,3]},
    "L'": { "cubes": [4, 1, 3, 6], "rotation": -1, "vector": (1, 0, 0), "swaps": [1,3,6,4]},
    'L2': { "cubes": [4, 1, 3, 6], "rotation": 2, "vector": (1, 0, 0), "swaps": [3,6,4,1]},
    'D': { "cubes": [3, 2, 6, 5], "rotation": 1, "vector": (0, 1, 0), "swaps": [6,3,5,2]},
    "D'": { "cubes": [3, 2, 6, 5], "rotation": -1, "vector": (0, 1, 0), "swaps": [2,5,3,6]},
    'D2': { "cubes": [3, 2, 6, 5], "rotation": 2, "vector": (0, 1, 0), "swaps": [5,6,2,3]}
}

def move (move):
    moveinfo = moves[move]
    for i in range(0,90):
        for j in moveinfo["cubes"]:
            cube2[j].rotate(angle = radians(moveinfo['rotation']), axis = vector(*moveinfo["vector"]), origin = vector(0,0,0))
        sleep(0.003)
    cube2[moveinfo["cubes"][0]], cube2[moveinfo["cubes"][1]] ,cube2[moveinfo["cubes"][2]], cube2[moveinfo["cubes"][3]] = cube2[moveinfo["swaps"][0]], cube2[moveinfo["swaps"][1]], cube2[moveinfo["swaps"][2]], cube2[moveinfo["swaps"][3]]

solver.load()

def solutionActivate(moves):
    for m in moves.split():
        move(m)
        sleep(0.8)

while True:
    turn = str(input('What function: '))

    if turn == 'f':
        cube = cube.f()
        move('F')
    
    elif turn == 'fp':
        cube = cube.fp()
        move("F'")
    
    elif turn == 'ft':
        cube = cube.ft()
        move('F2')
    
    elif turn == 'b':
        cube = cube.b()
        move('B')

    elif turn == 'bp':
        cube.bp()
        move("B'")
    
    elif turn == 'bt':
        cube = cube.bt()
        move('B2')

    elif turn == 'u':
        cube = cube.u()
        move('U')
    
    elif turn == 'up':
        cube = cube.up()
        move("U'")
   
    elif turn == 'ut':
        cube = cube.ut()
        move('U2')
    
    elif turn == 'd':
        cube = cube.d()
        move('D')
    
    elif turn == 'dp':
        cube = cube.dp()
        move("D'")
    
    elif turn == 'dt':
        cube = cube.dt()
        move('D2')

    elif turn == 'r':
        cube = cube.r()
        move('R')
    
    elif turn == 'rp':
        cube = cube.rp()
        move("R'")
    
    elif turn == 'rt':
        cube = cube.rt()
        move('R2')

    elif turn == 'l':
        cube = cube.l()
        move('L')
    
    elif turn == 'lp':
        cube = cube.lp()
        move("L'")
    
    elif turn == 'lt':
        cube = cube.lt()
        move('L2')

    elif turn == 'exit':
        break
    
    elif turn == 'solve':
        cube.reset()
        solution = solver.solve(cube)
        print('Solution:', solution.moves())
        solutionActivate(solution.moves())
        solution.reset()
        cube = solution
        
    else:
        print('Error: move', turn ,'is not indexed')

    print ("The cube's state is:")
    cube.render()

    if cube.isSolved():
        print('The cube is solved!')