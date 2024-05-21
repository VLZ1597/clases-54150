'''
Un conjunto o SET, es una coleccion no ordenada de objetos unicos
se escribe usando llaves {} (para crear un set vacio se ulitiza set() 
de lo contrario creariamos un diccionario)
'''
# Un set puede convertise en una lista y viceversa
mi_lista = list({1,2,3,4})
mi_set = set(mi_lista)
print(type(mi_set))

'''
La funcion ADD permite agregar un nuevo item al set
se escribe mi_conjunto.add(item_a_agregar)
'''
num = {1,2,3,4}
num.add(5)
print(num)

'''
Para añadir multiples elementos a un set se usa la funcion UPDATE()
puede tomar argumentos en una lista, tupla,string,conjunto o cualquier 
objeto de tipo iterable.
La misma se escribe: mi_conjunto.update(item_a_agregar)
'''
num = {1,2,3,4}
num.update([5,6,7,8])
num.update(range(9,12))
print(num)

'''
La funcion DISCARD, hace lo contrario, elimina el ultimo item del set
se escribe: mi_conjunto.discard(item_a_descartar)
'''
num = {1,2,3,4}
num.discard(2)
print(num)

'''
La funcion remove, funciona igual que discard pero con una diferencia, 
en discard si el item a remover no existe, simplemente se ignora.
En remove en este cado nos indica un error
se escribe: mi_conjunto.remove(item_a_remover)
'''
num = {1,2,3,4}
num.remove(2)
# num.remove(5) en este caso me daria error por que no hay ningun 5

'''
IN se utiliza para determinar si un elemento pertenece a un set
se escribe: set_a_validar in mi_conjunto
'''
num = {1,2,3,4}
print(2 in num)
print(2 not in num)

'''
CLEAR se utiliza para borrar todos los valores de un set
se escribe: mi_conjunto.clear() 
'''
num = {1,2,3,4}
num.clear()
print(num)

'''
La funcion POP retorna un elemnto en forma aleatoria
'''
num = {1,2,3,4}
while num:
    print(f"Se está borrando: {num.pop()}")

'''
Los dict es una coleccion no oredenada de objetos
Para crear un diccionario se emplean las llaves {},
y sus pares clave-valor se separan por comas, a su vez intercalamos
la clave del valor con dos puntos(:)
'''
colores = {
    "amarillo":"yellow",
    "azul":"blue",
    "rojo":"red"
           }
print(type(colores))

'''
En los dict se utilizan las funciones ya mencionadas
(add,update,len,in y clear) y se agrega una nueva llamada
DEL , que elimina el item del dic , sin modificar el resto del dict
se escribe: mi_dict["clave"]
'''
num = {
    "uno":1,
    "dos":2,
    "tres":3,
    "cuatro":4
         }

del(num["dos"])
print(num)

















# colores = {"Rojo","Blanco","Azul"}
# # colores.add("Violeta")
# # colores.add("Dorado")
# colores.update({"Violeta","Dorado"})
# colores.discard("Dorado")
# colores.discard("Celeste")
# colores.discard("Blanco")
# print(colores)
# # Al utilizar el metodo discard, el codigo no se rompo
# # Si utilizo el metodo remove, el codigo se rompe
# print(type(colores))

# ganadores = {1990: 'Alemania',
#     1994: 'Brasil',
#     1998: 'Francia',
#     2002: 'Brasil',
#     2006: 'Italia',
#     2010: 'España',
#     2014: 'Alemania',
#     2018: 'Francia'}
# print(ganadores)

# animales = {"elefante": ""}
# animales.update({'perro':'bobby','tigre':'pepe','mono':'homero'})
# animales['elefante']= "Trompis"
# print(animales)
