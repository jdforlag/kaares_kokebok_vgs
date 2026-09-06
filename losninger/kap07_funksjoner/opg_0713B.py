def g(x):
    return x - 5

a = -1

# g(-1) er negativ, og g vokser. Vi øker a til g(a) ikke lenger er negativ
while g(a) < 0:
    a += 1

print(a)
print(f"Nullpunktet er x = {a}")
