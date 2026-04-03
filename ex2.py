# Exercício 2 - Marcenaria Artesanal

from pulp import *

prob = LpProblem("Marcenaria", LpMaximize)

x1 = LpVariable("Mesas", 0, None, LpInteger)
x2 = LpVariable("Cadeiras", 0, None, LpInteger)

prob += 50*x1 + 30*x2

prob += 5*x1 + 2*x2 <= 100
prob += 4*x1 + 2*x2 <= 60
prob += x1 + x2 <= 25

prob.solve()

print("Status:", LpStatus[prob.status])
print("Mesas:", value(x1))
print("Cadeiras:", value(x2))
print("Lucro máximo:", value(prob.objective))
