# Exercício 9 - Mix de Produção de Móveis Modulados

from pulp import *
prob = LpProblem("Producao_Moveis", LpMaximize)

# Variáveis
x1 = LpVariable("Armarios", lowBound=5)
x2 = LpVariable("Estantes", lowBound=5)
x3 = LpVariable("Gaveteiros", lowBound=5)

# Função objetivo
prob += 150*x1 + 100*x2 + 80*x3

# Restrições
prob += 10*x1 + 5*x2 + 4*x3 <= 200 # MDF
prob += 6*x1 + 3*x2 + 2*x3 <= 120 # Horas
prob += x1 <= 15 # Demanda armários
prob += x2 + x3 <= 30 # Logística

# Resolver
prob.solve()
print("Status:", LpStatus[prob.status])
print("Armários:", value(x1))
print("Estantes:", value(x2))
print("Gaveteiros:", value(x3))
print("Lucro máximo:", value(prob.objective))