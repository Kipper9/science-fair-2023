from Cube import Cube

cube = Cube()

while True:
    turn = str(input('What is your turn: '))

    if turn == 'f':
        cube.f()
    
    elif turn == 'fp':
        cube.fp()
    
    elif turn == 'ft':
        cube.ft()
    
    elif turn == 'u':
        cube.u()
    
    elif turn == 'up':
        cube.up()
   
    elif turn == 'ut':
        cube.ut()
    
    elif turn == 'd':
        cube.d()
    
    elif turn == 'dp':
        cube.d()
    
    elif turn == 'dt':
        cube.dt()
    
    elif turn == 'r':
        cube.r()
    
    elif turn == 'rp':
        cube.rp()
    
    elif turn == 'rt':
        cube.rt()
    
    elif turn == 'l':
        cube.l()
    
    elif turn == 'lp':
        cube.lp()
    
    elif turn == 'lt':
        cube.lt()
    
    elif turn == 'b':
        cube.b()
    
    elif turn == 'bp':
        cube.bp()
    
    elif turn == 'bt':
        cube.bt()
    elif turn == 'exit':
        break
    else:
        print('error: move', turn ,'is not indexed')

        
    
    print ("The cube's state is:", end ='')
    cube.render()

    if cube.isSolved():
        print('The cube is solved!')
        break