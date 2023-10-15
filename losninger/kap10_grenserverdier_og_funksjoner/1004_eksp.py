import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return 100 * np.e ** (-0.012 * t)

t_verdier = np.arange(0, 168, 0.5)
plt.plot(t_verdier, f(t_verdier), label='Virkestoff over tid')

timer = 0
while f(timer) > 50:
    timer += 1

plt.axhline(y=50, color='black', linestyle='--', label='50 mg grense')
plt.plot(timer, f(timer), "o", label=f'Tidspunkt for 50 mg: {timer} timer')

plt.title('Mengde virkestoff i kroppen over tid')
plt.xlabel('Tid (timer)')
plt.ylabel('Mengde virkestoff (mg)')
plt.legend()
plt.grid()
plt.show()

dager = timer // 24
timer_rest = timer % 24
print(f"Det tar {dager} dager og {timer_rest:.1f} timer for virkestoffet å reduseres til 50 mg.")
