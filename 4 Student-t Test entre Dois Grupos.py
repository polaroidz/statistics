# -*- coding: utf-8 -*-
import math
import numpy as np
import scipy.stats as stats

np.random.seed(seed=42)

# Requisitos
# 1. Os grupos devem ser independentes;
# 2. n < 10% da população;
# 3. A distribuição das amostras deve ser próxima da normal (checar skewness);

# Grupo A (Controle)
a_mean = 52.1 #@param
a_sd = 45.1 #@param
a_n = 22 #@param

# Grupo B (Experimento)
b_mean = 27.1 #@param
b_sd = 26.4 #@param
b_n = 22 #@param

# Parametros do Experimento
ci = 0.95 #@param
alpha = 1 - ci

power = 0.8 #@param

df = min(a_n - 1, b_n - 1)
t_df = stats.t.ppf(ci, df=df)

# Quando você junta dois dados aumenta a variabilidade geral
# por isso a soma, apesar de analisarmos a distribuição da diferença
SE = math.sqrt((pow(a_sd, 2) / a_n) + (pow(b_sd, 2) / b_n))

# Diferença entre os dois grupos
diff = a_mean - b_mean
diff = abs(diff)

print("Diferenca entre grupos, x_a - x_b =", diff)

ci_upper = diff + t_df * SE
ci_lower = diff - t_df * SE

print("Intervalo de confiança para", ci * 100)
print("(x_a - x_b) +- z*SE = ({:.3f},{:.3f})".format(ci_lower, ci_upper))

print("Testando Hipótese")
print("Ho: x_a - x_b  =", 0)
print("Ha: x_a - x_b !=", 0)

t_score = diff / SE
p_value = stats.norm.pdf(t_score)

print("t-score =", t_score)
print("p-value =", p_value)

if p_value < alpha:
    print("Ho rejeitada")
    print("A diferença entre os grupos não é fruto de mera chance")
else:
    print("Não foi possivel rejeitar Ho")
    print("A diferença entre os grupos não é significativa o suficiente")
    print("para afirmar que eles são grupos distintos")


# 0.05 pdf para dist t centralizada em 0 (Ho)
t_null = stats.t.ppf(ci, df=df)

se = diff / (t_null + t_score)

n_ideal = (pow(a_sd, 2) + pow(b_sd, 2)) / pow(se, 2)
n_ideal = int(n_ideal)

print("Número de Amostras Ideal")
print("Número usado:", df + 1)
print("Número ideal:", n_ideal)


