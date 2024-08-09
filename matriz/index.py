def ingresar_matriz():
    # Solicita el tamaño de la matriz
    tamano = int(input("Ingrese el tamaño de la matriz: "))
    
    # Crea la matriz con el tamaño especificado
    matriz = [[0] * tamano for _ in range(tamano)]
    
    # Rellena la matriz con los valores ingresados por el usuario
    for i in range(tamano):
        for j in range(tamano):
            matriz[i][j] = int(input(f"Ingrese la posición {i},{j}: "))
    
    return matriz

# Ejemplo de uso
matriz = ingresar_matriz()
print("Matriz ingresada:")
for fila in matriz:
    print(fila)
