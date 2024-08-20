class Auto:
    def __init__(self, marca, modelo, año, color, tipo, combustible, precio_compra, tipo_carroceria, transmision):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo = tipo  
        self.combustible = combustible
        self.precio_compra = precio_compra
        self.tipo_carroceria = tipo_carroceria
        self.transmision = transmision
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.4

    def mostrar_informacion(self):
        info = (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Año: {self.año}\n"
            f"Color: {self.color}\n"
            f"Tipo: {self.tipo}\n"
            f"Combustible: {self.combustible}\n"
            f"Precio de Compra: ${self.precio_compra:.2f}\n"
            f"Tipo de Carrocería: {self.tipo_carroceria}\n"
            f"Transmisión: {self.transmision}\n"
            f"Precio de Venta: ${self.precio_venta:.2f}\n"
        )
        return info

def convertir_precio(precio_str):
    """
    Convierte un precio en formato de miles o millones a formato numérico.
    Ejemplo: '50k' -> 50000, '2.5m' -> 2500000
    """
    precio_str = precio_str.strip().lower()
    if precio_str.endswith('k'):
        return float(precio_str[:-1]) * 1_000
    elif precio_str.endswith('m'):
        return float(precio_str[:-1]) * 1_000_000
    else:
        return float(precio_str)

def registrar_auto():
    print("\nRegistro de un Auto")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))
    color = input("Color: ")
    tipo = input("Tipo (Nacional/Importado): ")
    combustible = input("Combustible: ")
    
    while True:
        precio_compra_str = input("Precio de Compra (puede usar 'k' para miles o 'm' para millones): $")
        try:
            precio_compra = convertir_precio(precio_compra_str)
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa el precio en el formato correcto.")

    tipo_carroceria = input("Tipo de Carrocería: ")
    transmision = input("Transmisión: ")
    
    auto = Auto(
        marca, modelo, año, color, tipo, combustible, precio_compra, tipo_carroceria, transmision
    )
    return auto

def main():
    autos = []
    while True:
        auto = registrar_auto()
        autos.append(auto)
        
        continuar = input("\n¿Deseas agregar otro auto? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    print("\nInformación de los Autos Registrados:")
    for auto in autos:
        print(auto.mostrar_informacion())
        print('-' * 40)  

if __name__ == "__main__":
    main()
