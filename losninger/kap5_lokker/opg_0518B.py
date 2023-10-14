for i in range(9):
    resultat = 1
    print("1", end="")
    for j in range(2, i+3):
        print(f"*{j}", end="")
        resultat *= j
    print(f" = {resultat}")