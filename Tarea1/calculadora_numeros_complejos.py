import math


# Función para convertir de coordenadas polares a rectangulares
def rectangular(polar):
    # Convertir las coordenadas polares (r, θ) a rectangulares (x, y)
    vect1 = polar[0] * math.cos(math.radians(polar[1]))
    vect2 = polar[0] * math.sin(math.radians(polar[1]))
    rect = [vect1, vect2]
    return rect


# Función para convertir de coordenadas rectangulares a polares
def polar(recta):
    pol = []
    # Calcular el módulo (radio) de la coordenada polar
    pol.append(math.sqrt(recta[0] ** 2 + recta[1] ** 2))
    angulo = 0
    if recta[0] == 0:
        if recta[1] > 0:
            angulo = math.pi / 2
        elif recta[1] < 0:
            angulo = -math.pi / 2
        elif recta[1] == 0:
            angulo = 0
    else:
        angulo = math.atan(recta[1] / recta[0])

    # Ajustar el ángulo basado en el cuadrante
    if recta[0] < 0 and recta[1] >= 0:
        angulo += math.pi
    elif recta[0] < 0 and recta[1] < 0:
        angulo -= math.pi
    pol.append(math.degrees(angulo))  # Convertir el ángulo a grados
    return pol


# Función para sumar dos vectores en coordenadas polares
def suma(polar1, polar2):
    vec1 = rectangular(polar1)
    vec2 = rectangular(polar2)
    sumar = [vec1[0] + vec2[0], vec1[1] + vec2[1]]
    resultpolar = polar(sumar)
    return resultpolar


# Función para multiplicar dos vectores en coordenadas polares
def multiplicar(polar1, polar2):
    modulo = polar1[0] * polar2[0]
    angulo = polar1[1] + polar2[1]
    multi = [modulo, angulo]
    return multi


# Función para sumar tres vectores en coordenadas polares
def suma_3n(polar1, polar2, polar3):
    return suma(suma(polar1, polar2), polar3)
    
