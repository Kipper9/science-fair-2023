class Cube:
    def __init__(self):
        self.cubies = [
            ['W','R','B'],
            ['W','B','O'],
            ['W','O','G'],
            ['W','G','R'],

            ['R','B','Y'],
            ['B','O','Y'],
            ['O','G','Y'],
            ['G','R','Y']
        ]

    # does a clockwise twist to top of the cube
    def u(self):
        self.cubies[0], self.cubies[2], self.cubies[2], self.cubies[3] = self.cubies[3], self.cubies[0], self.cubies[1], self.cubies[2]
    # does a counterclockwise twist to top of the cube
    def up(self):
        self.cubies[0], self.cubies[1], self.cubies[2], self.cubies[3] = self.cubies[3], self.cubies[0], self.cubies[1], self.cubies[2]
    # does a 180 turn to the top of the cube
    def ut(self):
        self.cubies[0], self.cubies[4], self.cubies[7], self.cubies[3] = self.cubies[7], self.cubies[3], self.cubies[0], self.cubies[4]
    
    # does a clockwise turn to the bottom layer
    def d(self):
        self.cubies[4], self.cubies[5], self.cubies[6], self.cubies[7] = self.cubies[7], self.cubies[4], self.cubies[5], self.cubies[6]
    # does a counterclockwise turn to the bottom layer
    def dp(self):
        self.cubies[4], self.cubies[5], self.cubies[6], self.cubies[7] = self.cubies[5], self.cubies[6], self.cubies[7], self.cubies[4]
    # does a 180 turn  to the bottom layer
    def dt(self):
        self.cubies[4], self.cubies[5], self.cubies[6], self.cubies[7] = self.cubies[6], self.cubies[7], self.cubies[4], self.cubies[5]

    # does a turn to the right hand side clockwise
    def r(self):
        self.cubies[1], self.cubies[5], self.cubies[6], self.cubies[2] = self.cubies[5], self.cubies[6], self.cubies[2], self.cubies[1]
    # does a turn to the right hand side counterclockwise
    def rp(self):
        self.cubies[1], self.cubies[5], self.cubies[6], self.cubies[2] = self.cubies[2], self.cubies[1], self.cubies[5], self.cubies[6]    
    # does a 180 turn to the right han side of the cube
    def rt(self):
        self.cubies[1], self.cubies[5], self.cubies[6], self.cubies[2] = self.cubies[6], self.cubies[2], self.cubies[1], self.cubies[5]    
    
    # does a turn to the left hand side clockwise
    def l(self):
        self.cubies[0], self.cubies[4], self.cubies[7], self.cubies[3] = self.cubies[3], self.cubies[0], self.cubies[4], self.cubies[7]
    # does a turn to the left hand side counterclockwise
    def lp(self):
        self.cubies[0], self.cubies[4], self.cubies[7], self.cubies[3] = self.cubies[4], self.cubies[7], self.cubies[3], self.cubies[0]
    # def lt(self):
        #todo
    
    # does a clockwise turn to the front of the cube
    def f(self):
        self.cubies[0], self.cubies[4], self.cubies[7], self.cubies[3] = self.cubies[3], self.cubies[0], self.cubies[4], self.cubies[7]
    # does a counterclockwise turn to the front of the cube
    def fp(self):
        self.cubies[0], self.cubies[4], self.cubies[7], self.cubies[3] = self.cubies[4], self.cubies[7], self.cubies[3], self.cubies[0]
    # def ft(self):
        #todo
   
    # does a clockwise turn to the backside of the cube
    def b(self):
        self.cubies[3], self.cubies[7], self.cubies[6], self.cubies[2] = self.cubies[2], self.cubies[3], self.cubies[7], self.cubies[6]
    # does a counterclockwise turn to the backside of the cube
    def bp(self):
        self.cubies[2], self.cubies[6], self.cubies[7], self.cubies[3] = self.cubies[3], self.cubies[2], self.cubies[6], self.cubies[7]
    # def bt(self):
        #todo

    def render(self):
        print(self.cubies)

cube = Cube()
print('test: ', end = '')
cube.render()

cube.rt()
print('test: ', end = '')
cube.render()