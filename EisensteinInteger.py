import cmath

class EisensteinInteger:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.omega = (-1 + cmath.sqrt(3) * 1j) / 2

    def __str__(self):
        return f"{self.a} + {self.b}ω"

    def __add__(self, other):
        return EisensteinInteger(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return EisensteinInteger(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        real = self.a * other.a - self.b * other.b
        imag = self.a * other.b + self.b * other.a
        return EisensteinInteger(real, imag)

    def conjugate(self):
        return EisensteinInteger(self.a, -self.b)

    def norm(self):
        return self.a**2 + self.a*self.b + self.b**2

# Example usage:
e1 = EisensteinInteger(3, 4)
e2 = EisensteinInteger(1, 2)

print("e1:", e1)
print("e2:", e2)
print("Sum:", e1 + e2)
print("Product:", e1 * e2)
print("Conjugate of e1:", e1.conjugate())
print("Norm of e1:", e1.norm())
