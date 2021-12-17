"""
Observa el siguiente código. Adivina lo que crees que producirá y escríbelo. Luego, ejecútalo y observa si estabas en lo cierto.
"""
#exercici 11 del capítol 03
#maria nicolau jaume
"""
Va comparant una sèrie de condicions, i a les solucions ens diu si aquestes són vertaderes o falses.
La primera es vertadera, perquè 3=3. La segona és falsa, perquè hi ha un espai innecessàri entre les comilles.
Les tercera i les cuarta són vertaderes, perquè 3 és més petit que 4 i 10.
La condició 5 és vertadera perquè la cadena 3 és més petita que la 4.
En canvi la condició 6 és falsa, perquè la cadena 3 és més gran que la 10.
La condició 7 és falsa perquè 2=2 és vertader, però no és igual a la cadena de vertader.
La condició 8 és vertadera, perquè 2=2 és vertader.
LA condició 9 és falsa, perquè el 3 no és més petit que la cadena de 3, sinó que són iguals.
"""
print("3" == "3")
print(" 3" == "3")
print(3 < 4)
print(3 < 10)
print("3" < "4")
print("3" < "10")
print( (2 == 2) == "True" )
print( (2 == 2) == True )
print(3 < int("3"))