"""
Observa el siguiente código. Adivina lo que crees que producirá y escríbelo. Luego, ejecútalo y compara el resultado con tu suposición. Señala claramente tu suposición y la respuesta correcta. Aunque no tengas que explicarlo, asegúrate de entender el por qué el ordenador ha imprimido eso. Que no te vaya a pillar desprevenido esto en el futuro.
"""
#exercici 9 del capítol 03
#maria nicolau jaume
"""
Aquest programa ens diu que x=5. 
Després x=y=6 però no es vera, perquè ens diu que x=5, per tant,no pot ser que x=6.
Seguidament diu que z=x=5 i és vera, perquè al principi diu que x=5.
Per tant, per això surt buzz.  
"""
x = 5
y = x == 6
z = x == 5
print("x=", x)
print("y=", y)
print("z=", z)
if y:
    print ("Fizz")
if z:
    print ("Buzz")
