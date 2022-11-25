"""print('😊 hi')
print('😘 Hello world')"""

# Consultar el tipo de dato.
"""print(type("Hola python")) # Tipo 'str'
print(type(12)) # Tipo 'int'
print(type(1.2)) # Tipo 'float'
print(type(True)) # Tipo 'bool'"""




# Introducir información el usuario e imprimirlo por consola 
"""age = int(input('what\'s your age: '))
print(age)"""

"""a = int(input('Introduce el valor de a: '))
b = int(input('Introduce el valor de b: '))
c = int(input('Introduce el valor de c: '))

root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(root1)
print(root2)"""

# Cambio de divisa
"""currency_yuan = int(input('What do you have left in yuan? '))
currency_yen = int(input('What do you have left in yen? '))
currency_won = int(input('What do you have left in won? '))

total = currency_yuan * 0.15 + currency_yen * 0.0077 + currency_won * 0.00080

print(total)"""

#Condiciones

import random

num = random.randint(0, 1)   # RNGesus will give us a random number that is either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')

# Condición de un boolenao
"""hello = True

if hello:
    print("Hola Python")
else :
    print("Probando condiciones")
""" 