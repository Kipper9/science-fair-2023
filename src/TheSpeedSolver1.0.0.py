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

    # does a u twist to the cube
    def u(self):
        self.cubies[0], self.cubies[1], self.cubies[2], self.cubies[3] = self.cubies[3], self.cubies[0], self.cubies[1], self.cubies[2]
    
    #def up(self):
        #todo
    # def ut():
    #     #todo
    
    def d(self):
        self.cubies[4], self.cubies[5], self.cubies[6], self.cubies[7] = self.cubies[7], self.cubies[4], self.cubies[5], self.cubies[6]
    # def dp():
    #     #todo
    # def dt():
    #     #todo
    
    # def r():
    #     #todo
    # def rp():
    #     #todo
    # def rt():
    
    # def l():
    #     #todo
    # def lp():
    #     #todo
    # def lt():
    #     #todo
    
    # def f():
    #     #todo
    # def fp():
    #     #todo
    # def ft():
    #     #todo
    
    # def b():
    #     #todo
    # def bp():
    #     #todo
    # def bt():
    #     #todo

    def render(self):
        print(self.cubies)



cube = Cube()
print('step1: ', end = '')
cube.render()

cube.u()
print('step2: ', end = '')
cube.render()

cube = Cube()
cube.d()
print('step3: ', end = '')
cube.render()