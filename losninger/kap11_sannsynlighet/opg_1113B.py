from numpy.random import binomial

p = 0.90
plukket = 1200
spiselige = binomial(plukket, p)
kastes = plukket - spiselige

print(f"Petter plukket {plukket} poteter.")
print(f"{spiselige} av dem var spiselige.")
print(f"{kastes} poteter måtte kastes.")
