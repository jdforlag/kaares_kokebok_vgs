import random

tall = random.randint(1, 6)
print(tall)

if tall == 6:
    print("Fantastisk! Du fikk en sekser!")
if tall < 5:
    print("Tallet er mindre enn 5.")
if tall > 2:
    print("Større enn 2.")
