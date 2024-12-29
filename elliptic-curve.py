from sympy import symbols, Eq, solveset

# Define the variables
x, y = symbols('x y')

# Define an elliptic curve equation y^2 = x^3 + ax + b
a, b = 2, 3
elliptic_curve_eq = Eq(y**2, x**3 + a*x + b)

# Solve the equation for y
solutions = solveset(elliptic_curve_eq, y)
print("Solutions for the elliptic curve:", solutions)
