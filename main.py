import numpy as np
from PIL import Image

class Canvas:

    def __init__(self,height,width,color):
        self.height = height
        self.width = width
        self.color = color

        self.data = np.zeros((self.height, self.width,3), dtype= np.uint8)
        self.data[:] = self.color

    def make(self,imagepath):
        img = Image.fromarray(self.data, mode='RGB')
        img.save(imagepath)


class Rectangle:

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color

canvas = Canvas(20,30,(255,255,255))
r1 = Rectangle(1,6,7,10,(100,100,125))
r1.draw(canvas)
canvas.make('canvas.png')