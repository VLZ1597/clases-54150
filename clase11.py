
# Link para entender composicion y agregacion
# https://www.seas.es/blog/informatica/agregacion-vs-composicion-en-diagramas-de-clases-uml/

# ================================================================================
# ================================================================================

# # Trabajando con variables podriamos guardar datos sueltos como los siguientes y mostrarlos
# nombre = 'Juan'
# edad = 26

# print(nombre)
# print(edad)

# # Pero para crear mas cantidad con lo que sabemos tendrimos un monton de variables
# # nombre y edad, ademas de que no se relacionan entre si mas que por algo que
# # pongamos en el nombre de la variable

# nombre1 = 'Juan'
# edad1 = 26
# nombre2 = 'Pepe'
# edad2 = 21

# print(nombre1)
# print(edad1)
# print(nombre2)
# print(edad2)

# # entonces podriamos usar diccionarios y agruparlos un poco mas
# persona1 = {
#     'nombre': 'Juan',
#     'edad': 26
# }
# persona2 = {
#     'nombre': 'Pepe',
#     'edad': 21
# }

# print(persona1['nombre'])
# print(persona1['edad'])
# print(persona2['nombre'])
# print(persona2['edad'])

# # Pero si tiene mas datos o tenemos que crear varias personas mas serian un monton
# # de lineas para cada persona. Y aca entra una clase (por lo menos un ejemplo
# # simple y basico de mejora en relacion a todo lo que nos brindan las clases)

# class Persona:
#     """
#     Esta es una clase donde se agregan todos los datos
#     respecto a una persona
#     """
#     def __init__(self, nombre, edad):
#         # Todo lo que definamos en __init__ se corre
#         # al crear una instancia de la clase
#         self.nombre = nombre
#         self.edad = edad

# #El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método.
# #Link de Interes: https://ejemplos.net/que-significa-self-en-python/

# #Creamos un objeto persona1 que es una instancia de la clase Persona
# persona1 = Persona("Juan", 26)

# #Vemos el tipo de objeto que es persona1
# type(persona1)

# # Y si queremos crear a Pepe solo hariamos lo siguiente
# persona2 = Persona("pepe", 21)

# # Para acceder a los datos cambia de como lo haciamos con dicc
# print(persona1.nombre) #Le pedimos a persona1 su nombre
# print(persona1.edad) #Le pedimos a persona1 su edad
# print(persona2.nombre) #Le pedimos a p2 su nombre
# print(persona2.edad) #Le pedimos a p2 su edad

# ================================================================================
# ================================================================================


# def nombre_de_funcion(param):
#     ...
    
# nombre_de_funcion('argumento')


# ================================================================================
# ================================================================================

# class NombreDeClase:
#     ...
    
# nombre_de_clase1 = NombreDeClase() # -> crea un objeto de NombreDeClase

# print(nombre_de_clase1)
# print(type(nombre_de_clase1))
# print(type(1))

# ================================================================================
# ================================================================================

# class Auto:
#     ...
    
# auto1 = Auto()
# auto2 = Auto()

# print(auto1)
# print(auto2)


# ================================================================================
# ================================================================================

# def asd():
#     ...

# class Auto:
    
#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!', self)
        
#     def avanzar(self, metros_a_avanzar):
#         print('El auto', self, 'avanzo', metros_a_avanzar, 'metros')


# auto1 = Auto()
# auto2 = Auto()

# print(auto1)
# print(auto2)
# auto1.tocar_bocina() # -> tocar_bocina(auto1)
# auto2.tocar_bocina() # -> tocar_bocina(auto2)
# auto1.avanzar(15) # -> tocar_bocina(auto1)
# auto2.avanzar(25) # -> tocar_bocina(auto2)

# ================================================================================
# ================================================================================

# class Auto:
    
#     def __init__(self, marca, modelo, color='Blanco'):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!', self)
        
#     def avanzar(self, metros_a_avanzar):
#         print('El auto', self, 'avanzo', metros_a_avanzar, 'metros')

#     # def guardar_fecha_fabricacion(self, fecha_fabricacion):
#     #     self.fecha_fabricacion = fecha_fabricacion


# auto1 = Auto('Ford', 'K', 'Rojo')
# auto2 = Auto('Fiat', 'Uno', 'Verde')
# auto3 = Auto('Renault', '18')

# print('Este es el auto 1', auto1)
# print(auto1.marca, auto1.modelo, auto1.color)

# print('Este es el auto 2', auto2)
# print(auto2.marca, auto2.modelo, auto2.color)

# print('Este es el auto 3', auto3)
# print(auto3.marca, auto3.modelo, auto3.color)

# # auto1.guardar_fecha_fabricacion('2024-05-07')
# print(auto1.fecha_fabricacion)

# print(auto2.fecha_fabricacion)

# ================================================================================
# ================================================================================

# class Auto:
    
#     cant_ruedas = 4
    
#     def __init__(self, marca, modelo, color='Blanco'):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         # self.cant_ruedas = 4
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!', self)
        
#     def avanzar(self, metros_a_avanzar):
#         print('El auto', self, 'avanzo', metros_a_avanzar, 'metros')

# auto1 = Auto('Ford', 'K', 'Rojo')
# auto2 = Auto('Fiat', 'Uno', 'Verde')
# auto3 = Auto('Renault', '18')

# # Auto.cant_ruedas = 5
# # auto1.cant_ruedas = 5
# # auto2.cant_ruedas = 5
# print(auto1.cant_ruedas)
# print(auto2.cant_ruedas)
# print(auto3.cant_ruedas)

# print(Auto.cant_ruedas)

# ================================================================================
# ================================================================================

# v1
# class Motor:
#     def __init__(self, cant_cilindros = 6):
#         self.cant_cilindros = cant_cilindros
        
# class Auto:
    
#     cant_ruedas = 4
    
#     def __init__(self, marca, modelo, color='Blanco', cant_cilindros=6):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.motor = Motor(cant_cilindros)
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!', self)
        
#     def avanzar(self, metros_a_avanzar):
#         print('El auto', self, 'avanzo', metros_a_avanzar, 'metros')


# auto1 = Auto('Ford', 'K', 'Rojo', 12)

# print(auto1.motor)
# print(auto1.motor.cant_cilindros)

# v2
# class Motor:
#     def __init__(self, n_serie, cant_cilindros = 6):
#         self.n_serie = n_serie
#         self.cant_cilindros = cant_cilindros
        
# class Auto:
    
#     cant_ruedas = 4
    
#     def __init__(self, marca, modelo, color='Blanco', **datos_de_motor):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.motor = Motor(**datos_de_motor) # -> Motor(n_serie=123456, cant_cilindros=12)
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!', self)
        
#     def avanzar(self, metros_a_avanzar):
#         print('El auto', self, 'avanzo', metros_a_avanzar, 'metros')


# auto1 = Auto('Ford', 'K', 'Rojo', n_serie=123456, cant_cilindros=12)

# print(auto1.motor)
# print(auto1.motor.n_serie)
# print(auto1.motor.cant_cilindros)


# ================================================================================
# ================================================================================

# class Motor:
#     def __init__(self, numero_serie, cant_cilindros = 6):
#         self.numero_serie = numero_serie
#         self.cant_cilindros = cant_cilindros
        
# class Auto:
    
#     cant_ruedas = 4
    
#     def __init__(self, marca, modelo, color='Blanco', **datos_de_motor):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.motor = Motor(**datos_de_motor) # -> Motor(n_serie=123456, cant_cilindros=12)
#         print(f'Se creo el auto {self}')
        
#     def __str__(self):
#         return f'Auto {self.marca} {self.modelo} de color {self.color}'
    
#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!', self)
        
#     def avanzar(self, metros_a_avanzar):
#         print('El auto', self, 'avanzo', metros_a_avanzar, 'metros')


# auto1 = Auto('Ford', 'K', 'Rojo', numero_serie=123456, cant_cilindros=12)

# print(auto1) # -> print(str(auto1)) 


# ================================================================================
# ================================================================================


# class Concesionaria:
    
#     def __init__(self, concesionaria):
#         self.concesionaria = concesionaria
#         self.autos = {}
        
#     def __str__(self):
#         return f'Listado de autos en la consecionaria "{self.concesionaria}"'
        
#     def __len__(self):
#         return len(self.autos)
    
#     def agregar_auto(self, auto):
#         if auto and auto.color.capitalize() == 'Negro':
#             self.autos.append(auto)
#         else:
#             print('Te falto el auto de color negro.')
        
#     def __getitem__(self, posicion):
#         try:
#             return self.autos[posicion]
#         except:
#             return 'No se encontro ese auto'
        
#     def __setitem__(self, posicion, nuevo_auto):
#         try:
#             if nuevo_auto.color == 'Negro':
#                 self.autos[posicion] = nuevo_auto
#             else:
#                 print('El auto no es negro.')
#         except:
#             print('No se pudo modificar el auto de la posicion {posicion}.')
        
#     def __iter__(self):
#         for auto in self.autos:
#             yield auto # <- queda en stand by, en espera

# concesionaria = Concesionaria('Pepito')

# print(concesionaria)
# print(len(concesionaria))
# auto1.color = 'Negro'
# # concesionaria.agregar_auto(auto1)
# concesionaria[0] = auto1
# print(concesionaria[0])
# print(concesionaria.autos)

# for valor in []:
#     ...
