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

    # does a clockwise twist to top of the cube the cube
    def u(self):
        self.cubies[0], self.cubies[2], self.cubies[2], self.cubies[3] = self.cubies[3], self.cubies[0], self.cubies[1], self.cubies[2]
    def up(self):
        self.cubies[0], self.cubies[1], self.cubies[2], self.cubies[3] = self.cubies[3], self.cubies[0], self.cubies[1], self.cubies[2]
    # def ut(self):
        #todo

    # does a clockwise turn to the bottom layer
    def d(self):
        self.cubies[4], self.cubies[5], self.cubies[6], self.cubies[7] = self.cubies[7], self.cubies[4], self.cubies[5], self.cubies[6]
    def dp(self):
        self.cubies[4], self.cubies[5], self.cubies[6], self.cubies[7] = self.cubies[5], self.cubies[6], self.cubies[7], self.cubies[4]
    # def dt(self):
        #todo

    # does a turn to the right hand side clockwise
    def r(self):
        self.cubies[1], self.cubies[5], self.cubies[6], self.cubies[2] = self.cubies[5], self.cubies[6], self.cubies[2], self.cubies[1]
    def rp(self):
        self.cubies[1], self.cubies[5], self.cubies[6], self.cubies[2] = self.cubies[2], self.cubies[1], self.cubies[5], self.cubies[6]
    # def rt(self):
    
    # does a turn to the left hand side clockwise
    def l(self):
        self.cubies[0], self.cubies[4], self.cubies[7], self.cubies[3] = self.cubies[3], self.cubies[0], self.cubies[4], self.cubies[7]
    # def lp():
        #todo
    # def lt():
        #todo
    
    # does a clockwise turn to the front of the cube
    def f(self):
        self.cubies[1], self.cubies[5], self.cubies[4], self.cubies[0] = self.cubies[0], self.cubies[1], self.cubies[5], self.cubies[4]

    # def fp():
        #todo
    # def ft():
        #todo
   
    # does a clockwise turn to the backside of the cube
    def b(self):
        self.cubies[3], self.cubies[7], self.cubies[6], self.cubies[2] = self.cubies[2], self.cubies[3], self.cubies[7], self.cubies[6]
    # def bp():
        #todo
    # def bt():
        #todo

    def render(self):
        print(self.cubies)

cube = Cube()
print('s: ', end = '')
cube.render()

cube.dp()
print('rp: ', end = '')
cube.render()