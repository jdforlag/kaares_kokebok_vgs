from scipy.stats import norm

mu = 500
sigma = 50
x = 600

z = (x - mu) / sigma
p_mindre = norm.cdf(z)
p_mer = 1 - p_mindre
svartekst = f"P(X>{600}) = P(Z>{z}) = {p_mer:.3f}"
print(svartekst)
