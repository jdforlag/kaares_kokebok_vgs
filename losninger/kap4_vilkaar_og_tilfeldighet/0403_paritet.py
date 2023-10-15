import random

tall = random.randint(10, 100)
deletall = random.randint(2, 10)
if tall % deletall == 0:
    print(f"{tall} er delelig med {deletall}")
else:
    print(f"{tall} er ikke delelig med {deletall}")
