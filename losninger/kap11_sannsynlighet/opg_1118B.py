from numpy.random import binomial

forsok = 2000
gutter = 7
jenter = 5
p = 0.74
gunstige = 0

for i in range(forsok):
    gutter_bestatt = binomial(gutter, p)
    jenter_bestatt = binomial(jenter, p)
    if gutter_bestatt == 5 and jenter_bestatt == 4:
        gunstige += 1

print(f"P(5 gutter og 4 jenter består) er omtrent {gunstige/forsok:.4f}")
