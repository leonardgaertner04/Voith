def number_to_words(n):
    """Konvertiert eine Zahl in ihre deutsche Wortform."""
    if n == 0:
        return "null"
    
    if n == 1:
        return "eins"
    
    units = ["", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
    teens = ["zehn", "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]
    tens = ["", "", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]

    words = []
    
    if n >= 100:
        words.append(units[n // 100] + "hundert")
        n %= 100
    
    if n >= 20:
        appendtens = tens[n // 10]
        n %= 10
    
    if n >= 10:
        words.append(teens[n - 10])
        n = 0
    
    if n > 0:
        words.append(units[n])
        if 'appendtens' in locals():
            words.append("und" + appendtens)
    elif n == 0 and len(words) == 0 and appendtens:
        words.append(appendtens)
    
    return ''.join(words)

def get_number():
    """Fragt den Benutzer nach einer gültigen Zahl."""
    zahl = input("Bitte gib eine Zahl ein: ")
    try:
        zahl = int(zahl)
    except ValueError:
        print("Es muss eine ganze Zahl eingegeben werden.")
        return get_number()
    if zahl < 0 or zahl > 100:
            print("Die Zahl muss zwischen 0 und 100 liegen.")
            return get_number()
    return zahl

zahl = get_number()
wort = number_to_words(zahl) 
print(f"Du hast die Zahl {wort} eingegeben.")
