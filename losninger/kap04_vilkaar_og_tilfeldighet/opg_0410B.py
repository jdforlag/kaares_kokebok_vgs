import random

er_sen = random.uniform(0, 100) < 40  # 40 % sannsynlighet
glemt_konfekt = random.uniform(0, 100) < 50  # 50 % sannsynlighet

if er_sen or glemt_konfekt:
    print("Lønnstrekk!")
else:
    print("Alt bra, ingen lønnstrekk")