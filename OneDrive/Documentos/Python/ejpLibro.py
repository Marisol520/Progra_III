class Libro:
    def __init__(self, titulo, autor, ano_publicacion, genero, numero_paginas, precio_compra):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.genero = genero
        self.numero_paginas = numero_paginas
        self.precio_compra = precio_compra

    def calcular_precio_venta(self):
        margen_ganancia = 1.5  
        return self.precio_compra * margen_ganancia

    def mostrar_informacion(self):
        print("\nInformación del Libro:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.ano_publicacion}")
        print(f"Género: {self.genero}")
        print(f"Número de páginas: {self.numero_paginas}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.calcular_precio_venta():.2f}")

def solicitar_informacion():
    print("Ingrese la información del libro:")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano_publicacion = input("Año de publicación: ")
    genero = input("Género: ")
    numero_paginas = int(input("Número de páginas: "))
    precio_compra = float(input("Precio de compra: $"))

    return Libro(titulo, autor, ano_publicacion, genero, numero_paginas, precio_compra)

def gestionar_libros():
    libros = []

    while True:
        libro = solicitar_informacion()
        libros.append(libro)
        
        continuar = input("\n¿Desea agregar otro libro? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\nResumen de Libros:")
    for libro in libros:
        libro.mostrar_informacion()
gestionar_libros()


#Este programa es para ayudar a una librería pequeña a gestionar de manera eficiente el inventario de libros. 
#Permite ingresar fácilmente detalles de cada libro, como título, autor, año de publicación, género, número de páginas y precio de compra. 
#Luego, calcula automáticamente el precio de venta aplicando un margen de ganancia del 50%. 
#La funcionalidad de agregar múltiples libros y mostrar un resumen detallado facilita el manejo del inventario, asegurando precios consistentes y proporcionando una visión clara y organizada de los libros disponibles. 
#Así, resuelve el problema de la gestión manual de inventario, evitando errores y ahorrando tiempo en el cálculo de precios y la visualización de información.