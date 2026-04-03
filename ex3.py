# Problema 3 - Pequena Fábrica de Brinquedos

from pulp import *

prob = LpProblem("Brinquedos", LpMaximize)
x1 = LpVariable("Carrinhos", 0, None, LpInteger)
x2 = LpVariable("Bonecas", 0, None, LpInteger)

# Objetivo e Restrições
prob += 12*x1 + 10*x2

prob += 3*x1 + 2*x2 <= 60
prob += 2*x1 + 1*x2 <= 40
prob += 1*x1 + 1*x2 <= 30

prob.solve()

print("Status:", LpStatus[prob.status])
print("Carrinhos:", value(x1))
print("Bonecas:", value(x2))
print("Lucro máximo:", value(prob.objective))
