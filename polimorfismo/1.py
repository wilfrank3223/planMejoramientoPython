# Definición de la clase Animal
class Animal:
    def hablar(self):
        pass  # Método base sin implementación

# Definición de la clase Perro que hereda de Animal
class Perro(Animal):
    def hablar(self):
        return "Guau"

# Definición de la clase Gato que hereda de Animal
class Gato(Animal):
    def hablar(self):
        return "Miau"

# Función que utiliza polimorfismo con objetos de diferentes clases
def hacer_hablar(animal):
    return animal.hablar()

# Creación de instancias de las clases Perro y Gato
mi_perro = Perro()
mi_gato = Gato()

# Llamada a la función con diferentes tipos de objetos
print(hacer_hablar(mi_perro))  # Salida: Guau
print(hacer_hablar(mi_gato))   # Salida: Miau
