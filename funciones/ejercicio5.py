# Ejercicio 5: Montador de menú rápido

# Opciones del menú con precios
platos = {1: ("Hamburguesa", 6.5), 2: ("Pizza", 7.0), 3: ("Ensalada", 5.5)}
bebidas = {1: ("Agua", 1.5), 2: ("Refresco", 2.0), 3: ("Cerveza", 2.5)}
complementos = {1: ("Patatas", 2.0), 2: ("Ensaladilla", 2.5), 3: ("Helado", 3.0)}

print(" Bienvenido al Montador de Menú Rápido")

# Selección del plato
print("\nPlatos:")
for num, (nombre, precio) in platos.items():
    print(f"{num}. {nombre} - {precio}€")
op_plato = int(input("Elige un plato (1-3): "))

# Selección de bebida
print("\nBebidas:")
for num, (nombre, precio) in bebidas.items():
    print(f"{num}. {nombre} - {precio}€")
op_bebida = int(input("Elige una bebida (1-3): "))

# Selección de complemento
print("\nComplementos:")
for num, (nombre, precio) in complementos.items():
    print(f"{num}. {nombre} - {precio}€")
op_complemento = int(input("Elige un complemento (1-3): "))

# Método de pago
pago = input("\nMétodo de pago (efectivo/tarjeta): ").lower()

# Cálculo del total
plato, precio_plato = platos[op_plato]
bebida, precio_bebida = bebidas[op_bebida]
complemento, precio_complemento = complementos[op_complemento]
total = precio_plato + precio_bebida + precio_complemento

# Resume
print("\n---  RESUMEN DE TU PEDIDO ---")
print(f"Plato: {plato} - {precio_plato}€")
print(f"Bebida: {bebida} - {precio_bebida}€")
print(f"Complemento: {complemento} - {precio_complemento}€")
print(f"Método de pago: {pago.capitalize()}")
print(f" Total: {total:.2f} €")
print("¡Gracias por tu compra! ")
