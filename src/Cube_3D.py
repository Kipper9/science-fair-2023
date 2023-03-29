from Cube import Cube
from vpython import *
from time import *
import Solver_3 as solver

solver.load()
cube = Cube()

moves = {
    'R': { "cubes": [0, 2, 7, 5], "rotation": -1, "vector": (1, 0, 0), "swaps": [2,5,0,7], "func": "r" },
    "R'": { "cubes": [0, 2, 7, 5], "rotation": 1, "vector": (1, 0, 0), "swaps": [7,0,5,2], "func": "rp" },
    'R2': { "cubes": [0, 2, 7, 5], "rotation": 2, "vector": (1, 0, 0), "swaps": [5,7,2,0], "func": "rt" },
    'F': { "cubes": [0, 1, 2, 3], "rotation": -1, "vector": (0, 0, 1), "swaps": [1,3,0,2], "func": "f" },
    "F'": { "cubes": [0, 1, 2, 3], "rotation": 1, "vector": (0, 0, 1), "swaps": [2,0,3,1], "func": "fp" },
    'F2': { "cubes": [0, 1, 2, 3], "rotation": 2, "vector": (0, 0, 1), "swaps": [3,2,1,0], "func": "ft" },
    'U': { "cubes": [0, 1, 7, 4], "rotation": -1, "vector": (0, 1, 0), "swaps": [7,0,4,1], "func": "u" },
    "U'": { "cubes": [0, 1, 7, 4], "rotation": 1, "vector": (0, 1, 0), "swaps": [1,4,0,7], "func": "up" },
    'U2': { "cubes": [0, 1, 7, 4], "rotation": 2, "vector": (0, 1, 0), "swaps": [4,7,1,0], "func": "ut" },
    'B': { "cubes": [4, 7, 5, 6], "rotation": 1, "vector": (0, 0, 1), "swaps": [7,5,6,4], "func": "b" },
    "B'": { "cubes": [4, 7, 5, 6], "rotation": -1, "vector": (0, 0, 1), "swaps": [6,4,7,5], "func": "bp" },
    'B2': { "cubes": [4, 7, 5, 6], "rotation": 2, "vector": (0, 0, 1), "swaps": [5,6,4,7], "func": "bt" },
    'L': { "cubes": [4, 1, 3, 6], "rotation": 1, "vector": (1, 0, 0), "swaps": [6,4,1,3], "func": "l" },
    "L'": { "cubes": [4, 1, 3, 6], "rotation": -1, "vector": (1, 0, 0), "swaps": [1,3,6,4], "func": "lp" },
    'L2': { "cubes": [4, 1, 3, 6], "rotation": 2, "vector": (1, 0, 0), "swaps": [3,6,4,1], "func": "lt" },
    'D': { "cubes": [3, 2, 6, 5], "rotation": 1, "vector": (0, 1, 0), "swaps": [6,3,5,2], "func": "d" },
    "D'": { "cubes": [3, 2, 6, 5], "rotation": -1, "vector": (0, 1, 0), "swaps": [2,5,3,6], "func": "dp" },
    'D2': { "cubes": [3, 2, 6, 5], "rotation": 2, "vector": (0, 1, 0), "swaps": [5,6,2,3], "func": "dt" }
}

def solutionActivate(moves):
    for m in moves.split():
        move(m)
        sleep(0.2)
    
def moveBtn(btn):
    move(btn.text)
    solution = solver.solve(cube)
    print('Solution:', solution.moves())

def solveBtn(btn):
    global cube
    solution = solver.solve(cube)
    print('Solution:', solution.moves())
    solutionActivate(solution.moves())
    solution.reset()

def scrambleBtn(btn):
    solutionActivate("L F2 D' B L2 F'")

def move(move):
    global cube
    moveinfo = moves[move]
    for i in range(0,90):
        for j in moveinfo["cubes"]:
            cube2[j].rotate(angle = radians(moveinfo['rotation']), axis = vector(*moveinfo["vector"]), origin = vector(0,0,0))
        sleep(0.00001)
    cube2[moveinfo["cubes"][0]], cube2[moveinfo["cubes"][1]] ,cube2[moveinfo["cubes"][2]], cube2[moveinfo["cubes"][3]] = cube2[moveinfo["swaps"][0]], cube2[moveinfo["swaps"][1]], cube2[moveinfo["swaps"][2]], cube2[moveinfo["swaps"][3]]
    cube = getattr(cube, moveinfo["func"])()
    cube.render()

scene.width = 1500
scene.height = 675
scene.title = "Cube Solver"
scene.append_to_title("\n\n")


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

for label in moves.keys():
    button(text = label, bind = moveBtn, pos = scene.title_anchor)
# scene.append_to_caption("\n\n")
scene.append_to_caption("\n")
button(text = "Solve", bind = solveBtn)
button(text = "Scramble", bind = scrambleBtn)

while True:
    pass