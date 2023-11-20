# Definición de la clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass  # Método base sin implementación

# Definición de la clase derivada que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

# Creación de una instancia de la clase derivada
mi_perro = Perro("Buddy")

# Acceso a atributos de la clase base
print(f"{mi_perro.nombre} hace el sonido: {mi_perro.hacer_sonido()}")
