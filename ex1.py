# Exercício 1 - Confeitaria de Doces

from pulp import *

prob = LpProblem("Confeitaria", LpMaximize)

# Variáveis de Decisão
x1 = LpVariable("Chocolate", 0, None, LpInteger)
x2 = LpVariable("Baunilha", 0, None, LpInteger)

# Função Objetivo
prob += 20*x1 + 15*x2

# Restrições
prob += 2*x1 + 1*x2 <= 20  # Farinha
prob += 3*x1 + 3*x2 <= 36  # Ovos
prob += 1*x1 + 2*x2 <= 16  # Tempo
prob.solve()

print("Status:", LpStatus[prob.status])
print("Lucro:", value(prob.objective))
print("Chocolate:", value(x1))
print("Baunilha:", value(x2))
