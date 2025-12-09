# Función que lanza un error en caso de que nombre1 sea Infanta y nombre2 sea Elena con mensaje personalizado
def comprobar_nombre(nom1, nom2):
    if nom1 == "Infanta" and nom2 == "Elena":
        raise ValueError(f"IES {nom1} {nom2} en Galapagar con estudios de formación profesional")


# Función para comprobar que los números introducidos no son negativos
def validar_numero(numero):
    if numero < 0:
        raise ValueError("Número inválido, los números no pueden ser negativos")


#Ejercicio1 nombres compuestos
lista1_nombre = ["Trajano", "Adriano", "Antonia", "Penélope", "Infanta"]
lista2_nombre = ["Elena", "Alejandro", "Odiseo", "Penélope", "Monica"]
cont_nombre = 0

for nombre1 in lista1_nombre:
    lista_nom_compuestos = []
    for nombre2 in lista2_nombre:
        try:
            comprobar_nombre(nombre1, nombre2)
            if nombre1 == nombre2:
                continue
            else:
                cont_nombre += 1
                lista_nom_compuestos.append((nombre1, nombre2))
        except ValueError as e:
            print(e)

    print(f"Lista de nombres compuestos de {nombre1}:")
    for lista_compuestos in lista_nom_compuestos:
        print(lista_compuestos)

print(f"Se han generado un total de: {cont_nombre} nombres compuestos")
def comprobar_nombre(nombre1, nombre2):
    """
    Esta función comprueba si los nombres son iguales.
    Si son iguales, lanza una excepción ValueError.
    """
    if nombre1 == nombre2:
        raise ValueError(f"Los nombres '{nombre1}' y '{nombre2}' son iguales y no se pueden combinar.") 
    



    print("EJERCICIO 1")
listaNombre = ["Manuel", "Infanta", "Elena", "Santa", "Juan"]
listaNombre2 = ["Manuel", "Infanta", "Elena", "Santa", "Juan"]

contador = 0

for nombre in listaNombre:
    for nombre2 in listaNombre2:
        if nombre != nombre2:
            contador += 1
            nombreCompuesto = nombre + " " + nombre2
            try:
                if nombreCompuesto == "Infanta Elena":
                    raise ValueError(f"{nombreCompuesto}: IES en Galapagar con estudios de formación profesional")
                else:
                    print(f"{nombreCompuesto}")
            except ValueError as e:
                print(e)

print(f"Al FINAL ha habido {contador} nombres compuestos")