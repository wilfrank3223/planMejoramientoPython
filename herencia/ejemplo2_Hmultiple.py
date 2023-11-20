# Definición de la clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Definición de la primera clase derivada
class Coche(Vehiculo):
    def conducir(self):
        return "Conduciendo el coche"

# Definición de la segunda clase derivada con herencia múltiple
class Bicicleta(Vehiculo):
    def pedalear(self):
        return "Pedalear la bicicleta"

class VehiculoEcologico(Coche, Bicicleta):
    pass  # No se define ningún método adicional

# Creación de una instancia de la clase derivada con herencia múltiple
mi_vehiculo_ecologico = VehiculoEcologico("Tesla", "Model S")

# Uso de métodos de ambas clases derivadas y la clase base
print(f"{mi_vehiculo_ecologico.marca} {mi_vehiculo_ecologico.modelo}: {mi_vehiculo_ecologico.conducir()} y {mi_vehiculo_ecologico.pedalear()}")
