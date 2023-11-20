# Definición de la clase Perro
class Perro:
    # Método de inicialización
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre   # Atributo que almacena el nombre del perro
        self.raza = raza       # Atributo que almacena la raza del perro
        self.edad = edad       # Atributo que almacena la edad del perro
        self.estado = "durmiendo"  # Atributo que indica el estado del perro

    # Método que simula el ladrido del perro
    def ladrar(self):
        print("¡Guau! ¡Guau!")

    # Método que cambia el estado del perro a jugar
    def jugar(self):
        self.estado = "jugando"
        print(f"{self.nombre} está jugando.")

# Creación de una instancia de la clase Perro
mi_perro = Perro("Max", "Labrador", 3)

# Acceso a los atributos de la instancia
print(f"{mi_perro.nombre} es un {mi_perro.raza} de {mi_perro.edad} años.")

# Llamada a los métodos de la instancia
mi_perro.ladrar()
mi_perro.jugar()

# Acceso al atributo actualizado después de llamar al método jugar
print(f"{mi_perro.nombre} está actualmente {mi_perro.estado}.")
