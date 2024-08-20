class Perro:
    def __init__(self, nombres, peso):
        self.nombres = nombres
        self.peso = peso
        self.estado = "NO HA SIDO ATENDIDO"
        self.tamaño = "Perro Grande" if peso >= 10 else "Perro Peque"

    def registrar(self):
        self.estado = "FUE ATENDIDO"

    def __str__(self):
        return f"Nombre: {self.nombres}, Peso: {self.peso}kg, Tamaño: {self.tamaño}, Estado: {self.estado}"

# Solicitar información del usuario
nombres = input("Ingrese el nombre del perro: ")
peso = float(input("Ingrese el peso del perro en kg: "))

# Crear un objeto Perro con la información proporcionada
perro = Perro(nombres, peso)

# Preguntar si el perro ya ha sido atendido
atendido = input("¿El perro ya fue atendido? (si/no): ").strip().lower()

# Actualizar el estado según la respuesta del usuario
if atendido == "si":
    perro.registrar()

# Mostrar la información del perro
print(perro)