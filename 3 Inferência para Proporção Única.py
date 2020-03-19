# -*- coding: utf-8 -*-

import math

import numpy as np
import scipy.stats as stats

np.random.seed(seed=42)

p_hat = 0.25 #@param
p_pop = 0.50 #@param

alpha = 0.05 #@param

n = 24 #@param

if n * p_pop <= 10 and n * (1 - p_pop) <= 10:
    print("Deve haver ao menos 10 sucesos e 10 falhas no teste")
    raise

SE = math.sqrt((p_pop*(1-p_pop))/n)
z_score = (p_hat - p_pop) / SE

p_value = stats.norm.pdf(z_score)

print("Testando Hipótese")
print("Ho: p_pop  =", p_pop)
print("Ha: p_pop !=", p_pop)

if p_value < alpha:
    print("Ho rejeitada")
else:
    print("Não foi possivel rejeitar Ho")
