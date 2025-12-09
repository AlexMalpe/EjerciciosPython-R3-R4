# Ejercicio 3: Múltiplos de 7 entre 80 y 200

for i in range(81, 200):
    if i % 7 == 0:
        print(f"El primer múltiplo de 7 mayor que 80 y menor que 200 es: {i}")
        break
