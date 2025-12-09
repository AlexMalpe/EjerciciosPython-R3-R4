# --------------------------------------------------------------
#  Ejercicio 6: Creador de menú de cine 
# --------------------------------------------------------------
# Escribe un programa en Python que simule la compra de un menú de cine.
#
# El usuario deberá seguir este flujo:
#   1️⃣ Elegir tipo de entrada (Normal, VIP o Infantil).
#   2️⃣ Elegir combo de comida (Palomitas, Nachos o Hot Dog).
#   3️⃣ Elegir bebida (Refresco, Agua o Cerveza).
#   4️⃣ Elegir método de pago (Efectivo o Tarjeta).
#
# El programa debe:
#   ✅ Mostrar un resumen final con los precios y el total.
#   ✅ Aplicar un 10% de descuento si el pago es con tarjeta.
#   ✅ Controlar errores si el usuario introduce un número fuera de rango.
# --------------------------------------------------------------

#opciones disponibles y sus precios
entradas = {
    1: ("Normal", 8.0),
    2: ("VIP", 12.0),
    3: ("Infantil", 6.0)
}

combos = {
    1: ("Palomitas", 4.5),
    2: ("Nachos", 5.0),
    3: ("Hot Dog", 4.0)
}

bebidas = {
    1: ("Refresco", 2.5),
    2: ("Agua", 1.5),
    3: ("Cerveza", 3.0)
}

print(" Bienvenido al Creador de Menú de Cine ")

# --------------------------------------------------------------
# Función auxiliar para mostrar las opciones disponibles
# --------------------------------------------------------------
def mostrar_opciones(diccionario, titulo):
    """
    Muestra las opciones (clave, nombre y precio) de un diccionario.
    """
    print(f"\n{titulo}:")
    for num, (nombre, precio) in diccionario.items():
        print(f"{num}. {nombre} - {precio}€")

# --------------------------------------------------------------
# ELECCIÓN DE ENTRADA
# --------------------------------------------------------------
mostrar_opciones(entradas, "Tipos de entrada")

# Bucle que se repite hasta que el usuario introduzca una opción válida
while True:
    try:
        op_entrada = int(input("Elige tu tipo de entrada (1-3): "))
        if op_entrada in entradas:
            break  # Opción válida → salimos del bucle
        else:
            print(" Opción no válida, intenta de nuevo.")
    except ValueError:
        print(" Debes introducir un número.")

# --------------------------------------------------------------
# ELECCIÓN DE COMBO DE COMIDA
# --------------------------------------------------------------
mostrar_opciones(combos, "Combos de comida")

while True:
    try:
        op_combo = int(input("Elige tu combo (1-3): "))
        if op_combo in combos:
            break
        else:
            print(" Opción no válida, intenta de nuevo.")
    except ValueError:
        print(" Debes introducir un número.")

# --------------------------------------------------------------
# ELECCIÓN DE BEBIDA
# --------------------------------------------------------------
mostrar_opciones(bebidas, "Bebidas disponibles")

while True:
    try:
        op_bebida = int(input("Elige tu bebida (1-3): "))
        if op_bebida in bebidas:
            break
        else:
            print(" Opción no válida, intenta de nuevo.")
    except ValueError:
        print(" Debes introducir un número.")

# --------------------------------------------------------------
# MÉTODO DE PAGO
# --------------------------------------------------------------
while True:
    pago = input("\nMétodo de pago (efectivo/tarjeta): ").lower()
    if pago in ["efectivo", "tarjeta"]:
        break
    else:
        print(" Escribe 'efectivo' o 'tarjeta'.")

# --------------------------------------------------------------
# CÁLCULOS
# --------------------------------------------------------------
# Obtenemos los nombres y precios seleccionados por el usuario
entrada, precio_entrada = entradas[op_entrada]
combo, precio_combo = combos[op_combo]
bebida, precio_bebida = bebidas[op_bebida]

# Sumamos el total
total = precio_entrada + precio_combo + precio_bebida

# Si paga con tarjeta → aplica descuento del 10%
if pago == "tarjeta":
    descuento = total * 0.10
    total -= descuento
else:
    descuento = 0

# --------------------------------------------------------------
# RESULTADOS FINALES
# --------------------------------------------------------------
print("\n---  RESUMEN DE TU COMPRA ---")
print(f"Entrada: {entrada} - {precio_entrada}€")
print(f"Comida: {combo} - {precio_combo}€")
print(f"Bebida: {bebida} - {precio_bebida}€")

if descuento > 0:
    print(f"Descuento aplicado (10%): -{descuento:.2f}€")

print(f"Método de pago: {pago.capitalize()}")
print(f" Total a pagar: {total:.2f}€")
print("\n ¡Disfruta de tu película")
