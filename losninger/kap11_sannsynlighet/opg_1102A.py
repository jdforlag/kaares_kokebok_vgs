from numpy.random import randint

kastene = randint(1, 7, size=200)
seksere = sum(kastene == 6)
enere = sum(kastene == 1)

print("200 terningkast gav:")
print(f"{seksere} seksere")
print(f"{enere} enere")
