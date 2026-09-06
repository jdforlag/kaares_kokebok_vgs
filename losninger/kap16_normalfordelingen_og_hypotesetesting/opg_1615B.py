from scipy.stats import norm

mu = 500
sigma = 50

t = mu - 4*sigma

while True:
    p_mindre = norm.cdf(t, mu, sigma)
    p_storre = 1 - p_mindre

    # NB: P(X>t) synker når t øker. Vi starter langt til venstre, der
    # P(X>t) er nesten 1, og stopper når den har sunket ned til 0,758.
    if p_storre <= 0.758:
        break

    t += 0.1

print(f"t = {t:.1f}")
print(f"Kontroll: P(X > {t:.1f}) = {1 - norm.cdf(t, mu, sigma):.3f}")
