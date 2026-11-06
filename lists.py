# Maak een boodschappenlijst
boodschappen = ["Brood", "Melk", "Appels", "Kaas", "Eieren","bananen","Yoghurt"]

# Voeg twee producten toe
boodschappen.append("Bananen")
boodschappen.append("Yoghurt")

# Verwijder één product
boodschappen.remove("Kaas")

# Controleer of melk op de lijst staat
if "Melk" in boodschappen:
    print("Melk staat op de lijst!")

# Print het aantal producten
print("Aantal producten:", len(boodschappen))

# Print de volledige boodschappenlijst
print("Boodschappenlijst:", boodschappen)
