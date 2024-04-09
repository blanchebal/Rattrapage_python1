import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def tracer_figure(self):
        t = turtle.Turtle()
        t.speed(0)
        t.color("red")
        t.forward(self.longueur)
        t.right(90)
        t.color("blue")
        t.forward(self.largeur)
        t.right(90)
        t.color("green")
        t.forward(self.longueur)
        t.right(90)
        t.color("purple")
        t.forward(self.largeur)
        turtle.done()
rectangle = Rectangle(200, 100)
rectangle.tracer_figure()