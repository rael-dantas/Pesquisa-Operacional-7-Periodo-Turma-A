# Problema 10 - Otimização de Dieta para Gado de Corte

from pulp import *

prob = LpProblem("Otimização de Dieta para Gado de Corte", LpMaximize)

# Variáveis de Decisão
x1 = LpVariable("Milho", 0, None, LpInteger)
x2 = LpVariable("Farelo de Soja", 0, None, LpInteger)
x3 = LpVariable("Suplemento Mineral", 0, None, LpInteger)


# Função Objetivo
prob += 2*x1 + 5*x2 + 12*x3

# Restrições
prob += 5*x1 + 20*x2 + 10*x3 >= 400  
prob += 30*x1 + 10*x2 + 5*x3 >= 600  
prob += 1*x1 + 1*x2 + 1*x3 <= 100  
prob += 1*x2 <= 2*x1 
prob += 1*x1 + 1*x2 + 1*x3 >= 0.1*x3
prob.solve()

print("Status:", LpStatus[prob.status])
print("Milho:", value(x1))
print("Farelo de Soja:", value(x2))
print("Suplemento Natural:", value(x3))
print("Lucro máximo:", value(prob.objective))