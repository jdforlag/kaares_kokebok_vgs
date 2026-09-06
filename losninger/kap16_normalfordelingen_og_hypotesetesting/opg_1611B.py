from scipy.stats import norm

a = float(input("Oppgi a: "))
b = float(input("Oppgi b: "))

# Kontrollerer at verdiene er gyldige
if a <= -5.0 or a >= 5.0:
    print("Ugyldig verdi. Du må ha -5 < a < 5.")
elif b <= a:
    print("Ugyldig verdi. Du må ha b > a.")
else:
    sanns = norm.cdf(b) - norm.cdf(a)
    print(f"P({a} < Z < {b}) = {sanns:.4f}")
