nombre = input("Ingrese un nombre: ")

print(nombre)

archivo_abierto = open('archivo_de_prueba.xml','w')

archivo_abierto.write(nombre)

archivo_abierto.close()

