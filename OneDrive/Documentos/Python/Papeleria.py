class Item:
    def __init__(self, tipo, descripcion, precio_compra):
        self.tipo = tipo
        self.descripcion = descripcion
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.30

    def __str__(self):
        return f"Tipo: {self.tipo}, Descripción: {self.descripcion}, Precio Compra: {self.precio_compra:.2f}, Precio Venta: {self.precio_venta:.2f}"

def obtener_datos_item():
    tipo = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción: ")
    precio_compra = float(input("Ingrese el precio de compra: "))
    return Item(tipo, descripcion, precio_compra)

print("Ingrese los datos del primer producto:")
producto1 = obtener_datos_item()
print("\nIngrese los datos del segundo producto:")
producto2 = obtener_datos_item()

print("\nInformación de los productos:")
print(producto1)
print(producto2)
