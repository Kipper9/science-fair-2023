from Cube import Cube

import Solver_5 as Solver

cube = Cube()

while True:
    turn = str(input('What function: '))

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
        cube = cube.dp()
    
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
        Solver.solve(cube)
        break

    elif turn == 's1':
        cube = cube.u()
        cube = cube.rt()
        cube = cube.fp()

    elif turn == 's2':
        cube = cube.u()
        cube = cube.rt()
        cube = cube.fp()
        cube = cube.dt()

    elif turn == 's3':
        cube = cube.u()
        cube = cube.rt()
        cube = cube.fp()
        cube = cube.dt()
        cube = cube.ft()

    elif turn == 'exit':
        break
    
    else:
        print('Error: move', turn ,'is not indexed')

    print ("The cube's state is:")
    cube.render()

    if cube.isSolved():
        print('The cube is solved!')
        break