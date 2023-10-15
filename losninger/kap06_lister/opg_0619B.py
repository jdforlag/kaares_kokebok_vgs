print("Oppgi sidene i en trekant slik: 3 4 5")
sider = input().split(" ")  # A list with the sides as strings

# Converting text to integers
for i in range(len(sider)):
    sider[i] = int(sider[i])

# Finding the largest side
c = max(sider)

# Removing the largest side from the list
sider.remove(c)

# Extracting and removing the remaining sides
b = sider.pop()
a = sider.pop()

# Checking if the triangle is right-angled
if a**2 + b**2 == c**2:
    print("Trekanten er rettvinklet.")
else:
    print("Trekanten er ikke rettvinklet.")
