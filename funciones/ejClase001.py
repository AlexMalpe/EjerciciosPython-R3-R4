"""
Ejercicio 6:
Reescribe tu programa de cálculo de pago con el tiempo extra (hora y media) 
y crea una función llamada calcular_pago, la cual reciba dos parámetros (horas y tarifa).
"""

def calcular_pago(horas, tarifa):
    """
    Calcula el salario semanal de un trabajador considerando 
    el pago de horas extras (a 1.5 veces la tarifa normal).
    """

    # Si el trabajador hizo más de 40 horas, calculamos las horas extras
    if horas > 40:
        horas_extras = horas - 40  # Horas trabajadas por encima de 40
        salario = (horas_extras * (tarifa * 1.5)) + ((horas - horas_extras) * tarifa)
    else:
        # Si no hay horas extras, se paga normalmente
        salario = horas * tarifa

    # Devolvemos el salario total calculado
    return salario


# Pedimos los datos al usuario
horas_usuario = float(input("Ingrese el número de horas trabajadas: "))
tarifa_usuario = float(input("Ingrese la tarifa por hora (€): "))

# Llamamos a la función y mostramos el resultado
salario_total = calcular_pago(horas_usuario, tarifa_usuario)
print(f"Tu salario total es de: {salario_total:.2f} €")
