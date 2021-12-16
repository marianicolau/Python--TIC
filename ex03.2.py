"""
Escribe un programa que reciba un número del usuario e imprima si es positivo, negativo o cero. Utiliza la cadena if/elif/else apropiada, no vayas a emplear tres if consecutivos.
"""
#exercici 2 del capítol 03
#maria nicolau jaume

num = int(input("Digues un numero"))
if num > 0:
    print("Numero positiu")
elif num < 0:
    print("Numero negatiu")
else:
    print("Numero es igual a 0")
