sparebelop = 4600
saldo = 0
mnd = 0
while saldo < 250_000:
    saldo = saldo + sparebelop
    mnd += 1
aar = mnd // 12
rest_mnd = mnd % 12
print("Antall år:", aar)
print("Antall måneder:", rest_mnd)
