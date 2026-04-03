# Exercício 7 - Confecção de Uniformes Esportivos

from pulp import *

prob = LpProblem("Uniformes", LpMaximize)
x1 = LpVariable("Futebol", lowBound=2)
x2 = LpVariable("Basquete", lowBound=0, upBound=6)

prob += 40*x1 + 30*x2
prob += 3*x1 + 2*x2 <= 30 # Corte
prob += 2*x1 + 3*x2 <= 24 # Costura
prob += x1 + x2 <= 10 # Total

prob.solve()
print("Status:", LpStatus[prob.status])
print("Futebol:", value(x1))
print("Basquete:", value(x2))
print("Lucro:", value(prob.objective))