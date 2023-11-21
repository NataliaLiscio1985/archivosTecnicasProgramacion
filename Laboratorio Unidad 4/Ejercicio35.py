'''
Ejercicio 35 
Crear un diccionario en Python que defina como clave el número de documento de una persona y 
como valor un string con su nombre. 
Desarrollar las siguientes funciones: 
1) Cargar por teclado los datos de 4 personas. 
2) Listado completo del diccionario. 
3) Consulta del nombre de una persona ingresando su número de documento.
'''

def cargaDatos():
    datos = {}
    for i in range(4):
        documento = int(input("Ingrese el número de documento: "))
        nombre = input("Ingrese el nombre: ")
        datos[documento] = nombre
    return datos

def imprimir(datos):
    for documento, nombre in datos.items():
        print(documento, nombre)
        
def consulta(datos):
    documento = int(input("Ingrese el número de documento a consultar: "))
    if documento in datos:
        print("El nombre de la persona es", datos[documento])
    else:
        print("No existe una persona con dicho documento")

# Bloque principal del programa

datos = cargaDatos()
print("Listado completo del diccionario")
imprimir(datos)
consulta(datos)

