# Opgave 1:
# Maak de lijst ‘getal_kwadraat_paar’ aan voor getallen 1 tot en met 5 waarin elk element bestaat uit een
# tuple die het getal en het bijbehorende kwadraat bevat. Gebruik een list comprehension.

getal_kwadraat_paar = []
for i in range(1, 6):
    getal_kwadraat_paar.append((i, i ** 2))
print(getal_kwadraat_paar)

# Opgave 2:
# Schrijf een dobbelspel voor een dobbelsteen met waardes 1 t/m 6. Als de speler 5 of 6 gooit,
# heeft hij gewonnen. Als hij 1 of 2 gooit, heeft hij verloren. Als hij 3 of 4 gooit, mag hij nog een keer gooien.
# Gebruik de random.randrange functie uit de module random voor de dobbelsteenwaarde. Hou de game status bij in een
# variabele die gecheckt wordt door een while loop. Gebruik if/elif waarde in tuple om te checken of een waarde
# gegooid is. Print de uitkomst.

import random

game_status = True
while game_status:
    dobbelsteen = random.randrange(1, 7)
    if dobbelsteen in (5, 6):
        print(f"Je hebt gewonnen met {dobbelsteen}")
        game_status = False
    elif dobbelsteen in (1, 2):
        print(f"Je hebt verloren met {dobbelsteen}")
        game_status = False
    elif dobbelsteen in (3, 4):
        print(f"Je mag nog een keer gooien met {dobbelsteen}")
    else:
        print(f"Er is iets fout gegaan met {dobbelsteen}")
        game_status = False

