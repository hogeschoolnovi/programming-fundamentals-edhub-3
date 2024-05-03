# Opgave 1:
# Maak de lijst ‘getallen’ aan: getallen = [2, 4, 7, 11, 19]
# Voer de volgende opdrachten uit:
#     Voeg het getal 22 toe aan (het einde van) de lijst
#     Voeg het getal 6 toe tussen 4 en 7
#     Vervang het getal 4 door het getal 5

list = [2, 4, 7, 11, 19]
list.append(22)
list.insert(2, 6)
list[1] = 5
print(list)

# Opgave 2:
# In de Fibonacci rij bestaat elk getal uit de som van de twee voorgaande getallen: 1, 1, 2, 3, 5…
# De som van 1 en 1 is 2, de som van 1 en 2 is 3, enzovoorts. Implementeer de functie ‘fibon-acci’ die als
# parameter de lijst ‘fibonacci_reeks = [1, 1]’ krijgt aangeleverd, en een element toe-voegt aan de lijst,
# bestaande uit de vorige twee elementen. Roep de functie meerdere keren aan (Bijvoorbeeld met een for-loop).

#Mogelijke oplossing:
fibbonacci_reeks = [1, 1]
for i in range(10):
    a = fibbonacci_reeks[-1]
    b = fibbonacci_reeks[-2]
    c = a + b
    fibbonacci_reeks.append(c)
print(fibbonacci_reeks)

#Andere oplossing:
a = 1
b = 1
optie2 = [a, b]
for i in range(10):
    c = a + b
    a = b
    b = c
    optie2.append(c)
print(optie2)

# andere oplossing:
fibbonacci_reeks = [1, 1]
for i in range(10):
    fibbonacci_reeks.append(fibbonacci_reeks[-1] + fibbonacci_reeks[-2])
print(fibbonacci_reeks)

# Opgave 3:
# Maak een lijst ‘kwadraten’ die de kwadraten bevat van de getallen 1 tot en met 10. Gebruik een for loop.

kwadraten = []
for i in range(1, 11):
    kwadraten.append(i ** 2)
print(kwadraten)
