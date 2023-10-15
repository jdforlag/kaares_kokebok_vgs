import time

tid_start = time.time_ns()
naturlige_tall = list(range(1, 10**6 + 1))
summen = sum(naturlige_tall)
tid_slutt = time.time_ns()

nanosekunder = tid_slutt - tid_start
millisekunder = nanosekunder / 1e6

print(f"Summen er {summen}")
print(f"Tid i nanosekunder: {nanosekunder}")
print(f"Tid i millisekunder: {millisekunder}")
