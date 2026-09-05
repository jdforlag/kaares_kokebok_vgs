def f(x):
    return 4 - x

x_koord = int(input("Oppgi x: "))
y_koord = int(input("Oppgi y: "))
y_fasit = f(x_koord)  # y-verdien punktet må ha for å ligge på grafen

if y_koord == y_fasit:
    print("Punktet ligger på f.")
else:
    print("Punktet ligger ikke på f.")
