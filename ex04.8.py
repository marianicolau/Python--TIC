"""
Escribe un programa en Python que:
- Le pida al usuario siete números
- Imprima la suma total de esos números
- Imprima la cuenta de las entradas positivas, las que sean iguales a cero, y las negativas. Emplea una cadena if, elif, else, en lugar de tres if consecutivos
"""
#exercici 8 del capítol 04
#maria nicolau jaume

total = 0
 
for i in range(7):
    x = int(input("Digués 1 número"))
num = total + x 
print("El total es:", num)
if x > 0:
    print("La suma dels números positius és:", num)
elif x < 0:
    print("La suma dels números negatius a zero és:", num)
else:
    print("La suma dels números igual a zero és:", num)
