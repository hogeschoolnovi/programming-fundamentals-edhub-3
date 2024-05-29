#####################
# Voorbeeld opgave: #
#####################
# Maak een lijst `getallen` aan: `getallen = [10, 20, 30]`
#
# Voer de volgende opdrachten uit:
#
# - Voeg het getal 40 toe aan (het einde van) de lijst
# - Vervang het getal 10 door het getal 15
#
# Aan het einde print je de lijst `getallen`.


# list met getallen
getallen = [10, 20, 30]

# Voeg het getal 40 toe aan (het einde van) de lijst
getallen.append(40)
print('list na toevoeging 40 aan het einde van de lijst: ', getallen)  # Het resultaat is: [10, 20, 30, 40]

# Vervang het getal 10 door het getal 15
getallen[0] = 15
print('list na vervanging van 10 door 15: ', getallen)  # Het resultaat is: [15, 20, 30, 40]


#####################

# Opgave 1:
# Maak de lijst ‘getallen’ aan: getallen = [2, 4, 7, 11, 19]
# Voer de volgende opdrachten uit:
#     Voeg het getal 22 toe aan (het einde van) de lijst
#     Voeg het getal 6 toe tussen 4 en 7
#     Vervang het getal 4 door het getal 5

getallen = [2, 4, 7, 11, 19]

#     Voeg het getal 22 toe aan (het einde van) de lijst
getallen.append(22)
print('list na toevoeging 22 aan het einde van de lijst: ', getallen)  # Het resultaat is: [2, 4, 7, 11, 19, 22]

#     Voeg het getal 6 toe tussen 4 en 7
getallen.insert(2, 6)
print('list na toevoeging 6 tussen 4 en 7: ', getallen)  # Het resultaat is: [2, 4, 6, 7, 11, 19, 22]

#     Vervang het getal 4 door het getal 5
getallen[1] = 5
print('list na vervanging van 4 door 5: ', getallen)  # Het resultaat is: [2, 5, 6, 7, 11, 19, 22]

#####################

# Opgave 2:
# In de Fibonacci rij bestaat elk getal uit de som van de twee voorgaande getallen: 1, 1, 2, 3, 5, 8 enzovoorts
# De som van 1 en 1 is 2, de som van 1 en 2 is 3, enzovoorts. Implementeer de functie ‘fibonacci’ die een lijst als parameter meekrijgt.
# Maak een variabele aan genaamd 'fibonacci_start_reeks' en geef  die de eerste twee elementen van de Fibonacci reeks [1, 1].
# Maak een functie genaamd fibonacci die de fibonacci_reeks uitbreidt met een nieuw element.
# Roep de functie 5 keer aan (Bijvoorbeeld met een for-loop).
# Print de waarde van de fibonacci_reeks.
# Gewenste uitkomst:   [1, 1, 2, 3, 5, 8, 13]

fibonacci_reeks = [1, 1]


def fibonacci(fibonacci_reeks):
    fibonacci_reeks.append(fibonacci_reeks[-1] + fibonacci_reeks[-2])
    return fibonacci_reeks


for i in range(5):
    fibonacci(fibonacci_reeks)
    print(fibonacci_reeks)

print('fibonacci reeks: ', fibonacci_reeks) # Het resultaat is: [1, 1, 2, 3, 5, 8, 13]


#####################

# Opgave 3:
# Maak een lijst ‘kwadraten’ die de kwadraten bevat van de getallen 1 tot en met 10. Gebruik een for loop.
# Gewenste uitkomst:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

kwadraten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(kwadraten)):
    kwadraten[i] = kwadraten[i] ** 2


print('kwadraten: ', kwadraten) # Het resultaat is: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

