'''
Ejercicio 5 
Se solicita escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y 
devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es 
válido. 
Debes utilizar las funciones previamente escritas y probadas del ejercicio 3 y 4. 
Agrega algunos casos de prueba al código.
'''
def is_year_leap(year):
    if year% 4!= 0:
        return False
    elif year % 100!= 0:
        return True
    elif year% 400!= 0:
        return False
    else:
        return True 
        
    
def fecha_valida (year, month, day):
    if day <1 or day >31 or month <1 or month >12 or year <1500:        
        return False
    elif month == 2:
        if day > 29:
            return False
        elif day == 29 and is_year_leap(year):
            return True
        else:
            return False
    else:
        return True
 
def def_dia_mes(year, month, day):
    if fecha_valida:
        dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
        if is_year_leap(year):
            dias_mes[1] = 29
    for i in range(month-1):
        day += dias_mes[i]
    return day         


print(def_dia_mes(2020, 2, 29))