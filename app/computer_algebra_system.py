import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define functions
f = sp.sin(x)
g = sp.cos(y)

# Perform algebraic operations
h = f + g
print(h)

# Solve equations
sol = sp.solve([sp.diff(f, x) - 1, sp.diff(g, y) - 1], [x, y])
print(sol)

# Perform calculus operations
integral = sp.integrate(h, x)
print(integral)
