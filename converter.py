def number_to_words(n):
    """
    Konvertiert eine Ganzzahl n (0-100) in ihre deutsche Wortform.
    Args:
        n (int): Die zu konvertierende Zahl (zwischen 0 und 100).
    Returns:
        str: Die deutsche Wortform der Zahl.
    Raises:
        ValueError: Falls n nicht im Bereich [0, 100] liegt.
    """
    if not 0 <= n <= 100:
        raise ValueError("Nur Zahlen zwischen 0 und 100 sind erlaubt.")
  
    
    """Sonderfälle für 0 und 1"""
    if n == 0:
        return "null"
    
    if n == 1:
        return "eins"
    
    """Wortlisten für Einheiten und Zehner"""
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


