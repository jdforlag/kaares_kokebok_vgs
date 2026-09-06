# Forklaring:
# Eleven regner ut summen av en aritmetisk rekke. Det første leddet er a = 3,
# og differansen er d = 4. Rekka er altså 3 + 7 + 11 + 15 + ...
# Løkka legger sammen N ledd, og skriver til slutt ut summen.
# Med N = 10 blir svaret S_10 = 210.
#
# Forutsigelse for N = 100:
# Vi bruker summeformelen for en aritmetisk rekke:
#     S_n = (n/2) * (2*a1 + (n-1)*d)
#     S_100 = 50 * (2*3 + 99*4) = 50 * 402 = 20100

a = 3
d = 4
N = 100  # Endret fra 10
S = 0

for i in range(N):
    S = S + a
    a = a + d

print(S)
