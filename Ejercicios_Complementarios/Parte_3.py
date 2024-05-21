# =============== Guia Parte 3 ==================
# Actividad N°1
# Crea un programa que solicite dos números enteros al usuario y determine si ambos son números pares.

# n1 = int(input("Ingrese el 1er num: "))
# n2 = int(input("Ingrese el 2do num: "))
# if n1 %2 == 0 and n2 %2 == 0:
#     print("Los numeros son pares") 
# else:
#     print("Cara de verga")
    
# Actividad N°2
# Escribe un programa que tome un número entero ingresado por el usuario 
# y determine si es un número par, divisible por 3 y 5 al mismo tiempo, 
# o ninguno de los anteriores 

# n1 = int(input("Ingrese su num: "))
# if n1 %2 == 0:
#     if n1 %3 == 0 and n1 %5 == 0:
#         print("El numero es par y divisible por 3 y 5")
#     else:
#         print("El numero es par pero no es divisible por 3 y 5")
# else:
#     print("El numero no es par")


# Actividad N°3
# Cree un programa que solicite un numero entero al user y
# determine si es un numero negativo, positivo o igual a cero.
# En caso de ser positivo , verifica si es par o impar.

# n1 = int(input("Ingrese su num: "))
# if n1 > 0:
#     if n1 %2 == 0:
#         print("El numero es positivo y par")
#     elif n1 %2 == 1:
#         print("El numero es positivo e impar")
# elif n1 < 0:
#     print("Es negativo")
# elif n1 == 0:
#     print("Es cero")
 
# Actividad N°4
# Escribe un programa que tome un numero positivo entero
# ingresado por el user y muestre "Es positivo" si el numero
# es mayor que cero, de lo contrario , muestra "No es positivo"

# n1 = int(input("Ingrese su num: "))
# resultado = "Es positivo" if n1 > 0 else "No es positivo"
# print(resultado)