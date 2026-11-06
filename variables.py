# Prijzen van producten
appel_prijs = 1.50
brood_prijs = 2.25
melk_prijs = 1.80

# Aantal verkochte producten
aantal_appels = 10
aantal_broden = 5
aantal_melk = 8

# Bereken de omzet
totale_omzet = (
    appel_prijs * aantal_appels
    + brood_prijs * aantal_broden
    + melk_prijs * aantal_melk
)

# Print de resultaten
print("Appels:", appel_prijs, aantal_appels)
print("Brood:", brood_prijs, aantal_broden)
print("Melk:", melk_prijs, aantal_melk)

print("Totale omzet:", totale_omzet)
