# Definimos la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def buscar_valor(matriz, valor):
    # Recorremos la matriz para buscar el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retornamos la posición (fila, columna)
    return None  # Si no se encuentra el valor

# Valor a buscar
valor_a_buscar = 5

# Llamamos a la función de búsqueda
resultado = buscar_valor(matriz, valor_a_buscar)

# Mostramos el resultado
if resultado:
    print(f"El valor {valor_a_buscar} se encontró en la posición: {resultado}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")