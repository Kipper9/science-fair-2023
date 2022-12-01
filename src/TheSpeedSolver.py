from Cube import Cube
cube = Cube()

numturns = int(input('How many turns: '))
turns = []

for i in range (1,numturns + 1):
    y = str(input('What is the turn: '))
    turns.append(y)

for y in range (0,numturns):
    if turns[y] == 'f':
        cube.f()
    
    elif turns[y] == 'fp':
        cube.fp()
    
    elif turns[y] == 'ft':
        cube.ft()
    
    elif turns[y] == 'u':
        cube.u()
    
    elif turns[y] == 'up':
        cube.up()
   
    elif turns[y] == 'ut':
        cube.ut()
    
    elif turns[y] == 'd':
        cube.d()
    
    elif turns[y] == 'dp':
        cube.dp()
    
    elif turns[y] == 'dt':
        cube.dt()
    
    elif turns[y] == 'r':
        cube.r()
    
    elif turns[y] == 'rp':
        cube.rp()
    
    elif turns[y] == 'rt':
        cube.rt()
    
    elif turns[y] == 'l':
        cube.l()
    
    elif turns[y] == 'lp':
        cube.lp()
    
    elif turns[y] == 'lt':
        cube.lt()
    
    elif turns[y] == 'b':
        cube.b()
    
    elif turns[y] == 'bp':
        cube.bp()
    
    elif turns[y] == 'bt':
        cube.bt()
    else:
        print('error: move',y,'is not indexed')

print('test: ', cube.render())