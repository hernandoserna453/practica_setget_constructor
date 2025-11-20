from Datos import Datos
lista_datos=[]
class Lista:
    def __init__(self,nombres,apellidos,edad,correo,ciudad,pais):
        self.nombre=nombres
        self.apellido=apellidos
        self.edad=edad
        self.correo=correo
        self.ciudad=ciudad
        self.pais=pais
    
def agregar():
    nombres=input("Ingrese sus nombres: ")
    apellidos=input("Ingrese sus apellidos: ")
    edad=int(input("Ingrese su edad: "))
    correo=input("Ingrese su correo electronico: ")
    ciudad=input("Ingrese su ciudad de residencia: ")
    pais=input("Ingrese su pais de nacimiendo: ")
    dato=Datos()
    dato.nombre = nombres
    dato.apellido = apellidos
    dato.edad = edad
    dato.correo = correo
    dato.ciudad = ciudad
    dato.pais = pais
    lista_datos.append(dato)
    print("Datos guardados exitosamente")

def consultar():
    if not lista_datos:
        print("No hay datos para mostrar.")
        return
    for i, dato in enumerate(lista_datos):
        print(f"{i + 1}. Nombre: {dato.nombre}, Apellidos: {dato.apellido}, Edad: {dato.edad}, Correo: {dato.correo}, Ciudad: {dato.ciudad}, Pais: {dato.pais}")

def modificar():
    consultar()
    if not lista_datos:
        return
    indice = int(input("Ingrese el número del dato a modificar: ")) - 1
    if  indice < len(lista_datos):
        nombre = input("Ingrese el nuevo nombre: ")
        apellido = input("Ingrese el nuevo apellido: ")
        edad = int(input("Ingrese la nueva edad: "))
        correo = input("Ingrese el nuevo correo: ")
        ciudad = input("Ingrese la nueva ciudad: ")
        pais = input("Ingrese el nuevo pais: ")
        lista_datos[indice].nombre = nombre
        lista_datos[indice].apellido = apellido
        lista_datos[indice].edad = edad
        lista_datos[indice].correo = correo
        lista_datos[indice].ciudad = ciudad
        lista_datos[indice].pais = pais
        print("Dato modificado exitosamente.")
    else:
        print("Índice inválido.")

def eliminar():
    consultar()
    if not lista_datos:
        return
    indice = int(input("Ingrese el indice del dato a eliminar: ")) - 1
    if indice < len(lista_datos):
        del lista_datos[indice]
        print("Dato eliminado exitosamente...")
    else:
        print("Indice invalido")





        