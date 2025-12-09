"""
n = int(input("cuantos numeros vas a querer"))
a, b = 0, 1
print (a, b, end=" ")
for i in range (2, n):
    c = a + b
    print (c, end = " ")
    a, b = b, c
"""

ListaNombres = ["ALex", "Paco", "Elena", "Juan", "Pedro"]
ListaNombres2 = ["Malpelo", "perez", "rio", "infanta", "lopez"]

contador = 0

for nombre in ListaNombres:
    for nombre2 in ListaNombres2:

        if nombre != nombre2:
            contador += 1
            nombrecompuesto = nombre + " " + nombre2

            try:
                if nombrecompuesto == "Elena infanta":
                    raise ValueError(f"{nombrecompuesto}: instituto Galapagar")
                else:
                    print(nombrecompuesto)

            except ValueError as e:
                print(e)

print(f"Al FINAL ha habido {contador} nombres compuestos")
