def calcular_inversion(cantidad, interes, anios):
    """Calcula el capital acumulado año a año."""
    for i in range(1, anios + 1):
        cantidad *= (1 + interes / 100)
        print(f"Año {i}: capital = {cantidad:.2f} €")


def main():
    cantidad = float(input("Introduce la cantidad a invertir (€): "))
    interes = float(input("Introduce el interés anual (%): "))
    anios = int(input("Introduce el número de años: "))
    calcular_inversion(cantidad, interes, anios)


# Ejecutar el programa
main()
