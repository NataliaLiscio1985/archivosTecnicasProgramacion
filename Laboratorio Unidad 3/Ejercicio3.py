"""
Ejercicio 3 
 
Se debe calcular el pago de un impuesto, denominado Impuesto Personal de Ingresos (IPI, para 
abreviar) utilizando la siguiente regla: 
 
• si el ingreso del ciudadano no era superior a $85528, el impuesto era igual al 18% del ingreso 
menos $556,02 (esta fue la llamada exención fiscal). 
• si el ingreso era superior a esta cantidad, el impuesto era igual a $14839.02, más el 32% del 
excedente sobre 85528 pesos. (Formula = (valoringresado – 85528) x 0.32 + 14839.02) 
 Información Privada 
• Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es 
igual a cero). 
 
Tu tarea es escribir una calculadora de impuestos. 
Debe aceptar un valor de punto flotante: el ingreso. 
A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función 
llamada round() que hará el redondeo
"""

valoringresado = float(input("Ingrese el valor del salario: "))
if(valoringresado <= 85528):
    impuesto = valoringresado * 0.18 - 556.02
else:
    impuesto = (valoringresado - 85528) * 0.32 + 14839.02

if(impuesto > 0):
    print("El impuesto es: ", round(impuesto, 0))
else:
    print("No debe abonar IPI")
    

