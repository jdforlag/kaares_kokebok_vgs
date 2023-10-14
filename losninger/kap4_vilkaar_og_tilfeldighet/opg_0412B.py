import random

tall = random.randint(50, 100)
print(f"Tallet er {tall}")

if 70 <= tall <= 90:
    print("Tallet er i intervallet [70, 90]")
else:
    print("Tallet er ikke i intervallet [70, 90]")