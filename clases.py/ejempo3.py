# Definición de la clase Coche
class Coche:
    # Método de inicialización
    def __init__(self, marca, modelo, color):
        self.marca = marca    # Atributo que almacena la marca del coche
        self.modelo = modelo  # Atributo que almacena el modelo del coche
        self.color = color    # Atributo que almacena el color del coche
        self.encendido = False  # Atributo que indica si el coche está encendido o apagado

    # Método que enciende el coche
    def encender(self):
        self.encendido = True
        print(f"El coche {self.marca} {self.modelo} está encendido.")

    # Método que apaga el coche
    def apagar(self):
        self.encendido = False
        print(f"El coche {self.marca} {self.modelo} está apagado.")

# Creación de una instancia de la clase Coche
coche1 = Coche("Toyota", "Corolla", "Azul")
# Llamadas a los métodos encender y apagar de la instancia coche1
coche1.encender()
coche1.apagar()
