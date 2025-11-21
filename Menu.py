from Datos import Datos 
from Lista import agregar, consultar, modificar, eliminar
while True: # Bucle infinito para el menú
    print("                         ")
    print("-----Menú de opciones-----")
    print("1. Agregar")
    print("2. Consultar")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Salir")
    print("                    ")
    opcion = input("Seleccione una opción: ")
    print("                           ")

    if opcion == "1": #
        agregar()
    if opcion == "2":
        consultar()
    elif opcion == "3":
        modificar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    
