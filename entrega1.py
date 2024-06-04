# Función para registrar usuarios y almacenar en la base de datos
def registrar_usuario(base_de_datos):
    nombre_usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    base_de_datos[nombre_usuario] = contraseña
    print("Usuario registrado con éxito.")

# Función para mostrar la información de la base de datos
def mostrar_base_de_datos(base_de_datos):
    print("Base de datos de usuarios:")
    for usuario, contraseña in base_de_datos.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

# Función para el login de usuarios
def login_usuario(base_de_datos):
    nombre_usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    if nombre_usuario in base_de_datos and base_de_datos[nombre_usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Base de datos de usuarios (diccionario)
base_de_datos = {}

# Menú principal del programa
while True:
    print("\nMenú:")
    print("1. Registrar usuario")
    print("2. Mostrar base de datos de usuarios")
    print("3. Iniciar sesión")
    print("4. Salir")
    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == "1":
        registrar_usuario(base_de_datos)
    elif opcion == "2":
        mostrar_base_de_datos(base_de_datos)
    elif opcion == "3":
        login_usuario(base_de_datos)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
