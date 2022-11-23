from sympy import *

# Operator D
def op_D(f, t, ω0, β):
    return diff(f, t, 2) + 2*β*diff(f, t, 1) + ω0**2 * f

t = symbols("t", real=True)
ω0 = symbols("omega_0", real=True, positive=True)
β = symbols("beta", real=True, positive=True)

f0 = symbols("f_0", real=True, positive=True)
ω = symbols("omega", real=True, positive=True)


