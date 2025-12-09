def cuenta_atras(numero):
    """Muestra una cuenta atrás desde el número hasta 0."""
    if numero < 0:
        print("El número debe ser positivo.")
    else:
        for i in range(numero, -1, -1):
            if i == 0:
                print(i)
            else:
                print(i, end=", ")


def main():
    numero = int(input("Introduce un número entero positivo: "))
    cuenta_atras(numero)


# Ejecutar el programa
main()
