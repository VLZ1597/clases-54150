def registro_user(database):
    nombre_user = input("Ingrese su nombre de usuario: ")
    while True:
        contraseña = input("Ingrese su contraseña (mínimo 4 caracteres): ")
        if len(contraseña) < 4:
            print("La contraseña debe tener al menos 4 caracteres. Inténtelo de nuevo.")
        else:
            break
    
    database[nombre_user] = contraseña
    print("Usted está registrado!")

def mostrar_user(database):
    print("Usuarios registrados: ")
    for nombre_user, contraseña in database.items():
        print(f"|Nombre de Usuario: {nombre_user}| |Contraseña: {contraseña}|")
        
def login(database):
    nombre_user = input("Ingrese su nombre de ususario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if nombre_user in database and database[nombre_user] == contraseña:
        print(f"Bienvenido {nombre_user}!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")
    
def pepito():
    
    base_datos = {}

    while True:
        print("Bienvenido al sistema de registro y login de usuarios")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Login de usuario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registro_user(base_datos)
        elif opcion == "2":
            mostrar_user(base_datos)
        elif opcion == "3":
            login(base_datos)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

pepito()             


