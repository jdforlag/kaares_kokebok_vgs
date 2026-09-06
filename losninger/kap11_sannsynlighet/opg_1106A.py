from numpy.random import choice

kjonn = ["jente", "gutt"]
sanns = [0.486, 0.514]
fodsler = choice(kjonn, p=sanns, size=150)

jenter = sum(fodsler == "jente")
gutter = sum(fodsler == "gutt")

print(f"Simuleringen gav {jenter} jenter og {gutter} gutter.")
