# Definición de la clase Persona
class Persona:
    # Método de inicialización, se ejecuta al crear una nueva instancia de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo que almacena el nombre de la persona
        self.edad = edad      # Atributo que almacena la edad de la persona

    # Método que imprime un mensaje de presentación
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Creación de una instancia de la clase Persona
persona1 = Persona("Juan", 25)
# Llamada al método presentarse de la instancia persona1
persona1.presentarse()
