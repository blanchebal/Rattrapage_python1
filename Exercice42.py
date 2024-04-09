from math import gcd

class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur

    def invert(self):
        return Fraction(self.denominateur, self.numerateur)

    def simplify(self):
        diviseur = gcd(self.numerateur, self.denominateur)
        return Fraction(self.numerateur // diviseur, self.denominateur // diviseur)

    def __mul__(self, autre_fraction):
        return Fraction(self.numerateur * autre_fraction.numerateur, self.denominateur * autre_fraction.denominateur)

    def __add__(self, autre_fraction):
        nouveau_numerateur = self.numerateur * autre_fraction.denominateur + autre_fraction.numerateur * self.denominateur
        nouveau_denominateur = self.denominateur * autre_fraction.denominateur
        return Fraction(nouveau_numerateur, nouveau_denominateur)

    def __sub__(self, autre_fraction):
        nouveau_numerateur = self.numerateur * autre_fraction.denominateur - autre_fraction.numerateur * self.denominateur
        nouveau_denominateur = self.denominateur * autre_fraction.denominateur
        return Fraction(nouveau_numerateur, nouveau_denominateur)

    def __truediv__(self, autre_fraction):
        return self * autre_fraction.invert()

    def __str__(self):
        return f"{self.numerateur}/{self.denominateur}"

    def non_simplified(self):
        return f"{self.numerateur}/{self.denominateur}"

    @classmethod
    def from_string(cls, chaine):
        numerateur, denominateur = map(int, chaine.split('/'))
        return cls(numerateur, denominateur)

def main():
    f1 = Fraction(2, 4)
    f2 = Fraction(1, 4)
    f3 = f1 + f2
    f4 = f1 - f2
    f5 = f1 * f2
    f6 = f1 / f2
    f7 = Fraction(4, 10)
    f8 = Fraction.from_string('5/10')

    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7.simplify())
    print(f7.invert())
    print(f8)
    print(f3.non_simplified())

main()