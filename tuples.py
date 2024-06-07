# ==========================================
# Voorbeeld opdracht:
# Declareer twee tuples met de namen ‘tuple_een’ en ‘tuple_twee’.
# tuple_een krijgt de waarden 1, 2 en 3. tuple_twee krijgt de waarden 4, 5 en 6.
# Zorg dat je een tuple krijgt met de waarden 1, 2, 3, 4, 5 en 6. Onthoud dat tuples onveranderlijk zijn.
# ==========================================

tuple_een = (1, 2, 3)
tuple_twee = (4, 5, 6)

# je zal een nieuwe tuple variabele moeten declareren. De tuples die al gedeclareerd zijn kunnen niet worden aangepast
# (zoals een list kan worden aangepast met append, insert en remove).
combined_tuple = tuple_een + tuple_twee

print('combined tuple: ', combined_tuple)  # Het resultaat is: (1, 2, 3, 4, 5, 6



# ==========================================
# Opdracht 1:
# maak een tuple aan met de waarden 'b', 'c', 'a'
# print de waarden van de tuple in de juiste volgorde (a, b, c)
# maak gebruik van de indexen van de tuple
#
# Gewenste uitkomst:  a b c
# ==========================================

tuple_letters = ('b', 'c', 'a')

print('tuple letters in juiste volgorde: ', tuple_letters[2], tuple_letters[0], tuple_letters[1])  # Het resultaat is: a b c



# ==========================================
# Opdracht 2:
# Maak de lijst ‘getal_kwadraat_paar’ aan voor getallen 1 tot en met 5 waarin elk element bestaat uit een
# tuple die het getal en het bijbehorende kwadraat bevat. Gebruik een list comprehension.
#
# Gewenste uitkomst: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)
# ==========================================

getal_kwadraat_paar = [(i, i ** 2) for i in range(1, 6)]

print('getal kwadraat paar: ', getal_kwadraat_paar)  # Het resultaat is: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)



# =========================================
# Opdracht 3:
# Maak een tuple genaamd tuple_count met de waarden 1, 2, 3, 4, 5
# Zorg dat je een nieuwe tuple_countdown krijgt met de waarden 5, 4, 3, 2, 1
# Maak gebruik van de reversed() functie
#
# Gewenste uitkomst: (5, 4, 3, 2, 1)
# ==========================================

tuple_count = (1, 2, 3, 4, 5)
tuple_countdown = tuple(reversed(tuple_count))

print('tuple countdown: ', tuple_countdown)  # Het resultaat is: (5, 4, 3, 2, 1)



