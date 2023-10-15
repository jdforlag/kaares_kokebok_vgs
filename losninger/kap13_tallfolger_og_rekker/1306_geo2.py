def a(n):
    return 2 * 3 ** (n - 1)

summ = 0
i = 1  # Starter fra a_1
# a1+a3+a5+...+1062882
while a(i) <= 1_062_882:
    summ += a(i)  
    i += 2

print(f"Summen er {summ}")
