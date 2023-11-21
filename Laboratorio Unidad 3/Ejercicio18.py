""" 
Ejercicio 18 
Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje 
"Promocionado". 
"""

n1 = float(input("Ingrese la primera nota: "))
n2= float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercer nota: "))

promedio = (n1+n2+n3)/3

if promedio >= 7:
    print("Promocionado")
else:   
    print("No promocionado")
    
    