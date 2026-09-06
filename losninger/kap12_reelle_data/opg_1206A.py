kulepenner = [5, 2, 4, 1, 4]
dager = ["man", "tirs", "ons", "tors", "fre"]

# Vi begynner med å anta at mandag hadde færrest kulepenner
minste_antall = kulepenner[0]
minste_dag = dager[0]

for i in range(len(dager)):
    if kulepenner[i] < minste_antall:
        minste_antall = kulepenner[i]
        minste_dag = dager[i]

print(f"Det var færrest kulepenner på {minste_dag}dag.")
print(f"Da var det {minste_antall} kulepenner i skuffen.")
