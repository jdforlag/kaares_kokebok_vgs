import numpy as np

def g(x):
    return (np.e**(x-3)-1) / (2*x-6)

k = 1.0
while k > 0.001:
    a = k + 3
    print(f"x = {a:.10f}, g(x) = {g(a):.10f}")
    k = k / 2
