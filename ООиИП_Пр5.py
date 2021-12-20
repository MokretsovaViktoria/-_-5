
class Win_Door:
    def __init__(self, x, y):
        self.square = x * y
class Room:
    def __init__(self, w, l, h):
        self.w = w
        self.l = l
        self.h = h
        self.wd = []
    def addWd(self, w, h):
        self.wd.append(Win_Door(w,h))
    def calcFullSquare(self):
        return self.w * self.l
    def workSurface(self):
        new_square = self.calcFullSquare()
        for i in self.wd:
            new_square -= i.square
        return new_square
    def requiredRolls(self, x, y):
        return self.workSurface / ( x * y)


r1 = Room(6,2, 2.7)
print(r1.calcFullSquare())
r1.addWd(1,1)
r1.addWd(1,1)
r1.addWd(1,2)