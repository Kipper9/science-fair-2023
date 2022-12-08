class Cube:
    def __init__(self):
        # Array Layout: U1, U2, U3, U4, L1, L2, F1, F2, ....
        self.cubies = [
            ['W'],['W'],
            ['W'],['W'],
            ['R'],['R'],['B'],['B'],['O'],['O'],
            ['R'],['R'],['B'],['B'],['O'],['O'],
            ['Y'],['Y'],
            ['Y'],['Y'],
            ['G'],['G'],
            ['G'],['G'],
            ]
    
    # These are all the turning functions for a Rubik's cube (tudo)
    
    # does a clockwise twist to top of the cube
    def u(self):
       self.cubies[0], self.cubies[1], self.cubies[2], self.cubies[3], self.cubies[4], self.cubies[5], self.cubies[6], self.cubies[7], self.cubies[8], self.cubies[9], self.cubies[22], self.cubies[23] = self.cubies[2], self.cubies[0], self.cubies[3], self.cubies[1], self.cubies[6], self.cubies[7], self.cubies[8], self.cubies[9], self.cubies[23], self.cubies[22], self.cubies[5], self.cubies[4]
    # does a counterclockwise twist to top of the cube
    def up(self):
        self.cubies[0], self.cubies[1], self.cubies[2], self.cubies[3], self.cubies[4], self.cubies[5], self.cubies[6], self.cubies[7], self.cubies[8], self.cubies[9], self.cubies[22], self.cubies[23] = self.cubies[1], self.cubies[3], self.cubies[0], self.cubies[2], self.cubies[23], self.cubies[22], self.cubies[4], self.cubies[5], self.cubies[6], self.cubies[7], self.cubies[9], self.cubies[8]
    # does a 180 turn to the top of the cube
    def ut(self):
        self.cubies[0], self.cubies[1], self.cubies[2], self.cubies[3], self.cubies[4], self.cubies[5], self.cubies[6], self.cubies[7], self.cubies[8], self.cubies[9], self.cubies[22], self.cubies[23] = self.cubies[3], self.cubies[2], self.cubies[1], self.cubies[0], self.cubies[8], self.cubies[9], self.cubies[23], self.cubies[22], self.cubies[4], self.cubies[5], self.cubies[7], self.cubies[6]
    
    # does a clockwise turn to the bottom layer
    def d(self):
       self.cubies[10], self.cubies[11], self.cubies[12], self.cubies[13], self.cubies[14], self.cubies[15], self.cubies[16], self.cubies[17], self.cubies[18], self .cubies[19], self.cubies[21], self.cubies[20] = self.cubies[21], self.cubies[22], self.cubies[10], self.cubies[11], self.cubies[12], self.cubies[13], self.cubies[18], self.cubies[16], self.cubies[19], self.cubies[17], self.cubies[14]
    # does a counterclockwise turn to the bottom layer
    def dp(self):
       self.cubies[10], self.cubies[11], self.cubies[12], self.cubies[13], self.cubies[14], self.cubies[15], self.cubies[16], self.cubies[17], self.cubies[18], self.cubies[19], self.cubies[21], self.cubies[20] = self.cubies[12], self.cubies[13], self.cubies[14], self.cubies[15], self.cubies[21], self.cubies[20], self.cubies[17], self.cubies[19], self.cubies[16], self.cubies[18], self.cubies[14]
    # does a 180 turn  to the bottom layer
    # def dt(self):


    # does a turn to the right hand side clockwise
    # def r(self):

    # # does a turn to the right hand side counterclockwise
    # def rp(self):

    # # does a 180 turn to the right han side of the cube
    # def rt(self):
    

    # # does a turn to the left hand side clockwise
    # def l(self):

    # # does a turn to the left hand side counterclockwise
    # def lp(self):

    # # does a 180 turn to the left hand side of the cube
    # def lt(self):

    # # does a clockwise turn to the front of the cube
    # def f(self):

    # # does a counterclockwise turn to the front of the cube
    # def fp(self):

    # # does a 180 turn to the front side of the cube
    # def ft(self):

   
    # # does a clockwise turn to the backside of the cube
    # def b(self):
 
    # # does a counterclockwise turn to the backside of the cube
    # def bp(self):
 
    # # does a 180 turn to the back side of the cube
    # def bt(self):


    def render(self):
        print(self.cubies)
