# 1. Zvětšovač
cislo = int(input("3: "))
cislo += 10
print(f"Výsledek je: {cislo}")

print()


# 2. Útrata v hospodě
ucet = float(input("750: "))
lidi = int(input("4: "))

na_osobu = ucet / lidi
print(f"Každý zaplatí: {na_osobu:.2f} Kč")

print()


# 3. Plocha kruhu
r = float(input("9: "))

plocha = 3.14 * r * r
print(f"Plocha kruhu je: {round(plocha)}")
