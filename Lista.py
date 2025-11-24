class Datos:
    def __init__(self, nombre, apellido, documento, edad, correo, ciudad, pais):# Constructor con parámetros
        self.nombre = nombre  
        self.apellido = apellido
        self.documento = documento
        self.edad = edad
        self.correo = correo
        self.ciudad = ciudad
        self.pais = pais

lista_datos = [] # Lista para almacenar los objetos Datos

def documento_existe(documento): # Verifica si el documento ya existe
    for dato in lista_datos:# Recorre la lista de datos
        if dato.documento == documento:# Compara el documento
            return True# Si existe, retorna True
    return False# Si no existe, retorna False
def agregar():# Agrega un nuevo objeto Datos a la lista
    print("--- AGREGAR DATOS ---")
    nombre = input("Ingrese sus nombres: ")
    apellido = input("Ingrese sus apellidos: ")
    while True:
        documento = int(input("Ingrese su número de documento: "))# Solicita el documento
        if documento_existe(documento):# Verifica si el documento ya existe
            print("Ese documento ya existe. Ingrese uno diferente por favor.")
        else:
            break# Si no existe, sale del bucle
    edad = int(input("Ingrese su edad: "))
    correo = input("Ingrese su correo electrónico: ")
    ciudad = input("Ingrese su ciudad de residencia: ")
    pais = input("Ingrese su país de nacimiento: ")
    dato = Datos(nombre, apellido, documento, edad, correo, ciudad, pais)

    lista_datos.append(dato)# Agrega el objeto a la lista
    print("Datos guardados exitosamente.")


def consultar(): #Funcion para concultar los datos por el numero de documento
    documento = int(input("Ingrese el número de documento a consultar: ")) # Se solicita el numero de identificacion

    for datos in lista_datos: #Recorre los datos en la lista de datos
        if datos.documento == documento: # Compara datos.documento con documento 
            print("----- Datos encontrados -----") #Aqui muestra los datos si hay datos con el numero de identificacion
            print(f"Nombre: {datos.nombre}")
            print(f"Apellido: {datos.apellido}")
            print(f"Edad: {datos.edad}")
            print(f"Correo: {datos.correo}")
            print("-----------------------------")
            return 
    print("No se encontró un registro con ese numero de documento.") #Si no se encuentran datos aparece este mensaje
    print("-----------------------------")

def modificar():# Modifica un objeto Datos en la lista
    consultar()# Muestra los datos existentes
    if not lista_datos:# Verifica si la lista está vacía
        return
    indice = int(input("Ingrese el número del registro a modificar: ")) - 1# Solicita el índice del registro a modificar
    if 0 <= indice < len(lista_datos):# Verifica si el índice es válido
        print("--- MODIFICAR DATOS ---")
        nombre = input("Nuevo nombre: ")
        apellido = input("Nuevo apellido: ")
        documento = int(input("Nuevo número de documento: "))
        edad = int(input("Nueva edad: "))
        correo = input("Nuevo correo: ")
        ciudad = input("Nueva ciudad: ")
        pais = input("Nuevo país: ")
        lista_datos[indice].nombre = nombre
        lista_datos[indice].apellido = apellido
        lista_datos[indice].documento = documento
        lista_datos[indice].edad = edad
        lista_datos[indice].correo = correo
        lista_datos[indice].ciudad = ciudad
        lista_datos[indice].pais = pais

        print("Registro modificado exitosamente.")
    else:
        print("Índice inválido.")


def eliminar():# Elimina un objeto Datos de la lista
    consultar()# Muestra los datos existentes
    if not lista_datos:# Verifica si la lista está vacía
        return

    indice = int(input("Ingrese el número del registro a eliminar: ")) - 1# Solicita el índice del registro a eliminar

    if 0 <= indice < len(lista_datos):# Verifica si el índice es válido
        del lista_datos[indice]# Elimina el objeto de la lista
        print("Registro eliminado exitosamente.")
    else:
        print("Índice inválido.")
