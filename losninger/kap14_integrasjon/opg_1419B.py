def G(x):
    """Grensekostnaden i kroner per enhet ved produksjon av x enheter."""
    return 4*x + 160

a = 50
b = 120
n = 950
dx = (b - a) / n
kostnadsokning = 0

# Høyreorienterte rektangler: høyden leses av i høyre endepunkt.
# Derfor lar vi i gå fra 1 til og med n.
for i in range(1, n+1):
    x = a + i*dx
    kostnadsokning += G(x) * dx

print(f"Kostnadene øker med omtrent {kostnadsokning:.2f} kr per måned.")
