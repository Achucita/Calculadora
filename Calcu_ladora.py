import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def multiplicacion(a,b):
    return a * b

if __name__ == "__main__":
    print("Suma de 5 y 3:", suma(5, 3))
    print("Resta de 5 y 3:", resta(5, 3))
    print("Multiplicación de 3 y 6:", multiplicacion(3, 6))
    try:
	print("Division de 5 y 0:", division(5,0))
    except ValueError as e:
	print(e)
