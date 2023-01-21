from vpython import *
from time import *

floor = box(pos = vector(0,-5,0), color = color.yellow, size = vector(10,.1,10))
ceiling = box(pos = vector(0,5,0), color = color.white, size = vector(10,.1,10))
backWall = box(pos = vector(0,0,-5), color = color.green, size = vector(10,10,.1))
leftWall = box(pos = vector(-5,0,0), color = color.red, size = vector(.1,10,10))
rightWall = box(pos = vector(5,0,0), color = color.orange, size = vector(.1,10,10))
frontWall = box(pos = vector(0,0,5), color = color.blue, size = vector(10,10,.1))
global cubie1

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

}

def move (move):
    moveinfo = moves[move]
    for i in range(0,90):
        for j in moveinfo["cubes"]:
            cube[j].rotate(angle = radians(moveinfo['rotation']), axis = vector(*moveinfo["vector"]), origin = vector(0,0,0))
        sleep(0.001)
    cube2[moveinfo["cubes"][0]], cube2[moveinfo["cubes"][1]] ,cube2[moveinfo["cubes"][2]], cube2[moveinfo["cubes"][3]] = cube2[moveinfo["swaps"][0]], cube2[moveinfo["swaps"][1]], cube2[moveinfo["swaps"][2]], cube2[moveinfo["swaps"][3]]