"""
Volem saber si una paraula és capicua:
entrada: “capicua”, sortida: no és capicua
entrada: “anna”, sortida: és capicua.
"""

#exemple pràctic 2 llistes
#maria nicolau jaume

print ("Digués una paraula:")
paraula = input()


x = len(paraula)-1
capicua = 1 
for i in range(len(paraula)):
  if paraula[i] != paraula[x]:
    capicua = 0
  x = x-1
if capicua == 1:
  print("Es capicua")
else:
  print("No es capicua")
  
print(capicua)
  
