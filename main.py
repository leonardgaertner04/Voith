from converter import number_to_words 

def get_number():
    """Fragt den Benutzer nach einer gültigen Zahl."""
    zahl = input("Bitte gib eine Zahl ein: ")
    
    """Überprüft auf ganze Zahlen und den definierten Bereich."""
    while True:
        try:
            zahl = int(zahl)
            if 0 <= zahl <= 100:
                break
            else:
                print("Die Zahl muss zwischen 0 und 100 liegen.")
        except ValueError:
            print("Es muss eine ganze Zahl eingegeben werden.")
        zahl = input("Bitte gib eine Zahl ein: ")
    return zahl

zahl = get_number()
wort = number_to_words(zahl) 
print(f"Du hast die Zahl {wort} eingegeben.")