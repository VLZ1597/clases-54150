# =============== Guia Parte 4 ====================
# Actividad N°1
# escribe un programa que tome un numero entero positivo
# ingresado por el user y muestre la tabla de multiplicar
# de ese numero. Repite la solicitud al ingresar un nuevo 
# numero hasta que ingrese 0

# while True:
#     numero = int(input("Ingrese un numero positivo (o uno negativo para salir): "))
#     if numero == 0:
#         break
#     for i in range(1,11):
#         resultado=numero*i
#         print(f"{numero} x {i} = {resultado}")

# Actividad N°2
# Escribe un programa que tome una lista de nombres ingresados
# por el user separados por un espacio y lo liste mostrando su ubi

# nombres = input("Ingrese nombres separados: ").split()
# for i,nombre in enumerate(nombres):
#     print(f"Nombre {i + 1}: {nombre}")

# Actividad N°3
# Crea un progama que solicite al user ingresar una palabra.
# Luego, recorre la palabra y cuenta cuantas vocales contiene.
# Al final, si no se encontraron vocales, muestra un mensaje comunicando 
# que la palabra ingresada solo contiene cosonantes.

# palabra = input("Ingresa una palabra: ")
# vocales = "aeiou"
# contador = 0

# for i in palabra:
#     if i in vocales:
#         contador += 1

# else:
#     if contador == 0:
#         print("La palabra no tiene vocales")
#     else:
#         print(F"La palabra tiene {contador} vocales")

    


        