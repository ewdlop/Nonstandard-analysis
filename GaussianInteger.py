class GaussianInteger:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b}i"

    def __add__(self, other):
        return GaussianInteger(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return GaussianInteger(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        real = self.a * other.a - self.b * other.b
        imag = self.a * other.b + self.b * other.a
        return GaussianInteger(real, imag)

    def conjugate(self):
        return GaussianInteger(self.a, -self.b)

    def norm(self):
        return self.a**2 + self.b**2

# Example usage:
g1 = GaussianInteger(3, 4)
g2 = GaussianInteger(1, 2)

print("g1:", g1)
print("g2:", g2)
print("Sum:", g1 + g2)
print("Product:", g1 * g2)
print("Conjugate of g1:", g1.conjugate())
print("Norm of g1:", g1.norm())
