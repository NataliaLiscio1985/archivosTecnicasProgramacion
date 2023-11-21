'''
Ejercicio 35 
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa 
que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 
y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa 
en sueldos al personal. 
'''

n = int(input("Ingrese la cantidad de empleados: "))
contador1 = 0   
contador2 = 0
suma = 0

for i in range(n):
    sueldo = int(input("Ingrese el sueldo del empleado: "))
    if sueldo >= 100 and sueldo <= 300:
        contador1 = contador1 + 1
    else:
        contador2 = contador2 + 1
    suma = suma + sueldo
    
print("La cantidad de empleados que cobran entre $100 y $300 es: ", contador1)
print("La cantidad de empleados que cobran mas de $300 es: ", contador2)
print("El importe total que gasta la empresa en sueldos al personal es: $", suma)
