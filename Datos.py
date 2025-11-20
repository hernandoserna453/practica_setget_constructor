class Datos:
    def __init__(self):
        self._nombre = ""
        self._edad = 0
    
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_edad(self):
        return self._edad
    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad no puede ser negativa")
    nombre = property(get_nombre, set_nombre)
    edad = property(get_edad, set_edad)
# Ejemplo de uso
if __name__ == "__main__":
    datos = Datos()
    datos.nombre = "Juan"
    datos.edad = 30
    print(f"Nombre: {datos.nombre}, Edad: {datos.edad}")