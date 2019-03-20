class Example():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def minus(self):
        print(self.a - self.b)

ex = Example(1,2,3)
ex.minus()