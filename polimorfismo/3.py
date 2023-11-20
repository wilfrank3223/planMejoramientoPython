# Clase que implementa la sobrecarga del operador +
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sobrecarga del operador +
    def __add__(self, otro_punto):
        nuevo_x = self.x + otro_punto.x
        nuevo_y = self.y + otro_punto.y
        return Punto(nuevo_x, nuevo_y)

# Creación de instancias de la clase Punto
punto1 = Punto(1, 2)
punto2 = Punto(3, 4)

# Uso de la sobrecarga del operador +
resultado = punto1 + punto2

# Impresión de las coordenadas del resultado
print(f"Coordenadas del resultado: ({resultado.x}, {resultado.y})")  # Salida: (4, 6)
