inntekter = [3, 2, 1, 5, 3, 3, 8, 10, 7, 7, 4, 6]
sum_inntekter = 0
antall_minst5 = 0

for inntekt in inntekter:
    if inntekt >= 5:
        antall_minst5 += 1
    print(f"{inntekt} millioner kr")
    sum_inntekter += inntekt
    
print(sum_inntekter)
print(f"Det var {antall_minst5} måneder med minst 5 millioner kroner.")
