def precioEntrada(edad, es_estudiante, precio_normal=10):

    if edad < 18 or es_estudiante:
        precio_final = precio_normal * 0.5  # 50% de descuento
    else:
        precio_final = precio_normal
    return precio_final

# Capturar datos por teclado
edad = int(input("Ingrese su edad: "))
es_estudiante_input = input("¿Es usted estudiante? (s/n): ").strip().lower()
es_estudiante = es_estudiante_input == 's'

# Mostrar precio final basado en la entrada del usuario
precio = precioEntrada(edad, es_estudiante)
print(f"El precio de su entrada es: {precio}€")

# Ejemplos de uso:
print("Menor de edad:", precioEntrada(16, False))           # 5.0
print("Estudiante:", precioEntrada(20, True))               # 5.0
print("Sin descuentos:", precioEntrada(25, False))          # 10
