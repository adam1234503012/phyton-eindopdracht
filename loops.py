# Gegevens van het monster
monster_health = 150
player_damage = 25
aantal_aanvallen = 0

# Val het monster aan
while monster_health > 0:
    monster_health = monster_health - player_damage
    aantal_aanvallen = aantal_aanvallen + 1

    if monster_health < 0:
        monster_health = 0

    print("Monster health:", monster_health)

print("Monster verslagen!")
print("Aantal aanvallen:", aantal_aanvallen)

# Bonus: drie verschillende monsters
monsters = [100, 150, 200]

for health in monsters:
    aanvallen = 0

    while health > 0:
        health = health - player_damage
        aanvallen = aanvallen + 1

        if health < 0:
            health = 0

    print("Monster verslagen in", aanvallen, "aanvallen!")
