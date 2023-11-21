'''
Ejercicio 34 
Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y 
como valor el precio del mismo. 
Desarrollar además las funciones de: 
1) Imprimir en forma completa el diccionario 
2) Imprimir solo los artículos con precio superior a 100
'''



def cargaproductos():
    productos = {}
    for i in range(5):
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        productos[nombre] = precio
        
    return productos

def imprimir(productos):
    for nombre, precio in productos.items():
        print(nombre, precio)
        
def imprimir_mayor100(productos):
    for nombre, precio in productos.items():
        if precio > 100:
            print(nombre, precio)

# Bloque principal del programa

productos = cargaproductos()
print("Lista completa de productos\n")
imprimir(productos)
print("\nLista de productos con precio mayor a 100\n")
imprimir_mayor100(productos)
