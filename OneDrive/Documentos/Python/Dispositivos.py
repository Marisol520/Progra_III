class Dispositivo:
    def __init__(self, modelo, tamano_pant, capacidad_alm, memoria_ram, procesador, sistema_operativo, precio_compra):
        self.modelo = modelo
        self.tamano_pant= tamano_pant
        self.capacidad_alm = capacidad_alm
        self.memoria_ram = memoria_ram
        self.procesador = procesador
        self.sistema_operativo = sistema_operativo
        self.precio_compra = precio_compra

    def calcular_precio_venta(self):
        return self.precio_compra * 1.7

    def mostrar_informacion(self):
        print("\nInformación del Dispositivo:")
        print(f"Modelo: {self.modelo}")
        print(f"Tamaño de pantalla: {self.tamano_pant}")
        print(f"Capacidad de almacenamiento: {self.capacidad_alm}")
        print(f"Memoria RAM: {self.memoria_ram}")
        print(f"Procesador: {self.procesador}")
        print(f"Sistema operativo: {self.sistema_operativo}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.calcular_precio_venta():.2f}")

def solicitar_informacion():
    print("Ingrese la información del dispositivo:")
    modelo = input("Modelo: ")
    tamano_pant = input("Tamaño de pantalla: ")
    capacidad_alm = input("Capacidad de almacenamiento: ")
    memoria_ram = input("Memoria RAM: ")
    procesador = input("Procesador: ")
    sistema_operativo = input("Sistema operativo: ")
    precio_compra = float(input("Precio de compra: $"))

    return Dispositivo(modelo, tamano_pant, capacidad_alm, memoria_ram, procesador, sistema_operativo, precio_compra)

def gestionar_dispositivos():
    dispositivos = []

    while True:
        dispositivo = solicitar_informacion()
        dispositivos.append(dispositivo)
        continuar = input("\n¿Desea agregar otro dispositivo? (s/n): ").strip().lower()
        if continuar != 's':
            break


    print("\nResumen de Dispositivos:")
    for dispositivo in dispositivos:
        dispositivo.mostrar_informacion()

gestionar_dispositivos()
