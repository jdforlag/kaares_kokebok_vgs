timelonn = [120, 130, 110, 115, 115, 180]
timer = [6, 5, 4, 4, 5, 9]
total_inntekt = sum([timelonn[i] * timer[i] for i in range(len(timelonn))])
print(f"Total inntekt for uken er {total_inntekt} kroner.")
