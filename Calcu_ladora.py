import math

def suma(a, b):
    return a + b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

if __name__ == "__main__":
    print("Suma de 5 y 3:", suma(5, 3))
