# Programa para calcular el capital acumulado de una inversión año a año
# Aplica interés compuesto sobre una cantidad inicial durante un período determinado
#Nuevo cambio realizado

def calcular_inversion(cantidad, interes, anios):
    """
    Calcula el capital acumulado año a año aplicando interés compuesto.
    
    Parámetros:
    - cantidad: Capital inicial a invertir
    - interes: Tasa de interés anual (en porcentaje)
    - anios: Número de años de la inversión
    """
    # Iterar por cada año de la inversión
    for i in range(1, anios + 1):
        # Aplicar el interés compuesto: cantidad = cantidad × (1 + interés/100)
        cantidad *= (1 + interes / 100)
        # Mostrar el capital acumulado en cada año
        print(f"Año {i}: capital = {cantidad:.2f} €")


def main():
    """Función principal que solicita datos al usuario y ejecuta el cálculo."""
    # Solicitar la cantidad inicial a invertir
    cantidad = float(input("Introduce la cantidad a invertir (€): "))
    # Solicitar el interés anual en porcentaje
    interes = float(input("Introduce el interés anual (%): "))
    # Solicitar el número de años de la inversión
    anios = int(input("Introduce el número de años: "))
    # Llamar a la función para calcular y mostrar la inversión
    calcular_inversion(cantidad, interes, anios)


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
