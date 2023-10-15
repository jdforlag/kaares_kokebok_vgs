import random

kast1 = random.randint(1, 6)
kast2 = random.randint(1, 6)
print(kast1, kast2)

if kast1 == kast2:
    print("Like")
else:
    print("Ikke like")