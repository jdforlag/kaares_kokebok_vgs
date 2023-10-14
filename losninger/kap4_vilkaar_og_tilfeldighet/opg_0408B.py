import random

tall1 = random.randint(-5, 3)
tall2 = random.randint(-5, 3)

if tall1 == tall2:
    print(f"{tall1} og {tall2}, tallene er like")
else:
    print(f"{tall1} og {tall2}, ikke like")