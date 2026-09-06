from scipy.stats import hypergeom

# 800 griser, 250 slakteklare, trekker 100
# P(X = 30) regnes da ut slik
p = hypergeom.pmf(30, 800, 250, 100)
print(p)

# P(X > 30) er det motsatte av P(X <= 30)
p_over_30 = 1 - hypergeom.cdf(30, 800, 250, 100)
print(f"P(X > 30) = {p_over_30:.4f}")
