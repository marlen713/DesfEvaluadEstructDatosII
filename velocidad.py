velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
            14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
            14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
            14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
            10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
            11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

def calcularpromedio(velocidades):
    suma = sum(velocidades)
    promedio = suma / len(velocidades)
    return promedio

def posicionessobre_promedio(velocidades):
    promedio = calcularpromedio(velocidades)
    posiciones = [i for i, v in enumerate(velocidades) if v > promedio]
    return posiciones


print("Las posiciones de las correas sobre el promedio son:", posicionessobre_promedio(velocidad))
