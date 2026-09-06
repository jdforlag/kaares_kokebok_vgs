b = 3
k = 2
summ = 0

# Legger til nye ledd så lenge leddet er mindre enn 9999
while b < 9999:
    summ = summ + b
    b = b * k

print(f"Summen er {summ}")
