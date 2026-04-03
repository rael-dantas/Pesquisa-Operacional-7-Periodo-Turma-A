# Exercício 8 - Produção de Dispositivos Eletrônicos

from pulp import *

prob = LpProblem("Eletronicos", LpMaximize)
x1 = LpVariable("Tablets", lowBound=0, upBound=8)
x2 = LpVariable("Smartphones", lowBound=0)

prob += 100*x1 + 120*x2
prob += 4*x1 + 2*x2 <= 40 # Montagem
prob += x1 + 2*x2 <= 16 # Teste
prob += x2 <= 2*x1 # Relação
prob += x1 + x2 >= 5 # Produção mínima
prob.solve()

print("Status:", LpStatus[prob.status])
print("Tablets:", value(x1))
print("Smartphones:", value(x2))
print("Lucro:", value(prob.objective))