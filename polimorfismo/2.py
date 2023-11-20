# Función que realiza una operación específica
def area(objeto):
    return objeto.calcular_area()

# Clase base que define un método sin implementación
class Figura:
    def calcular_area(self):
        pass

# Clase derivada que implementa el método calcular_area
class Cuadrado(Figura):
    def calcular_area(self):
        lado = 4
        return lado ** 2

# Clase derivada que implementa el método calcular_area de manera diferente
class Circulo(Figura):
    def calcular_area(self):
        radio = 3
        return 3.14 * radio ** 2

# Creación de instancias de las clases Cuadrado y Circulo
mi_cuadrado = Cuadrado()
mi_circulo = Circulo()

# Llamada a la función con diferentes tipos de objetos
print(area(mi_cuadrado))  # Salida: 16
print(area(mi_circulo))   # Salida: 28.26
