# =============== Guia Parte 1 ====================
# Actividad N°1
# Escribe un programa que le solicite al usario dos numeros
# enteros. Luego, muestre en pantalla la suma,resta,
# multiplicacion y divison de esos dos numeros.

n1 = int(input("Ingrese el 1er numero: "))
n2 = int(input("Ingrese el 2do numero: "))
suma = n1 + n2 
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2
print(f"El resultado de la suma de los  dos numeros ingresados es: {suma}")
print(f"El resultado de la resta de los  dos numeros ingresados es: {resta}")
print(f"El resultado de la multiplicación de los  dos numeros ingresados es: {multi}")
print(f"El resultado de la division de los  dos numeros ingresados es: {divi}")

# Actividad N°2
# Crea un programa que tome una cendena de texto como la entrada del user
# Luego, muestre en pantalla los primeros tres caracteres de la cadena ,seguidos
# por los últimos caracteres. Ademas, concatena ambos subconjuntos y muestra el resultado. 

texto = input("Ingresa una frase: ")
primeros = texto[:3]
ultimos = texto[-3:]
concatena = primeros + ultimos 
print(f"Los primeros tres caracteres son: {primeros}")
print(f"Los últimos tres caracteres son: {ultimos}")
print(f"La concatenación de ambos es: {concatena}")

# Actividad N°3
# Crea un programa que inicie con una lista de numeros enteros. Luego, solicita al User
# un numero entero y un indice para reemplazar un elemento  en la lista por el nuevo
# numero ingresado en el indice ingresado.
# Imprime la lista resultante

numeros = [1,2,3,4,5]
n_nuevo = int(input("Ingrese un numero nuevo: "))
indice = int(input("Ingrese un indice (0 al 4):"))

numeros[indice] = n_nuevo

print(f"Lista resultante {numeros}")

# Actividad N°4 
# Crea un programa que, teniendo en cuenta la siguiente tupla, muestre el valor
# del segundo elemento  de la misma . Ademas, debe mostrar cuantas veces se repite 
# este valor y cual es el indice del valor repetido.

palabras_tupla = ("manzana","pera","uva","naranja","sandia","manzana","platano","kiwi",
                  "pera","fresa","mango","uva","cereza","manzana","durazno")
segundo_elemento = palabras_tupla[5]
repeticiones = palabras_tupla.count(segundo_elemento)
indice = palabras_tupla.index(segundo_elemento,2)

print(f"El valor del segundo elemento es: {segundo_elemento}")
print(f"El valor se repite: {repeticiones}")
print(f"El indice es: {indice}")
