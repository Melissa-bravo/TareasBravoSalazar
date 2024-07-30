def operation_selector(num1, num2, op):
    # Verifica si num1 y num2 son enteros
    if type(num1) != int or type(num2) != int:
        return -50, None  # Código de error -50 si alguno no es entero
    # Verifica si op es una string
    if type(op) != str:
        return -60, None  # Código de error -60 si op no es una string
    # Verifica si op es una operación válida
    if op not in ["+", "-", "*", "&"]:
        return -70, None  # Código de error -70 si op no es válido

    # Realiza la operación correspondiente según el valor de op
    if op == "+":
        return 0, num1 + num2  # Suma
    if op == "-":
        return 0, num1 - num2  # Resta
    if op == "*":
        return 0, num1 * num2  # Multiplicación
    if op == "&":
        return 0, num1 & num2  # Operación AND


def calculo_promedio(lista):
    # Verifica si todos los elementos en la lista son enteros
    for i in lista:
        if type(i) != int:
            return -80, None  # Error si algún elemento no es entero
    # Verifica si la longitud de la lista es mayor a 10
    if len(lista) > 10:
        return -90, None  # Error de la lista si tiene mas de 10 elementos
    # Calcula y devuelve el promedio de la lista
    return 0, sum(lista) / len(lista)

