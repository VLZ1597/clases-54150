# Strings

# Método upper()
'''
Esta funcion sirve para hacer que devuelva la misma cadena pero
con sus caracteres en mayusculas
'''
cadena1 = 'soY la pRimer cadena'
print(cadena1)
cadena1_en_mayusculas = cadena1.upper()

print(cadena1_en_mayusculas)

# Metodo lower()
'''
Esta funcion es util para convertir cadenas a minusculas
'''
cadena1 = 'soY la pRimer cadena'
print(cadena1)
cadena1_en_minusculas = cadena1.lower()
print(cadena1_en_minusculas)

# Metodo capitalize()
'''
Esta funcion sirve para hacer que devuelva la misma cadena pero con
su primer caracter en mayus y el resto de caracteres en minuscula
'''
cadena1 = 'soY la pRimer cadena'
print(cadena1.capitalize())

# Metodo title()
'''
Esta funcion sirve para hacer que se devuelva la misma cadena pero 
con el primer caracter de cada palabra en mayus y el resto en minus
'''
cadena1 = 'soY la pRimer cadena'
print(cadena1.title())

# Metodo count()
'''
Si necesitamos saber cuantas veces aparece una subcadena dentro 
de la misma cadena, usamos el metodo count()
'''
cadena1 = 'soY la pRimer cadena'
print(cadena1.count('a'))
print(cadena1.count(' '))
print(cadena1.count(''))

# Metodo find()
'''
Si necesitamos averiguar el indice en el que aparece una subcadena
dentro de la misma cadena, usamos el metodo find()
si no se encuentra en la cadena devuelve -1
'''
cadena1 = 'soY la pRimer cadena'
print(cadena1.find('a'))
print(cadena1.find(' '))
print(cadena1.find(''))
print(cadena1.find('z'))

# Metodo rfind()
'''
El metodo rfind() devuelve el indice, pero de la ultima occurrencia
de la subcadena, es decir, la ultima que aparece en la cadena
si no se encuentra en la cadena devuelve -1
'''
cadena1 = 'soY la pRimer cadena'
print(cadena1.rfind('a'))
print(cadena1.rfind(' '))
print(cadena1.rfind(''))
print(cadena1.rfind('z'))

# Metodo split()
'''
Esta funcion sirve para devolver una lista con la cedena de caracteres
separadas por cada indice de la lista
si no se indica alfuna cadena para separar, separa por espacios
'''
cadena2 = 'segunda cadena al rescate'
lista = ['segunda', 'cadena', 'al', 'rescate']
lista = cadena2.split()
print(lista)
lista2 = cadena2.split('a')
print(lista2)
lista3 = cadena2.split('a ')
print(lista3)
lista4 = cadena2.split('asd el pepe loco')
print(lista4)

# Metedo join()
'''
Esta funcion sirve para devolver una cadena separada a partir 
de una especie de separador
si no se especifica del separador devulve error
'''
lista = ['segunda', 'cadena', 'al', 'rescate']
tupla = ('segunda', 'cadena', 'al', 'rescate')
lista = ['segunda', 'cadena', 'al', 'rescate']
cadena = ' '.join(lista)
print(cadena)
cadena = '<><>pepito<>solito<><>'.join(lista)
print(cadena)
cadena = ' -=-=- '.join(tupla)
print(cadena)

# Metodo strip
'''
Sirve para devolver una cadena borrando todos los caracteres, de adelante 
y detras solamente, de la cadena especificados en la cadena de caracteres a
borrar que se le pasan entre parentesis a strip
si no se espeficiva el caracter elimina los espacios 
'''
# password = input('Ingrese un password: ')
# print(password.strip())
# print(password.strip('asd'))

# Metodo replace()
'''
Esta funcion sirve para devolver uan cadena remplazando los sub caracteres  indicados
'''
palabra_repetida = 'cadena pepito cadena cadena cadena'
palabra_repetida_1 = palabra_repetida.replace('a','O')
palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra', 3)
print(palabra_repetida)
print(palabra_repetida_1)
print(palabra_repetida_modificada)

# Lista

# lista = ['segunda', 'cadena', 'al', 'rescate']
# print(lista)
# lista.clear()
# print(lista)

# lista2 = lista + [1,2,3]
# print(lista2)
# lista += [1,2,3]
# print(lista)
# lista.extend([1,2,3])
# print(lista)

# lista = ['segunda', 'cadena', 'al', 'rescate']
# lista.insert(0, 'pepitoooooo')
# print(lista)

# lista = lista[::-1]
# lista.reverse()
# print(lista)



# lista_numeros = [5,1,2,3,4,10]
# # lista_numeros.sort()
# lista_numeros.sort(reverse=True)
# print(lista_numeros)


# lista_numeros1 = ['5','1','2','3','4','10']
# lista_numeros1.sort()
# # lista_numeros1.sort(reverse=True)
# print(lista_numeros1)


# Sets


# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor1', (1, True))
# # el primero tiene que ser un set... el segundo un iterable
# print(conjunto1.isdisjoint(iterable1))
# iterable2 = (2, 'valor2', (2, True))
# print(conjunto1.isdisjoint(iterable2))
# iterable2 = (1, 'valor2', (2, True))
# print(conjunto1.isdisjoint(iterable2))



# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor1', (1, True), 45)
# print(conjunto1.issubset(iterable1))


# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor1', (1, True), 45)
# print(conjunto1.issuperset(iterable1))



# conjunto1 = {1, 'valor1', (1, True)}
# # iterable1 = (1, 'valor2', (2, True), 45)
# iterable1 = (2, 'valor2', (2, True), 45)
# conjunto3 = conjunto1.union(iterable1)
# print(conjunto1)
# print(conjunto3)


# conjunto1 = {1, 'valor1', (1, True)}
# # iterable1 = (2, 'valor2', (2, True), 45)
# iterable1 = (2, 'valor2', (1, True), 45)
# print(conjunto1.difference(iterable1))
# print(conjunto1)


# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# print(conjunto1.intersection(iterable1))
# variable = conjunto1.intersection(iterable1)
# print(conjunto1)



# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# conjunto1.difference_update(iterable1)
# print(conjunto1)


# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# conjunto1.intersection_update(iterable1)
# print(conjunto1)

    
    


# Dicts

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# valor1 = auto['motor']
# print(valor1)
# # valor2 = auto['ricardo']
# # print(valor2)
# valor3 = auto.get('ricardo', False)
# print(valor3)


# print(auto.keys())
# print(auto.values())
# print(auto.items())