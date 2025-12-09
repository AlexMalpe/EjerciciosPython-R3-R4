"""
EJERCICIO: Clasificador de palabras

Escribe un programa en Python que pida al usuario un texto y clasifique sus palabras según estas reglas:

- Palabras que empiezan por vocal.
- Palabras que terminan en consonante.
- Palabras que contienen algún número.

El programa debe:

- Separar el texto en palabras.
- Detectar cuáles cumplen cada condición.
- Guardarlas en un diccionario con tres listas.
- Mostrar un informe final indicando las palabras encontradas en cada categoría
  y cuántas hay en cada una.
"""
def empieza_por_vocal(palabra):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return len(palabra) > 0 and palabra[0] in vocales


def termina_en_consonante(palabra):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return len(palabra) > 0 and palabra[-1] in consonantes


def contiene_numeros(palabra):
    for caracter in palabra:
        if caracter.isdigit():
            return True
    return False


def clasificar_palabras(texto):
    palabras = texto.split()

    categorias = {
        "empiezan_vocal": [],
        "terminan_consonante": [],
        "con_numeros": []
    }

    for palabra in palabras:
        if empieza_por_vocal(palabra):
            categorias["empiezan_vocal"].append(palabra)

        if termina_en_consonante(palabra):
            categorias["terminan_consonante"].append(palabra)

        if contiene_numeros(palabra):
            categorias["con_numeros"].append(palabra)

    return categorias


def imprimir_informe(categorias):
    print("\n--- INFORME DE PALABRAS ---")

    print("\n1. Palabras que empiezan por vocal:")
    print(categorias["empiezan_vocal"], "→", len(categorias["empiezan_vocal"]))

    print("\n2. Palabras que terminan en consonante:")
    print(categorias["terminan_consonante"], "→", len(categorias["terminan_consonante"]))

    print("\n3. Palabras que contienen números:")
    print(categorias["con_numeros"], "→", len(categorias["con_numeros"]))


def main():
    texto = input("Introduce un texto: ")
    categorias = clasificar_palabras(texto)
    imprimir_informe(categorias)


if __name__ == "__main__":
    main()
