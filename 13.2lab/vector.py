class VECTOR:
    def __init__(self, Name, x1, y1, x2, y2):
        self.Name = Name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def GetLen(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1
        return (x*x + y*y)**0.5

    def Plus(self, v):
        x = self.x2 - self.x1
        y = self.y2 - self.y1

        x_new = v.x2 - v.x1
        y_new = v.y2 - v.y1

        return VECTOR("Сума векторів", 0, 0, x + x_new, y + y_new)

    def ShowName(self):
        print(self.Name)

    def SetCoord(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2