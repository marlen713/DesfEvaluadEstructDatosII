
import sys

precios = {'Notebook': 700000,
            'Teclado': 25000,
            'Mouse': 12000,
            'Monitor': 250000,
            'Escritorio': 135000,
            'Tarjeta de Video': 1500000}

def filtrarproductos(precios, umbral, condicion='mayor'):
    productosfiltrados = []
    
    for producto, precio in precios.items():
        if (condicion == 'mayor' and precio > umbral) or (condicion == 'menor' and precio < umbral):
            productosfiltrados.append(producto)
    
    return productosfiltrados

if len(sys.argv) == 2:
    umbral = int(sys.argv[1])
    productos = filtrarproductos(precios, umbral)
    print(f"Los productos mayores al umbral son: {', '.join(productos)}")
elif len(sys.argv) == 3:
    umbral = int(sys.argv[1])
    condicion = sys.argv[2]
    
    if condicion == 'mayor':
        productos = filtrarproductos(precios, umbral, 'mayor')
        print(f"Los productos mayores al umbral son: {', '.join(productos)}")
    
    elif condicion == 'menor':
        productos = filtrarproductos(precios, umbral, 'menor')
        print(f"Los productos menores al umbral son: {', '.join(productos)}")
    else:
        print("Lo sentimos, no es una operación válida.")
else:
    print("Por favor, ingresa un umbral y opcionalmente la condición 'mayor' o 'menor'.")