from scipy.stats import norm

z1 = -0.5
z2 = 1.0

mindre = norm.cdf(z1)
print(f"P(Z<={z1}) = {mindre:.4f}")

storre = 1 - mindre
print(f"P(Z>{z1}) = {storre:.4f}")

mellom = norm.cdf(z2) - norm.cdf(z1)
print(f"P({z1}<Z<{z2}) = {mellom:.4f}")
