class SLI(object):
    def __init__(self):
        self.l_x = 3
        self.l_y = 3
        self.f_x = 0.1
        self.f_y = 0.4
 
        self.x = l_x + f_x
        self.y = l_y + f_y
        def theta(x):
            if 0 <= x and x < 1:
                return x
            elif x > 1:
                return math.exp(theta(x-1))
            else:
                return 1
 
        def a_y(j):
            if l_y-1 == j:
                return math.exp(-f_y)
            else:
                return math.exp(-1/a_y(j+1))
        def eps(j):
            if l_x -1 == j:
                return math.exp(-f_x)
            else:
                return math.exp(-1/eps(j+1))
        def alg():
           c = 1 + self.eps(0)/self.a_y(0)
           j = 1
           if l_x == 1:
           h = self.f_x + math.log(c,math.e)
           while h >=1:
                j = j+1
                h = math.log(h,math.e)
           return j + h
          else: c = 1 + eps(1)*math.log(c,math.e)
          while (j < l_x - 1 and c >= eps(j)):
              j = j + 1
              c = 1 + eps(j)*math.log(c,math.e)
         if c < eps(j):
            z = j + c/eps(j)
            return z
         j = l_x
         h = f_x + math.log(c,math.e)
        while h >=1:
            j = j+1
            h = math.log(h,math.e)
        return j + h
