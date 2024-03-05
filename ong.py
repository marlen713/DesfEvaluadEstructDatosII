
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def productoria(lista):
    result = 1
    for num in lista:
        result *= num
    return result

def calcular(**kwargs):
    for key, value in kwargs.items():
        if key.startswith('fact'):
            print(f"El factorial de {value} es {factorial(value)}")
        elif key.startswith('prod'):
            print(f"La productoria de {value} es {productoria(value)}")

calcular(fact1 = 5, prod1 = [3,6,4,2,8], fact_2 = 6)  #LOS NUMEROS DE PROD1 = [3,6,4,2,8] cREO QUE ESTAN MAL YA QUE HICE MIL GESTIONES Y NUNCA ME DAN EL NUMERO DE LA GUIA