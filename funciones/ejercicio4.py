def mostrar_menu():
    print("\n--- MENÚ FRUTERÍA ---")
    print("1. Añadir stock")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Salir")


def pedir_producto(inventario, prompt="¿Qué producto?: "):
    producto = input(prompt).strip().lower()
    return producto if producto in inventario else None


def anadir_stock(inventario):
    producto = pedir_producto(inventario, "¿Qué producto quieres añadir (manzanas, peras, plátanos)? ")
    if not producto:
        print(" Producto no válido.")
        return

    try:
        cantidad = int(input("Cantidad a añadir: "))
        if cantidad < 0:
            print(" La cantidad debe ser un número positivo.")
            return
        inventario[producto] += cantidad
        print(f" Añadidas {cantidad} {producto}.")
    except ValueError:
        print(" Debes introducir un número válido.")


def vender_producto(inventario):
    producto = pedir_producto(inventario, "¿Qué producto quieres vender (manzanas, peras, platanos)? ")
    if not producto:
        print(" Producto no válido.")
        return

    try:
        cantidad = int(input("Cantidad a vender: "))
        if cantidad < 0:
            print(" La cantidad debe ser un número positivo.")
            return
        if cantidad <= inventario[producto]:
            inventario[producto] -= cantidad
            print(f" Vendidas {cantidad} {producto}.")
        else:
            print(" No hay suficiente stock.")
    except ValueError:
        print(" Debes introducir un número válido.")


def mostrar_inventario(inventario):
    print("\n Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"  - {producto.capitalize()}: {cantidad}")


def main():
    inventario = {"manzanas": 0, "peras": 0, "plátanos": 0}

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            anadir_stock(inventario)
        elif opcion == "2":
            vender_producto(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
