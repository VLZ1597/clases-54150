# if <condicion>:
#     <bloque de codigo>
# elif <condicion>:
#     <bloque de codigo>
# elif <condicion>:
#     <bloque de codigo>
# elif <condicion>:
#     <bloque de codigo>
# elif <condicion>:
#     <bloque de codigo>
# elif <condicion>:
#     <bloque de codigo>
# else:
#     <bloque de codigo>

'''
Bucle WHILE (no sabes la cantidad) repite el codigo en base a una condicion logica, siempre que esta sea True
para que finalice tendremos que cambiar ese valor a false , de lo contrario seria un bucle infinito
'''

# num = 5
# while num > 0:
#     print(f'{num}')
#     num -=1




# sentencia <condicion>:
#     <bloque de codigo>

# while []: # -> bool([]) == False
# while [1,2,'pepe']: # -> bool([]) == True
    # <bloque de codigo>

# contador = 0
# while True:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)
    

# contador = 0
# while False:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)

# print('Ultima linea de mi proyecto')


# contador = 0
# dato_de_condicion = 2
# while dato_de_condicion > 0:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)
#     dato_de_condicion -= 1

# print('Ultima linea de mi proyecto')


# contador = 0
# dato_de_condicion = True
# while dato_de_condicion:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)
#     if contador == 15:
#         dato_de_condicion = False

# print('Ultima linea de mi proyecto')


# contador = 0
# dato_de_condicion = True
# while dato_de_condicion:
#     if contador == 15:
#         dato_de_condicion = False
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)

# print('Ultima linea de mi proyecto')

# contador = 0
# dato_de_condicion = 2
# while dato_de_condicion:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)
#     dato_de_condicion -= 1

# print('Ultima linea de mi proyecto')


# contador = 0
# dato_de_condicion = 0
# while dato_de_condicion:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)
#     dato_de_condicion -= 1
# else:
#     print('Pase por el else')

# print('Ultima linea de mi proyecto')


# pass

# if 2> 0:
#     pass
#     ...

# contador = 0
# dato_de_condicion = 0
# while dato_de_condicion:
#     contador += 1
#     ...
#     print('Estoy mostrando este mensaje numero:', contador)
#     dato_de_condicion -= 1
#     ...
# else:
#     print('Pase por el else')

# print('Ultima linea de mi proyecto')


# continue

# contador = 0
# while contador < 5:
#     contador += 1
#     if contador == 2:
#         continue
#     print('Estoy mostrando este mensaje numero:', contador)
# else:
#     print('Pase por el else')

# print('Ultima linea de mi proyecto')


# break

# contador = 0
# while contador < 5:
#     contador += 1
#     if contador < 2:
#         print('pepito')
#     else:
#         break
#     print('Estoy mostrando este mensaje numero:', contador)
# else:
#     print('Pase por el else')

# print('Ultima linea de mi proyecto')


# lista = [1,2,3,4,'pepito', True, ('eaea', 'pepe'), 'ochentoso']
# lista = []

# conjunto = {1,2,3,4,'pepito', True, ('eaea', 'pepe'), 'ochentoso'}

# print('La lista contiene el valor:', lista[0])
# print('La lista contiene el valor:', lista[1])
# print('La lista contiene el valor:', lista[2])
# print('La lista contiene el valor:', lista[3])
# print('La lista contiene el valor:', lista[4])
# print('La lista contiene el valor:', lista[5])
# print('La lista contiene el valor:', lista[6])

# indice = 0
# cant_de_elementos = len(lista)
# while indice < cant_de_elementos:
#     print('La lista contiene el valor:', lista[indice])
#     indice += 1


# for pepito in conjunto:
#     print('La lista contiene el valor:', pepito)


# for pepito in conjunto:
#     print('La lista contiene el valor:', pepito)

# print('Ultima linea de mi proyecto')



# diccionario = {
#     'marca': 'Ford',
#     'modelo': 'K',
#     'ruedas': 5,
# }

# # for algo in diccionario:
# for algo in diccionario.keys():
#     print('El diccionario contiene:', algo)
#     print(f'{algo}: {diccionario[algo]}')
    
# for algo in diccionario.values():
#     print('El diccionario contiene:', algo)
    
# for algo in diccionario.items():
#     print('El diccionario contiene:', algo)

# dato1, dato2 = ['elemento1', 'elemento2']

# # for variable1, variable2 in diccionario.items():
# #     print(f'{variable1}: {variable2}')
# for key, value in diccionario.items():
    # print(f'{key}: {value}')

# print(f'asdasd{2+2}asdasd')
# print('asdasdas{2+2}dasdad')


# lista = [1,2,3,4,'pepito', True, ('eaea', 'pepe'), 'ochentoso']
# for valor in lista:
#     if valor == 'pepito':
#         continue
#     if valor == ('eaea', 'pepe'):
#         break
#     pass
#     ...
#     print('La lista contiene el valor:', valor)
# else:
#     print('Mostre el else')
