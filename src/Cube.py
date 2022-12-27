class Cube:
   # Array Layout: U1, U2, U3, U4, L1, L2, F1, F2, ....
   def __init__(self, cubies=[
         'W','W',
         'W','W',
         'R','R','B','B','O','O',
         'R','R','B','B','O','O',         
         'Y','Y',
         'Y','Y',
         'G','G',
         'G','G',
         ], parent = None):
      self.cubies = cubies
      self.parent = parent
    
   # These are all the turning functions for a Rubik's cube (tudo)
    
   # does a clockwise twist to top of the cube
   def u(self):
      _cubies = self.cubies.copy()
      _cubies[0], _cubies[1], _cubies[2], _cubies[3], _cubies[4], _cubies[5], _cubies[6], _cubies[7], _cubies[8], _cubies[9], _cubies[22], _cubies[23] = _cubies[2], _cubies[0], _cubies[3], _cubies[1], _cubies[6], _cubies[7], _cubies[8], _cubies[9], _cubies[23], _cubies[22], _cubies[5], _cubies[4]

      return Cube(_cubies, self)
   # does a counterclockwise twist to top of the cube
   def up(self):
      _cubies = self.cubies.copy()
      _cubies[0], _cubies[1], _cubies[2], _cubies[3], _cubies[4], _cubies[5], _cubies[6], _cubies[7], _cubies[8], _cubies[9], _cubies[22], _cubies[23] = _cubies[1], _cubies[3], _cubies[0], _cubies[2], _cubies[23], _cubies[22], _cubies[4], _cubies[5], _cubies[6], _cubies[7], _cubies[9], _cubies[8]
      
      return Cube(_cubies, self)
   # does a 180 turn to the top of the cube
   def ut(self):
      _cubies = self.cubies.copy()
      _cubies[0], _cubies[1], _cubies[2], _cubies[3], _cubies[4], _cubies[5], _cubies[6], _cubies[7], _cubies[8], _cubies[9], _cubies[22], _cubies[23] = _cubies[3], _cubies[2], _cubies[1], _cubies[0], _cubies[8], _cubies[9], _cubies[23], _cubies[22], _cubies[4], _cubies[5], _cubies[7], _cubies[6]
      
      return Cube(_cubies, self)

   # does a clockwise turn to the bottom layer
   def d(self):
      _cubies = self.cubies.copy()
      _cubies[10], _cubies[11], _cubies[12], _cubies[13], _cubies[14], _cubies[15], _cubies[16], _cubies[17], _cubies[18], _cubies[19], _cubies[21], _cubies[20] = _cubies[21], _cubies[20], _cubies[10], _cubies[11], _cubies[12], _cubies[13], _cubies[18], _cubies[16], _cubies[19], _cubies[17], _cubies[14], _cubies[15]
      
      return Cube(_cubies, self)
   # does a counterclockwise turn to the bottom layer
   def dp(self):
      _cubies = self.cubies.copy()
      _cubies[10], _cubies[11], _cubies[12], _cubies[13], _cubies[14], _cubies[15], _cubies[16], _cubies[17], _cubies[18], _cubies[19], _cubies[21], _cubies[20] = _cubies[12], _cubies[13], _cubies[14], _cubies[15], _cubies[21], _cubies[20], _cubies[17], _cubies[19], _cubies[16], _cubies[18], _cubies[10], _cubies[11]
      
      return Cube(_cubies, self)
   # does a 180 turn  to the bottom layer
   def dt(self):
      _cubies = self.cubies.copy()
      _cubies[10], _cubies[11], _cubies[12], _cubies[13], _cubies[14], _cubies[15], _cubies[16], _cubies[17], _cubies[18], _cubies[19], _cubies[21], _cubies[20] = _cubies[14], _cubies[15], _cubies[21], _cubies[20], _cubies[10], _cubies[11], _cubies[19], _cubies[18], _cubies[17], _cubies[16], _cubies[12], _cubies[13]

      return Cube(_cubies, self)
   
   # does a turn to the right hand side clockwise
   def r(self):
      _cubies = self.cubies.copy()
      _cubies[3], _cubies[1], _cubies[7], _cubies[13], _cubies[17], _cubies[19], _cubies[21], _cubies[23], _cubies[8], _cubies[9], _cubies[14], _cubies[15] = _cubies[7], _cubies[13], _cubies[17], _cubies[19], _cubies[21], _cubies[23], _cubies[1], _cubies[3], _cubies[14], _cubies[8], _cubies[15], _cubies[9]
   
      return Cube(_cubies, self)
    # does a turn to the right hand side counterclockwise
   def rp(self):
      _cubies = self.cubies.copy()
      _cubies[3], _cubies[1], _cubies[7], _cubies[13], _cubies[17], _cubies[19], _cubies[21], _cubies[23], _cubies[8], _cubies[9], _cubies[14], _cubies[15] = _cubies[21], _cubies[23], _cubies[1], _cubies[3], _cubies[7], _cubies[13], _cubies[17], _cubies[19], _cubies[9], _cubies[15], _cubies[8], _cubies[14]
   
      return Cube(_cubies, self)
    # does a 180 turn to the right han side of the cube
   def rt(self):
      _cubies = self.cubies.copy()
      _cubies[3], _cubies[1], _cubies[7], _cubies[13], _cubies[17], _cubies[19], _cubies[21], _cubies[23], _cubies[8], _cubies[9], _cubies[14], _cubies[15] = _cubies[17], _cubies[19], _cubies[21], _cubies[23], _cubies[1], _cubies[3], _cubies[7], _cubies[13], _cubies[15], _cubies[14], _cubies[9], _cubies[8]
   
      return Cube(_cubies, self)

   # does a turn to the left hand side clockwise
   def l(self):
      _cubies = self.cubies.copy()
      _cubies[0], _cubies[2], _cubies[6], _cubies[12], _cubies[16], _cubies[18], _cubies[20], _cubies[22], _cubies[4], _cubies[5], _cubies[10], _cubies[11] = _cubies[20], _cubies[22], _cubies[0], _cubies[2], _cubies[6], _cubies[12], _cubies[16], _cubies[18], _cubies[10], _cubies[4], _cubies[11], _cubies[5]
   
      return Cube(_cubies, self)
   # does a turn to the left hand side counterclockwise
   def lp(self):
      _cubies = self.cubies.copy()
      _cubies[0], _cubies[2], _cubies[6], _cubies[12], _cubies[16], _cubies[18], _cubies[20], _cubies[22], _cubies[4], _cubies[5], _cubies[10], _cubies[11] = _cubies[6], _cubies[12], _cubies[16], _cubies[18], _cubies[20], _cubies[22], _cubies[0], _cubies[2], _cubies[5], _cubies[11], _cubies[4], _cubies[10]
   
      return Cube(_cubies, self)
   # does a 180 turn to the left hand side of the cube
   def lt(self):
      _cubies = self.cubies.copy()
      _cubies[0], _cubies[2], _cubies[6], _cubies[12], _cubies[16], _cubies[18], _cubies[20], _cubies[22], _cubies[4], _cubies[5], _cubies[10], _cubies[11] = _cubies[16], _cubies[18], _cubies[20], _cubies[22], _cubies[0], _cubies[2], _cubies[6], _cubies[12], _cubies[11], _cubies[10], _cubies[5], _cubies[4]
   
      return Cube(_cubies, self)
   
   # does a clockwise turn to the front of the cube
   def f(self):
      _cubies = self.cubies.copy()
      _cubies[2], _cubies[3], _cubies[8], _cubies[14], _cubies[17], _cubies[16], _cubies[11], _cubies[5], _cubies[6], _cubies[7], _cubies[12], _cubies[13] = _cubies[11], _cubies[5], _cubies[2], _cubies[3], _cubies[8], _cubies[14], _cubies[17], _cubies[16], _cubies[12], _cubies[6], _cubies[13], _cubies[7]
   
      return Cube(_cubies, self)
   # does a counterclockwise turn to the front of the cube
   def fp(self):
      _cubies = self.cubies.copy()
      _cubies[2], _cubies[3], _cubies[8], _cubies[14], _cubies[17], _cubies[16], _cubies[11], _cubies[5], _cubies[6], _cubies[7], _cubies[12], _cubies[13] = _cubies[8], _cubies[14], _cubies[17], _cubies[16], _cubies[11], _cubies[5], _cubies[2], _cubies[3], _cubies[7], _cubies[13], _cubies[6], _cubies[12]
   
      return Cube(_cubies, self)
   # does a 180 turn to the front side of the cube
   def ft(self):
      _cubies = self.cubies.copy()
      _cubies[2], _cubies[3], _cubies[8], _cubies[14], _cubies[17], _cubies[16], _cubies[11], _cubies[5], _cubies[6], _cubies[7], _cubies[12], _cubies[13] = _cubies[17], _cubies[16], _cubies[11], _cubies[5], _cubies[2], _cubies[3], _cubies[8], _cubies[14], _cubies[13], _cubies[12], _cubies[7], _cubies[6]

      return Cube(_cubies, self)


   # does a clockwise turn to the backside of the cube
   def b(self):
      _cubies = self.cubies.copy()
      _cubies[0], _cubies[1], _cubies[9], _cubies[15], _cubies[19], _cubies[18], _cubies[10], _cubies[4], _cubies[23], _cubies[22], _cubies[21], _cubies[20] = _cubies[9], _cubies[15], _cubies[19], _cubies[18], _cubies[10], _cubies[4], _cubies[0], _cubies[1], _cubies[21], _cubies[23], _cubies[20], _cubies[22]
   
      return Cube(_cubies, self)
   # does a counterclockwise turn to the backside of the cube
   def bp(self):
      _cubies = self.cubies.copy()
      _cubies[0], _cubies[1], _cubies[9], _cubies[15], _cubies[19], _cubies[18], _cubies[10], _cubies[4], _cubies[23], _cubies[22], _cubies[21], _cubies[20] = _cubies[10], _cubies[4], _cubies[0], _cubies[1], _cubies[9], _cubies[15], _cubies[19], _cubies[18], _cubies[22], _cubies[20], _cubies[23], _cubies[21]
   
      return Cube(_cubies, self)
   # does a 180 turn to the back side of the cube
   def bt(self):
      _cubies = self.cubies.copy()
      _cubies[0], _cubies[1], _cubies[9], _cubies[15], _cubies[19], _cubies[18], _cubies[10], _cubies[4], _cubies[23], _cubies[22], _cubies[21], _cubies[20] = _cubies[19], _cubies[18], _cubies[10], _cubies[4], _cubies[0], _cubies[1], _cubies[9], _cubies[15], _cubies[20], _cubies[21], _cubies[22], _cubies[23]
   
      return Cube(_cubies, self)
   
   def isSolved(self):
      return (self.cubies[0] == self.cubies[1] == self.cubies[2] == self.cubies[3] and 
         self.cubies[4] == self.cubies[5] == self.cubies[10] == self.cubies[11] and 
         self.cubies[6] == self.cubies[7] == self.cubies[12] == self.cubies[13] and 
         self.cubies[8] == self.cubies[9] == self.cubies[14] == self.cubies[15] and 
         self.cubies[16] == self.cubies[17] == self.cubies[18] == self.cubies[19] and 
         self.cubies[20] == self.cubies[21] == self.cubies[22] == self.cubies[23])

   def render(self):

      if self.parent:
         self.parent.render()
         print("->")
      print(self.cubies)

   def reset(self):
      self.parent = None

   def __eq__(self, other):
      self.cubies == other.cubies

   def __hash__(self):
      return hash(tuple(self.cubies))