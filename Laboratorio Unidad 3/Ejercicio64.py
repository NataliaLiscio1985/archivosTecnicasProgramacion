'''
Ejercicio 64 
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a 
lo siguiente: 
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas) 
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar 
"Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" 
si la nota es inferior a 4. 
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”. 
'''

alumnos = []
notas = []
contador = 0

for i in range(4):
    alumnos.append(input("Ingrese el nombre del alumno: "))
    notas.append(int(input("Ingrese la nota del alumno: ")))

print('Listado de alumnos')
print('------------------')
print('')
for i in range(len(alumnos)):
    if notas[i] >= 8:
        contador+=1
        print(alumnos[i], ' tiene ', notas[i], ', condicion: Muy Bueno')
    elif notas[i] >= 4 and notas[i] <= 7:
        print(alumnos[i], ' tiene ', notas[i], ', condicion: Bueno')
    else:
        print(alumnos[i], ' tiene ', notas[i], ' , condicion: Insuficiente')

print('')
print('La cantidad de alumnos con condicion Muy Bueno es: ', contador)

