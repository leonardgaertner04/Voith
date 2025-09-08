zahl = input("Bitte gib eine Zahl ein: ")
try:
    zahl = float(zahl)
    print(f"Du hast die Zahl {zahl} eingegeben.")
except ValueError:
    print("Das war keine gültige Zahl.")