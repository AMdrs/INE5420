from classes import *
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt


class Viewport(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.width = 500
        self.height = 500

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(self.width, self.height)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_point()

    def transform(self, xw, yw, window):
        xwmin = window.getMin()
        ywmin = xwmin[1]
        xwmin = xwmin[0]
        wwidth = window.getSize()
        wheigth = wwidth[1]
        wwidth = wwidth[0]

        xvp = int((xw - xwmin) / wwidth * self.width)
        yvp = int((1 - ((yw - ywmin) / wheigth)) * self.height)

        return [xvp, yvp]

    def draw_point(self, object = None):

        if (object == None):
            return 1;

        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        coords = object.getCoords()
        new_coords = viewport.transform(coords[0], coords[1], window)
        painter.drawPoint(new_coords[0], new_coords[1])
        
        painter.end()
        self.label.setPixmap(canvas)

    def draw_line(self, object = None):

        if (object == None):
            return 1;

        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        coords = object.getCoords()
        new_coords = []
        for i in coords:
            new_coords.append(viewport.transform(i[0], i[1], window))
        painter.drawLine(new_coords[0][0], new_coords[0][1], new_coords[1][0], new_coords[1][1])
        
        painter.end()
        self.label.setPixmap(canvas)

display_file = DisplayFile()
window = Window()

app = QtWidgets.QApplication([])
viewport = Viewport()
viewport.show()

display_file.new_object("P1", "P", [(100, 100)])
viewport.draw_point(display_file.display_file[-1])
display_file.new_object("L1", "L", [(300,200), (10, 478)])
viewport.draw_line(display_file.display_file[-1])

app.exec()