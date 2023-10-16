from scipy.stats import norm

# Initialiserer variabler
ex = 150
sd = 10
print(f"X er normalfordelt med E(X)={ex} og SD(X)={sd}.")

# Ber brukeren om en x-verdi og beregner den tilhørende z-verdien
x = float(input("Oppgi en x-verdi: "))
z = (x - ex) / sd
print(f"z = {z:.3f}")

# Beregner P(Z <= z)
p_mindre = norm.cdf(z)
print(f"P(X <= {x}) = P(Z <= {z:.3f}) = {p_mindre:.3f}")

# Beregner P(Z > z) basert på P(Z <= z)
p_storre = 1 - p_mindre
print(f"P(X > {x}) = P(Z > {z:.3f}) = {p_storre:.3f}")

# Spør brukeren om å angi intervallverdier a og b
a = float(input("Skriv inn verdien til a (a < b): "))
b = float(input("Skriv inn verdien til b (b > a): "))

z_a = (a - ex) / sd
z_b = (b - ex) / sd

# Beregner sannsynligheten P(a < X < b)
p_mellom = norm.cdf(z_b) - norm.cdf(z_a)
print(f"P({a} < X < {b}) = P({z_a:.3f} < Z < {z_b:.3f}) = {p_mellom:.3f}")
