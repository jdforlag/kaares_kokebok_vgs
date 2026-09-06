innskudd = 5000
k = 1 + 0.002
saldo = 0

# Mønsteret gjentas 24 ganger: saldoen vokser med renta, og deretter
# settes et nytt beløp inn.
for i in range(24):
    saldo = saldo * k + innskudd

print(f"Like etter det 24. innskuddet har Camilla {saldo:.2f} kr.")
