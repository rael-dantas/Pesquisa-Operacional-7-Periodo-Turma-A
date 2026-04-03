# Problema 5 - Produção de Sucos Naturais

from pulp import *

prob = LpProblem("Sucos", LpMaximize)
x1 = LpVariable("Laranja", lowBound=0)
x2 = LpVariable("Melancia", lowBound=0)

prob += 8*x1 + 6*x2
prob += 10*x1 + 2*x2 <= 100 # Frutas
prob += 5*x1 + 10*x2 <= 120 # Tempo
prob += x1 + x2 <= 20 # Armazenamento

prob.solve()
print("Status:", LpStatus[prob.status])
print("Laranja:", value(x1))
print("Melancia:", value(x2))
print("Lucro:", value(prob.objective))