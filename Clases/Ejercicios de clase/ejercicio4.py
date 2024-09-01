##Creación de una matriz

filas = int(input("Ingresa el numero de filas: "))
columnas = int(input("Ingresa el numero de columnas: "))

matriz = []
print("\n Por favor, ingresa los valores de la matriz:")

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Elemento [{i+1}] [{j+1}]: "))
        fila.append(valor)
    
    matriz.append(fila)
    
print("\n La matriz ingresada es:")
for fila in matriz:
    print(fila)