c = 4
summ = c  # Siden S_1 = c_1

for leddnr in range(1, 11):
    print(f"S{leddnr} = {summ}")  # Skriver ut den nåværende delsummen
    c *= 0.5
    summ += c  
