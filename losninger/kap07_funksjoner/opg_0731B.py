import math

def vs(s):  # Venstresiden av likningen
    a = 7*s
    return a**2

def hs(s):  # Høyresiden av likningen
    grader = 60
    radianer = grader*2*math.pi / 360
    b = 3*s**2
    c = 5*s
    return b**2 + c**2 - 2*b*c*math.cos(radianer)

i = 0.01  # s-verdien du begynner søket med
steg = 0.0001

# For små s-verdier er venstresiden størst. Vi øker s til høyresiden har
# tatt igjen venstresiden. Da er likningen tilnærmet oppfylt.
while vs(i) > hs(i):
    i += steg

print(f"s = {i:.4f}")
print(f"Kontroll: venstresiden = {vs(i):.3f} og høyresiden = {hs(i):.3f}")
