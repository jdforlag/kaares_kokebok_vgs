import numpy as np
x = [1, 2, 3, 4]
y = [2, 5, 7, 10]
a, b = np.polyfit(x, y, 1)  # 1 betyr at vi vil ha en lineær modell

print(f"a = {a:.1f} og b = {b:.1f}")
print("Den lineære modellen er da:")

# Her er b negativ, derfor skriver vi minus foran og bruker abs(b)
print(f"f(x) = {a:.1f}x - {abs(b):.1f}")
