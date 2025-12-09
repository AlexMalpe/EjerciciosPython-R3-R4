"""
Ejercicio 7:
Reescribe el programa de calificaciones del capítulo anterior utilizando una función 
llamada computegrade, que reciba una puntuación (score) como parámetro y devuelva la 
nota (grade) como cadena de texto.
"""

def calificaciones(puntuacion):
    """
    Esta función recibe una puntuación numérica (puntiacion)
    y devuelve una calificación en texto según su valor.
    """

    # Comprobamos que la nota esté dentro del rango válido
    if 0 <= puntuacion <= 10:
        # Clasificamos la nota según el rango
        if puntuacion < 5:
            nota = "Insuficiente"
        elif puntuacion < 7:
            nota = "Suficiente"
        elif puntuacion < 9:
            nota = "Notable"
        else:
            nota = "Sobresaliente"
        
        # Devolvemos el texto completo de la calificación
        return f"Has sacado un {nota}. Tu nota es {puntuacion} sobre 10."
    else:
        # Si la nota no está entre 0 y 10, devolvemos un mensaje de error
        return "Error: la nota debe estar entre 0 y 10."

# Pedimos al usuario que introduzca su nota
notaUsu = float(input("Escriba su nota: "))

# Llamamos a la función y mostramos el resultado
resultado = calificaciones(notaUsu)
print(resultado)
