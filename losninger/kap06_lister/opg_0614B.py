import random
import time

reaksjonstider = []

for _ in range(3):
    print("Trykk Enter så snart du ser teksten Beep...")
    time.sleep(random.uniform(2, 4))
    print("Beep")
    tid_start = time.time()
    input()  # Waiting for the user to press Enter
    tid_slutt = time.time()
    reaksjonstid = tid_slutt - tid_start
    reaksjonstider.append(reaksjonstid)

print(f"Laveste reaksjonstid: {min(reaksjonstider):.3f} sekunder.")
