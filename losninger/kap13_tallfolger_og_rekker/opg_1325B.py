# 0,999... = 0,9 + 0,9*0,1 + 0,9*0,1**2 + ...
# Dette er en geometrisk rekke med a1 = 0,9 og k = 0,1

a = 0.9
k = 0.1
S = 0

for i in range(20):
    S = S + a
    a = a * k
    print(S)

# Delsummene nærmer seg 1. Ved regning:
#     S = a1 / (1 - k) = 0,9 / 0,9 = 1
print(f"Summen av den uendelige rekka er {0.9 / (1 - 0.1)}")
