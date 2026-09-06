verdier = [0, 1, 2, 3]
sanns = [0.4, 0.3, 0.2, 0.1]

# E(X) = sum av x_i * P(X = x_i)
E_X = 0
for i in range(len(verdier)):
    E_X += verdier[i] * sanns[i]

print(f"E(X) = {E_X}")

# Var(X) = sum av (x_i - E(X))^2 * P(X = x_i)
Var_X = 0
for i in range(len(verdier)):
    Var_X += (verdier[i] - E_X)**2 * sanns[i]

print(f"Var(X) = {Var_X}")
