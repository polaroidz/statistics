# -*- coding: utf-8 -*-
import math
import numpy as np
import scipy.stats as stats

np.random.seed(seed=42)

p_hat = 0.25 #@param
p_pop = 0.50 #@param

alpha = 0.05 #@param

n = 42 #@param

if n * p_pop <= 10 and n * (1 - p_pop) <= 10:
    print("Deve haver ao menos 10 sucesos e 10 falhas no teste")
    raise

z_critical = stats.norm.ppf(alpha / 2)
z_critical = abs(z_critical)

SE = math.sqrt((p_pop*(1-p_pop))/n)

ci_upper = p_hat + SE
ci_lower = p_hat - SE

print("Intervalo de confiança para", 1 - alpha)
print("p_hat +- z*SE = ({:.3f},{:.3f})".format(ci_lower, ci_upper))

z_score = (p_hat - p_pop) / SE
p_value = stats.norm.pdf(z_score)

print("Testando Hipótese")
print("Ho: p_pop  =", p_pop)
print("Ha: p_pop !=", p_pop)

if p_value < alpha:
    print("Ho rejeitada")
else:
    print("Não foi possivel rejeitar Ho")

n_ideal = (pow(z_critical, 2) * p_hat * (1 - p_hat))/pow(alpha, 2)
n_ideal = int(n_ideal)

print("Número de Amostras Ideal")
print("Número usado:", n)
print("Número ideal:", n_ideal)

