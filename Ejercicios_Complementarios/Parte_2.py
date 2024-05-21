# =============== Guia Parte 2 ==================
# Actividad N°1 

# Crea un programa que solicite al user ingresar nombres separados por
# comas. Luego, crea un conjunto con los nombres ingresados y muestra 
# por pantalla la cantidad de nombres unicos en el conjunto

nombres = input("Ingrese nombres separados por comas: ")
conjuntos_nombres = set(nombres.split(","))
cantidad =  len(conjuntos_nombres)
print(f"La cantidad de nombres unicos: {cantidad}")

# Actividad N°2 
# Crea un programa que simule un inventario de productos
# en una tienda. Inicia con un dict que conetenga algunos productos
# y sus cantidades. Luego, permite que el user agregue un nuevo 
# producto con su cantidad y actualizar la cantidad de un producto
# existente. Muestra el inventario actualizado

inventario = {
    "Manzana": 50,
    "Bananas": 30,
    "Peras": 40,
} 

nuevo_producto = input("Ingresa un nuevo producto: ")
cantidad_producto = int(input(f"Ingresa la cantidad de {nuevo_producto}: "))
inventario[nuevo_producto] = cantidad_producto

producto_existente = input("Ingresa un producto existente: ")
nueva_cantidad = int(input(f"Ingresa la cantidad de {producto_existente}: "))
inventario[producto_existente] = nueva_cantidad

print(f"Inventario actualizado:{inventario} ")

# Actividad N°3
# Cree un programa que tome una oracion ingresada por el user
# y realice las siguinetes operaciones:
# convierte la oreacion a mayusculas, cuenta cuantas 
# veces aparece la palabra "python", y muestra  la oracion sin espacios
# en blanco al inicio y al final.

oracion = input("Ingrese una oracion: ") 
mayus = oracion.upper()
contador = oracion.count("python")
oracion_sin_espacios = oracion.strip()

print(f"Oracion en mayus: {mayus}")
print(f"Contador de pythons: {contador}")
print(f"Oracion sin espacios: {oracion_sin_espacios}")

# Actividad N°4
# Crea dos conjuntos con números ingresados por el usuario separados por coma.
# Luego, muestra cuales elementos tienen en común los conjuntos 
# y crea un nuevo conjunto que contenga la unión de ambos conjuntos.

numeros1 = set(input("Ingresa números para el primer conjunto: ").split(","))
numeros2 = set(input("Ingresa números para el segundo conjunto: ").split(","))
tienen_elementos_comunes = numeros1.isdisjoint(numeros2)
union_conjuntos = numeros1.union(numeros2)

print(f"¿Que elementos tienen en común? {tienen_elementos_comunes}")
print(f"Unión de conjuntos: {union_conjuntos}")


 
