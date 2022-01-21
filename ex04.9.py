"""
Lanzador de monedas: (4 pts)
- Crea un programa que imprima al azar 0 o 1.
- En lugar de 0 o 1, que imprima cara o cruz.
- Añádele un bucle para que lo haga 50 veces.
- Crea una suma acumulada para el total de veces que salió cara y las que salió cruz.
"""
#exercici 9 del capítol 04
#maria nicolau jaume

cara = 0
creu = 0

import random
for i in range(50):
    x = ["cara", "creu"]
    random_index = random.randrange(2)
    print(x[random_index])
    if x[random_index]== "cara":
        cara = cara + 1
    elif x[random_index] == "creu":
        creu += 1

print("Número de cares: ",cara)
print("Número de creus: ",creu)


