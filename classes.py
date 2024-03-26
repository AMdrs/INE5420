class DisplayFile:
    def __init__(self):
        self.display_file = []
    
    def new_object(self, name = "NoName", type = "P", coords = [(0, 0)]):
        if (type == "P" and len(coords) == 1):
            x = Point(name, type, coords)
        elif (type == "L" and len(coords) == 2):
            x = Line(name, type, coords)
        else:
            x = Wireframe(name, type, coords)

        self.display_file.append(x)

class Window:
    def __init__(self, x = 500, y = 500):
        
        self.xmin = 0
        self.ymin = 0
        self.xmax = x
        self.ymax = y

        self.width = self.xmax - self.xmin
        self.height = self.ymax - self.ymin
    
        self.center = [0, 0]
        self.setCenter()

    def getMin(self):
        return (self.xmin, self.ymin)
    
    def getMax(self):
        return (self.xmax, self.ymax)
    
    def getSize(self):
        return (self.width, self.height)
    
    def getCenter(self):
        return self.center
    
    #Zoom a partir do meio da tela
    def zoom(self, scale):
        self.width = self.width * scale
        self.height = self.height * scale

        self.xmin = self.center - (self.width / 2)
        self.ymin = self.center - (self.height / 2)
        self.xmax = self.xmin + self.width
        self.ymax = self.ymin + self.height

        self.setCenter()


    def move(self, x, y):
        self.xmin += x
        self.xmax += x
        self.ymin += y
        self.ymax += y

        self.setCenter()

    def setCenter(self):
        self.center[0] = (self.xmin + self.xmax) / 2
        self.center[1] = (self.ymin + self.ymax) / 2

class Object:
    def __init__(self, name, type, coords):
        self.name = name
        self.type = type
        self.coords = coords
        self.size = len(self.coords)
    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def getCoords(self):
        return self.coords
    
    def getSize(self):
        return self.size
        
class Point(Object):
    def getCoords(self):
        return self.coords[0]

class Line(Object):
    pass

class Wireframe(Object):
    pass
