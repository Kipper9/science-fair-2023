from Cube import Cube

import slowSolver

cube = Cube()

while True:
    turn = str(input('What is your turn: '))

    if turn == 'f':
        cube = cube.f()
    
    elif turn == 'fp':
        cube = cube.fp()
    
    elif turn == 'ft':
        cube = cube.ft()
    
    elif turn == 'u':
        cube = cube.u()
    
    elif turn == 'up':
        cube = cube.up()
   
    elif turn == 'ut':
        cube = cube.ut()
    
    elif turn == 'd':
        cube = cube.d()
    
    elif turn == 'dp':
        cube = cube.d()
    
    elif turn == 'dt':
        cube = cube.dt()
    
    elif turn == 'r':
        cube = cube.r()
    
    elif turn == 'rp':
        cube = cube.rp()
    
    elif turn == 'rt':
        cube = cube.rt()
    
    elif turn == 'l':
        cube = cube.l()
    
    elif turn == 'lp':
        cube = cube.lp()
    
    elif turn == 'lt':
        cube = cube.lt()
    
    elif turn == 'b':
        cube = cube.b()
    
    elif turn == 'bp':
        cube.bp()
    
    elif turn == 'bt':
        cube = cube.bt()

    elif turn == 'solve':
        cube.reset()
        slowSolver.solve(cube)
        break
    
    elif turn == 'exit':
        break
    
    else:
        print('Error: move', turn ,'is not indexed')

    print ("The cube's state is:")
    cube.render()

    if cube.isSolved():
        print('The cube is solved!')
        break