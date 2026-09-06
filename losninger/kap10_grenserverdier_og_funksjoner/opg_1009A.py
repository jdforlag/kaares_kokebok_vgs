def f(x):
    return -0.2*x**2 + 100*x - 6500

def fd(x):  # Numerisk derivert av f(x)
    h = 0.001
    return (f(x+h)-f(x)) / h

varer = int(input("Oppgi antall varer (0-500): "))

# Er den deriverte positiv, vokser overskuddet, og bedriften bør produsere mer
if fd(varer) > 0:
    print("Overskuddet vokser. Bedriften bør øke produksjonen.")
elif fd(varer) < 0:
    print("Overskuddet minker. Bedriften bør minke produksjonen.")
else:
    print("Bedriften har allerede den produksjonen som gir størst overskudd.")

# NB: Den numeriske deriverte blir nesten aldri nøyaktig 0. Toppunktet ligger
# i x = 250, men fd(250) gir -0.0002, så siste gren brukes i praksis ikke.
