# Exercício 6 - Fábrica de Tintas Residenciais

from pulp import *

prob = LpProblem("Tintas", LpMaximize)
x1 = LpVariable("Fachadas", lowBound=0)
x2 = LpVariable("Interiores", lowBound=0, upBound=2)

prob += 10*x1 + 8*x2
prob += 6*x1 + 4*x2 <= 24 # Pigmento
prob += x1 + 2*x2 <= 6 # Solvente
prob += x2 <= x1 + 1 # Relação demanda
prob += x1 + x2 <= 5 # Produção total

prob.solve()

print("Status:", LpStatus[prob.status])
print("Fachadas:", value(x1))
print("Interiores:", value(x2))
print("Lucro máximo:", value(prob.objective))