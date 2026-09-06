import numpy as np

verdier = [2, 4, 7]
sanns = [0.4, 0.1, 0.5]
mu = 4.7   # Forventningsverdien fra forrige oppgave

# Var(X) = (k1-mu)^2 * P(X=k1) + (k2-mu)^2 * P(X=k2) + ...
Var_X = 0
for i in range(len(verdier)):
    Var_X += (verdier[i] - mu)**2 * sanns[i]

SD_X = np.sqrt(Var_X)

print(f"Var(X) = {Var_X:.3f}")
print(f"SD(X) = {SD_X:.3f}")
