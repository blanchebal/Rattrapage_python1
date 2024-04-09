import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def draw(self):
        t = turtle.Turtle()
        t.speed(0)
        t.fillcolor("black")
        t.pencolor("red")  # Bordure rouge
        t.begin_fill()
        for _ in range(2):
            t.forward(self.longueur)
            t.left(90)
            t.forward(self.largeur)
            t.left(90)
        t.end_fill()
        turtle.done()

class Square(Rectangle):
    def __init__(self, cote, inclinaison=30):
        super().__init__(cote, cote)
        self.inclinaison = inclinaison

    def draw(self):
        t = turtle.Turtle()
        t.speed(0)
        t.fillcolor("black")
        t.pencolor("red")  # Bordure rouge
        t.begin_fill()
        t.left(self.inclinaison)
        for _ in range(4):
            t.forward(self.longueur)
            t.left(90)
        t.end_fill()
        turtle.done()

# Exemple d'utilisation
rectangle = Rectangle(200, 100)
rectangle.draw()

square = Square(150)
square.draw()