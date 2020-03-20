# -*- coding: utf-8 -*-
import math
import numpy as np
import scipy.stats as stats

np.random.seed(seed=42)

# Condições:
# 1. Independencia
#   entre grupos
#   dentro dos grupos
# 2. Normalidade
# 3. A variancia entre os grupos 
#    deve ser semelhante

# Amostras
# (mean, n)
samples = [
    (5.07, 41),
    (7.0, 200),
    (6.76, 331)
] #@param

# Parametros do Experimento
ci = 0.95 #@param
alpha = 1 - ci

df_t = min(map(lambda e: e[1], samples)) - 1

k = len(samples) * (len(samples) - 1) / 2
df_k = k - 1

df_e = df_t - df_k

alpha_k = alpha / k


