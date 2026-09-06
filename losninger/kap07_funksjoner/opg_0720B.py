def h(t):
    """Høyden til kanonkula i meter, t sekunder etter avfyring."""
    return -4.9*t**2 + 40*t + 1.2

steg = 0.001
t = 0

# Kula stiger helt fram til det høyeste punktet
while h(t) < h(t+steg):
    t += steg

print(f"Kanonkula var høyest etter {t:.2f} sekunder.")
print(f"Da var høyden {h(t):.2f} meter.")
