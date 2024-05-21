'''
Las LISTAS en otros lenguajes tienen como restriccion que permite tener un solo tipo 
de dato. Pero en python, no tenemos esa restriccion. Son mutables
Podemos tener uan lista heterogenea que contenga nums, vars,strings, o incluso otras listas.
se declara usando corchetes
'''
datos = [1,-5,123,34,"Una cadena", "Otra cadena","Pepito"]
print(datos[0])
print(datos[-1])
print(datos[-2:]) # Utiliza slicing para ello se usa la notacion [inicio:fin:paso]

'''
La funcion APPEND permite agregar un nuevo item al final de una lista, se escibe,
mi_lista.append(elemento)
'''
num = [1,2,3,4,]
num.append(5)
print(num)

'''
Tambien se puede saber la longitud haciendo...
'''
num = [1,2,3,4,]
longitud = len(num)
print(longitud)

'''
La funcion POP hace lo contrario que APPEND, elimina el ultimo item de una lista
'''
num = [1,2,3,4,]
num.pop()
print(num)

'''
Las listas pueden utilizar la funcion COUNT, esta funcion fuenta el num de veces
que se repite un elemento en una lista
'''
num = [1,2,1,3,1,4,1]
print(num.count(1))

'''
Las listas pueden utiliar la funcion INDEX, esta funcion busca un elemento y nos dice
en que indice se encuentra
'''
num = [1,2,1,3,1,4,1,5]
print(num.index(5))

'''
Las TUPLAS son colecciones de datos que son inmutables
se declara utilizando parentesis
'''
mi_tupla = (1,2,3,4)
otra_tupla = ("Hola"," "," ","¿","como", "estas", "?")
tupla_valor_unico = (2,)
print(mi_tupla)
print(otra_tupla)
print(tupla_valor_unico)

'''
Las tuplas no contienen la funcion append(), pero puedes agregar elementos con las tecnica
de concatenacion
'''
num = (1,2,3,4)
num += (5,6,7,8)
print(num)
