# Función tipo ALU con control de errores


def operation_selector(num1, num2, op):
    # Verifica si num1 y num2 son enteros
    if not isinstance(num1, int) or not isinstance(num2, int):
        return -50, None  # código de error -50 si alguno no es entero
    # Verifica si op es una string
    if not isinstance(op, str):
        return -60, None  # código de error -60 si op no es una string
    # Verifica si op es una operación válida
    if op not in ["+", "-", "*", "&"]:
        return -70, None  # código de error -70 si op no es operación válida

    # Realiza la operación correspondiente según el valor de op
    if op == "+":
        return 0, num1 + num2  # Suma
    if op == "-":
        return 0, num1 - num2  # Resta
    if op == "*":
        return 0, num1 * num2  # Multiplicación
    if op == "&":
        return 0, num1 & num2  # Operación AND

# Función promedio con control de errores


def calculo_promedio(lista):
    # Verifica si todos los elementos en la lista son enteros
    if not all(isinstance(i, int) for i in lista):
        return -80, None  # código de error -80 si elemento no es entero
    # Verifica si la longitud de la lista es mayor a 10
    if len(lista) > 10:
        return -90, None  # código de error -90 si hay más de 10
    # Calcula y devuelve el promedio de la lista
    return 0, sum(lista) / len(lista)
