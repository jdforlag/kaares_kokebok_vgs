a = 450
k = 4/5
summ = 0
antall_ledd = 0

# Vi tar bare med leddene som er større enn 1
while a > 1:
    summ = summ + a
    a = a * k
    antall_ledd += 1

print(f"Vi tok med {antall_ledd} ledd.")
print(f"Summen er {summ:.2f}")

# Til sammenligning er summen av hele den uendelige rekka
#     a1 / (1 - k) = 450 / 0,2 = 2250
