# Exercício 4 - Oficina de Bicicletas

from pulp import *

prob = LpProblem("Brinquedos", LpMaximize)
x1 = LpVariable("Montanha", 0, None, LpInteger)
x2 = LpVariable("Passeios", 0, None, LpInteger)

# Objetivo e Restrições

prob += 80*x1 + 60*x2

prob += 2*x1 + 1*x2 <= 20
prob += 3*x1 + 3*x2 <= 45
prob += 1*x1 + 1*x2 <= 12
prob.solve()

print("Status:", LpStatus[prob.status])
print("Bicicleta para Montanha:", value(x1))
print("Bicicleta para Passeios:", value(x2))
print("Lucro máximo:", value(prob.objective))
