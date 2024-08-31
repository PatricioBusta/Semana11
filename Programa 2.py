# Definimos la matriz 3x3
matriz = [
    [5, 2, 9],
    [1, 6, 3],
    [8, 4, 7]
]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenar_fila(matriz, fila):
    matriz[fila] = bubble_sort(matriz[fila])
    return matriz

# Fila a ordenar (0-indexed)
fila_a_ordenar = 1

# Ordenamos la fila especificada
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz original y la matriz ordenada
print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz con fila ordenada:")
for fila in matriz_ordenada:
    print(fila)