A = [10]  # 10 kroner i startpris
B = [5]

t = 0  # Time in minutes
while A[t] >= B[t]:
    t += 1
    A.append(A[t-1] + 3)
    if t <= 10:
        B.append(B[t-1] + 1.5)
    else:  # t > 10
        B.append(B[t-1] + 4)

print(f"Hun må sykle i minst {t} minutter.")
