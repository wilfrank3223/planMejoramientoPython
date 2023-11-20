# Definición de la clase base
class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass  # Método base sin implementación

# Definición de la clase derivada con sobreescritura de método
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Creación de una instancia de la clase derivada
mi_cuadrado = Cuadrado("Rojo", 4)

# Uso del método sobreescrito
print(f"Área del cuadrado ({mi_cuadrado.color}): {mi_cuadrado.area()}")
