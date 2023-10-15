import random

tid = random.uniform(0, 4)  # Parkeringstid i timer

print(f"Du parkerte i {tid:.2f} timer")

if tid < 1:
    print("10 kr i P-avgift")
elif tid < 2:
    print("19 kr i P-avgift")
elif tid < 3:
    print("28 kr i P-avgift")
else:
    print("100 kr i P-avgift")
